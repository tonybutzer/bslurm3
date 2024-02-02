# Stage 6: Deployment.
    Stage 0: Feasibility and Concept Development
    Stage 1: Project Planning. The first stage of SDLC is all about “What do we want?” ...
    Stage 2: Gathering Requirements & Analysis. ...
    Stage 3: Design and Documentation. ...
    Stage 4: Coding or Implementation. ...
    Stage 5: Testing and Documentation. ...
    Stage 6: Deployment. ...
    Stage 7: Maintenance.

# Manual Deployment Steps for uberBrandon

## HELP ME

```

Setting up an AWS ParallelCluster

Prior to running any pcluster create commands, we have to get some things in place in the account
because CHS doesn't let us do them under the covers via pcluster.

1.  Create an S3 bucket the cluster will use to store its configuration.
    See dev-nlcd-parallelcluster-testbucket in the nlcd account for example.

2.  We have to use AMI images we build with the nodes.  CHS doesn't allow us the use the amazon
    default images.  Dan Sherman created some Terraform/Ansible stuff to build these images each
    month and they're basically just the amazon default images re-wrapped.

3.  We have to use the ephemeral VPC and subnets for the cluster nodes because there aren't enough
    IP addresses in the developer subnets.  The access host needs access to those.

4.  Security group for the nodes.  CHS doesn't let pcluster create these under the covers, so you
    have to create one - should do this in Terraform.  See sg-00e85d664a5bcd8bb in the nlcd account
    for example.

5.  Since we want the EFS filesystem to persist beyond the lifetime of the cluster, you should create
    that from Terraform prior to creating the cluster.

6.  You need to specify the PermissionsBoundary in the cluster.yaml in order for a lot of the things
    that get created under the covers to work.  This is the one I was told to use:
    arn:aws:iam::081515586180:policy/csr-Developer-Permissions-Boundary


On access host
---------------
Have to fix up the urllib3 libs:
python3 -m pip uninstall urllib3
python3 -m pip install urllib3==1.26.15

Install aws ParallelCluster python packages:
python3 -m pip install "aws-parallelcluster" --upgrade --user

Install Node.js - see the AWS Parallel Cluster documentation for the correct version:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
chmod ug+x ~/.nvm/nvm.sh
source ~/.nvm/nvm.sh
nvm install --lts=Gallium
node --version
pcluster version

List clusters that already exist:
pcluster list-clusters -r us-west-2

Describe a cluster:
pcluster describe-cluster --cluster-name bwstestcluster -r us-west-2

Create a cluster:
pcluster create-cluster --cluster-name bwstestcluster --cluster-configuration cluster.yaml -r us-west-2

Before you can do anything on the cluster, you have to modify the <clustername>-RoleHeadNode-XXXXX IAM Role on the head node.
Find the Action section for RunInstance and CreateFleet and replace them with this:
        {
            "Action": [
                "ec2:RunInstances"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Sid": "EC2RunInstances"
        },
        {
            "Action": [
                "ec2:CreateFleet"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Sid": "EC2CreateFleet"
        },


To delete a cluster:
pcluster delete-cluster -r us-west-2 -n bwstestcluster

Connect to the cluster head node:
pcluster ssh -r us-west-2 -n bwstestcluster -i bschulz-keypair-nlcd.pem


Running a test job

Create a simple script:
#!/bin/bash
sleep 30
echo "Hello World from $(hostname)"

Check the cluster status:
sinfo

Submit a job to SLURM:
sbatch hellojob.sh

Check the queue status:
squeue


Installing dependencies for test script:
sudo yum install python3-devel
sudo yum install gdal gdal-devel
sudo yum install numpy

export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

python3 -m pip install numpy
python3 -m pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')
python3 -m pip install tqdm
python3 -m pip install mpi4py

We will need to put the following into the custom AMI so we don't need to run this bootstrap every time.  Note from Kelcy - we should source the
environment from the shared FS, perhaps install conda in the custom AMI and use the mechanism they use on the HPS to source that.
Put this into bootstrap.sh and copy to S3 bucket we can get to (aws s3 cp bootstrap.sh s3://dev-nlcd-developer/test_mpi/):
#!/bin/bash
echo "Installing dependency packages"

yum -y install python3-devel gdal gdal-devel numpy

export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
export PATH=/opt/amazon/openmpi/bin/:$PATH

sudo -u ec2-user python3 -m pip install --upgrade pip setuptools wheel
sudo -u ec2-user python3 -m pip install numpy
sudo -u ec2-user python3 -m pip install "setuptools<58.0"
sudo -u ec2-user --preserve-env=CPLUS_INCLUDE_PATH,C_INCLUDE_PATH python3 -m pip install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')
sudo -u ec2-user python3 -m pip install tqdm
sudo -u ec2-user env PATH=$PATH python3 -m pip install mpi4py




To run the test script - variables are hard-coded internally, parameters just to satisfy checking:
python3 rcmap_3index.py p01_r04 2015 leafoff ./data


To run on the cluster using MPI, create a submission script like this:
#!/bin/bash
#SBATCH --job-name=run-model-base-3-job
#SBATCH --ntasks=40
#SBATCH --output=%x_%j.out

mpirun -np 40 python3 rcmap_3index.py p01_r04 2015 leafoff /efs




NOTES:

To update the cluster:
pcluster update-compute-fleet --cluster-name bwstestcluster --status STOP_REQUESTED -r us-west-2
pcluster update-cluster --cluster-name bwstestcluster --cluster-configuration cluster-fsx.yaml -r us-west-2

```


# IaC Steps for chaosMonkey

## Manual choas

**services used**
https://docs.aws.amazon.com/parallelcluster/latest/ug/aws-services-v3.html


### Building with the CLI

https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-configuring.html




# Costs

## Estimating

## Monitoring
![grafana costs](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2020/11/10/Cluster-costs-1024x536.jpg)

- https://aws.amazon.com/blogs/compute/monitoring-dashboard-for-aws-parallelcluster/
