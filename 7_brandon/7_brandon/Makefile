cat:
	cat Makefile

bbb:
	pcluster create-cluster --cluster-name bbb2-cluster --cluster-configuration bbb.yaml

abc:
	pcluster create-cluster --cluster-name abc-cluster --cluster-configuration abc.yaml

gen:
	pcluster create-cluster --cluster-name wsmonkey-cluster --cluster-configuration wsmonkey-cluster.yaml
	#pcluster create-cluster --cluster-name ws-cluster --cluster-configuration tony-cluster-config.yaml
	# pcluster configure --config tony-config-file.yaml

ungen: 
	pcluster delete-cluster --cluster-name monkey-cluster

stop-the-fleet:
	pcluster update-compute-fleet --cluster-name nlcd-pcluster --status STOP_REQUESTED
update:
	pcluster update-cluster --cluster-name nlcd-pcluster --cluster-config ./cluster.yaml --region us-west-2



list:
	pcluster list-clusters

bami:
	pcluster build-image --image-id nlcd-pcluster-v3-ami --image-configuration bi.yaml --region us-west-2
