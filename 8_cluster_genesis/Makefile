cat:
	cat Makefile

down:
	wget https://us-east-1-aws-parallelcluster.s3.us-east-1.amazonaws.com/parallelcluster/3.6.1/installer/pcluster-installer-bundle-3.6.1.209-node-v16.19.0-Linux_x86_64-signed.zip
	mv pcluster-installer-bundle-3.6.1.209-node-v16.19.0-Linux_x86_64-signed.zip /tmp


down7:
	https://github.com/aws/aws-parallelcluster-cookbook/archive/refs/tags/v3.7.0:.zip
									

install:
	mkdir ~/pc
	(cd ~/pc; unzip /tmp/pcluster-installer-bundle-3.6.1.209-node-v16.19.0-Linux_x86_64-signed.zip)
	(cd ~/pc/pcluster-installer-bundle; chmod +x install_pcluster.sh)
	(cd ~/pc; bash install_pcluster.sh)

gen:
	pcluster create-cluster --cluster-name monkey-cluster --cluster-configuration monkey-cluster.yaml
	#pcluster create-cluster --cluster-name ws-cluster --cluster-configuration tony-cluster-config.yaml
	# pcluster configure --config tony-config-file.yaml

ungen: 
	pcluster delete-cluster --cluster-name monkey-cluster


list:
	pcluster list-clusters

publish:
	(cd ..; make publish)


node:
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
	chmod ug+x ~/.nvm/nvm.sh
	source ~/.nvm/nvm.sh

node2:
	#nvm install --lts
	echo nvm install 17
	node --version
