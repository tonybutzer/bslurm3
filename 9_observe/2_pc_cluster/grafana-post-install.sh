#!/bin/bash

#source the AWS ParallelCluster profile
. /etc/parallelcluster/cfnconfig

yum -y install glibc-static

s3_bucket=$(echo $cfn_postinstall | sed "s/s3:\/\///g;s/\/.*//")

case "${cfn_node_type}" in
MasterServer)

#Unsupported
#cfn_efs=$(cat /etc/chef/dna.json | grep \"cfn_efs\" | awk '{print $2}' | sed "s/\",//g;s/\"//g")
#cfn_cluster_cw_logging_enabled=$(cat /etc/chef/dna.json | grep \"cfn_cluster_cw_logging_enabled\" | awk '{print $2}' | sed "s/\",//g;s/\"//g")
cfn_fsx_fs_id=$(cat /etc/chef/dna.json | grep \"cfn_fsx_fs_id\" | awk '{print $2}' | sed "s/\",//g;s/\"//g")

#Supported
master_instance_id=$(ec2-metadata -i | awk '{print $2}')
cfn_max_queue_size=$(aws cloudformation describe-stacks --stack-name $stack_name --region $cfn_region | jq -r '.Stacks[0].Parameters | map(select(.ParameterKey == "MaxSize"))[0].ParameterValue')


# Install docker to simplify Prometheus & Grafana deployment
yum -y install docker git golang-bin make
service docker start
chkconfig docker on
usermod -a -G docker $cfn_cluster_user


wget "${2}"
unzip master.zip ../Grafana/files/grafana/*
unzip master.zip ../Grafana/files/nginx/*
unzip master.zip ../Grafana/files/www/*
mv Grafana/files/* /home/$cfn_cluster_user/

unzip -j master.zip ../Grafana/files/prometheus.yml -d /home/$cfn_cluster_user
unzip -j master.zip ../Grafana/files/1h-cost-metrics.sh -d /usr/local/bin/
unzip -j master.zip ../Grafana/files/1m-cost-metrics.sh -d /usr/local/bin/
unzip -j master.zip ../Grafana/files/aws-region.py -d /usr/local/bin/

chmod +x /usr/local/bin/1h-cost-metrics.sh 
chmod +x /usr/local/bin/1m-cost-metrics.sh 

chown $cfn_cluster_user:$cfn_cluster_user /usr/local/bin/1h-cost-metrics.sh 
chown $cfn_cluster_user:$cfn_cluster_user /usr/local/bin/1m-cost-metrics.sh
chown $cfn_cluster_user:$cfn_cluster_user /usr/local/bin/aws-region.py

chown $cfn_cluster_user:$cfn_cluster_user -R /home/$cfn_cluster_user/

(crontab -l -u $cfn_cluster_user; echo "*/1 * * * * /usr/local/bin/1m-cost-metrics.sh") | crontab -u $cfn_cluster_user -
(crontab -l -u $cfn_cluster_user; echo "*/60 * * * * /usr/local/bin/1h-cost-metrics.sh") | crontab -u $cfn_cluster_user - 


# replace tokens 
sed -i "s/_S3_BUCKET_/${s3_bucket}/g"                   /home/$cfn_cluster_user/grafana/dashboards/ParallelCluster.json
sed -i "s/__INSTANCE_ID__/${master_instance_id}/g"      /home/$cfn_cluster_user/grafana/dashboards/ParallelCluster.json 
sed -i "s/__FSX_ID__/${cfn_fsx_fs_id}/g"                /home/$cfn_cluster_user/grafana/dashboards/ParallelCluster.json
sed -i "s/__AWS_REGION__/${cfn_region}/g"               /home/$cfn_cluster_user/grafana/dashboards/ParallelCluster.json 

sed -i "s/__AWS_REGION__/${cfn_region}/g"           /home/$cfn_cluster_user/grafana/dashboards/logs.json 

sed -i "s/__Application__/${stack_name}/g"          /home/$cfn_cluster_user/prometheus.yml 

sed -i "s/__INSTANCE_ID__/${master_instance_id}/g"  /home/$cfn_cluster_user/grafana/dashboards/master-node-details.json

sed -i "s/__INSTANCE_ID__/${master_instance_id}/g"  /home/$cfn_cluster_user/grafana/dashboards/compute-node-list.json 
sed -i "s/__INSTANCE_ID__/${master_instance_id}/g"  /home/$cfn_cluster_user/grafana/dashboards/compute-node-details.json 

#docker pull prom/pushgateway
docker run --name pushgateway --net host -d --restart=unless-stopped -p 9091:9091 \
    prom/pushgateway

# Run Prometheus
docker run --name prometheus --net host -d --restart=unless-stopped -p 9090:9090 \
    -v /home/$cfn_cluster_user/prometheus.yml:/etc/prometheus/prometheus.yml \
    -v prometheus-data:/prometheus \
    prom/prometheus \
         --config.file=/etc/prometheus/prometheus.yml \
         --storage.tsdb.path=/prometheus \
         --web.console.libraries=/usr/share/prometheus/console_libraries \
         --web.console.templates=/usr/share/prometheus/consoles \
         --web.external-url=/prometheus/ \
         --web.route-prefix=/

# Run Grafana
docker run --name grafana --net host -d --restart=unless-stopped -p 3000:3000 \
    -e GF_SECURITY_ADMIN_PASSWORD=Grafana4PC! \
    -e GF_SERVER_ROOT_URL="http://%(domain)s/grafana/" \
    -v /home/$cfn_cluster_user/grafana:/etc/grafana/provisioning \
    -v grafana-data:/var/lib/grafana \
    grafana/grafana


#Generate selfsigned certificate for Nginx over ssl
mkdir /home/$cfn_cluster_user/ssl
openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 -subj "/C=US/ST=WA/L=Seattle/O=AWS/CN=ngnix" -keyout /home/$cfn_cluster_user/ssl/nginx.key -out /home/$cfn_cluster_user/ssl/nginx.crt 
chown -R $cfn_cluster_user:$cfn_cluster_user /home/$cfn_cluster_user/

# Run Nginx
docker run  --name nginx --net host -d -p 443:443 --restart=unless-stopped \
    -v /home/$cfn_cluster_user/nginx/conf.d:/etc/nginx/conf.d/ \
    -v /home/$cfn_cluster_user/ssl:/etc/ssl/ \
    -v /home/$cfn_cluster_user/www:/usr/share/nginx/html \
    nginx


git clone https://github.com/vpenso/prometheus-slurm-exporter.git
cd prometheus-slurm-exporter
GOPATH=/root/go-modules-cache HOME=/root go mod download
GOPATH=/root/go-modules-cache HOME=/root go build
cp /tmp/prometheus-slurm-exporter/prometheus-slurm-exporter /usr/bin/prometheus-slurm-exporter

bash -c "cat << EOF > /etc/systemd/system/slurm_exporter.service
[Unit]
Description=Prometheus SLURM Exporter

[Service]
Environment=PATH=/opt/slurm/bin:$PATH
ExecStart=/usr/bin/prometheus-slurm-exporter
Restart=on-failure
RestartSec=15
Type=simple


[Install]
WantedBy=multi-user.target
EOF"

systemctl daemon-reload
systemctl enable slurm_exporter
systemctl start slurm_exporter


;;
ComputeFleet)



;;
esac


#########################################################################################################################
# The node_exporter is designed to monitor the host system. 
# It's not recommended to deploy it as a Docker container because it requires access to the host system. 
# Be aware that any non-root mount points you want to monitor will need to be bind-mounted into the container.
# If you start container for host monitoring, specify path.rootfs argument. 
# This argument must match path in bind-mount of host root. 
# The node_exporter will use path.rootfs as prefix to access host filesystem.
#########################################################################################################################
mkdir -p /home/$cfn_cluster_user/node_exporter
wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz
tar -xvzf node_exporter-1.0.1.linux-amd64.tar.gz
mv node_exporter-1.0.1.linux-amd64/node_exporter /home/$cfn_cluster_user/node_exporter/
chmod +x /home/$cfn_cluster_user/node_exporter/node_exporter

# set node exporter as a service
bash -c "cat << EOF > /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target
[Service]
Type=simple
Restart=on-failure
SyslogIdentifier=node_exporter
ExecStart=/home/$cfn_cluster_user/node_exporter/node_exporter
[Install]
WantedBy=multi-user.target
EOF"

# then run the daemon
systemctl daemon-reload
systemctl enable node_exporter
systemctl start node_exporter