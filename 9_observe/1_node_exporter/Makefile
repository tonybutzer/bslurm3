cat:
	cat Makefile

# node exporter
ne:
	mkdir ~/ne
	(cd ~/ne; wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz)
	(cd ~/ne; tar xvzf node_exporter-1.6.1.linux-amd64.tar.gz)
	(cd ~/ne/node_exporter-1.6.1.linux-amd64; ./node_exporter)


tne:
	curl http://localhost:9100/metrics


node-service:
	./install_node_exporter_as_a_service.sh
