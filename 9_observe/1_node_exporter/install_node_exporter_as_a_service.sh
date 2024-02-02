#! /bin/bash


sudo cp ~/ne/node_exporter-1.6.1.linux-amd64/node_exporter /usr/local/bin/


sudo useradd -rs /bin/false node_exporter


sudo tee /etc/systemd/system/node_exporter.service<<EOF
[Unit]
Description=Node Exporter
After=network.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
EOF


sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter


sudo systemctl status node_exporter

curl http://localhost:9100/metrics
