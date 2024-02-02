# Stage 9: Admin Guide

## Post Install Stuff

- https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-v3.html


- more to come

## Monitoring The Cluster with Prometheus and Grafana

### Monitor Cluster Level Dashboard

#### prometheus-slurm-exporter 

- https://github.com/vpenso/prometheus-slurm-exporter/

- https://grafana.com/grafana/dashboards/4323-slurm-dashboard/

- https://github.com/aws-samples/aws-parallelcluster-monitoring

---

- https://aws.amazon.com/blogs/compute/monitoring-dashboard-for-aws-parallelcluster/

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-PrometheusEC2.html

- https://sc20.hpcworkshops.com/10-monitoring/grafana/03-launch-pc.html

- interrogate grafana-post-install.sh


### Monitor Node Level Dashboad

- https://grafana.com/docs/grafana-cloud/send-data/metrics/metrics-prometheus/prometheus-config-examples/docker-compose-linux/

#### Node Exporter

- tutorial
    - https://www.youtube.com/watch?v=YUabB_7H710&t=585s
    - https://prometheus.io/docs/guides/node-exporter/

- as a systemctl service
    - https://docs.vmware.com/en/VMware-vRealize-Operations-Management-Pack-for-Kubernetes/1.8.1/management-pack-for-kubernetes/GUID-A1B68BE5-EF38-48E1-AA80-FD71E6F19989.html


- Repo
    - https://github.com/tonybutzer/observe/tree/main/prometheus-grafana

```
- job_name: node
  static_configs:
    - targets: ['10.12.66.172:9100']
```

- nice dashboard cheat
    - https://grafana.com/grafana/dashboards/13978-node-exporter-quickstart-and-dashboard/

#### Getting the Compute Node IP Addresses

- from decribe instance grep COMPUTE
- from parallel cluster CLI or python API ?


## MPI Considerations

- do we need mpi - it could cause issues - more to come

#### MPI Centos Installations:

```
export env MPICC=/usr/lib64/openmpi/bin/mpicc; pip3 install mpi4py


mpirun/mpiexec might be in 
/usr/lib64/openmpi/bin/
```
