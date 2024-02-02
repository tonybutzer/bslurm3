# Parallel Cluster Demo

# tldr; - Is the Parallel Cluster feasible and applicable for LCNext? `YES!`

![still here](https://media4.giphy.com/media/3FA2atHHZaOZi/200w.gif?cid=6c09b9526cp1t4offlvc4ntxukwgaxem1y7j8gs12j9jcjsg&ep=v1_gifs_search&rid=200w.gif&ct=g)

# Elevator Pitch

- Computers out of thin air
- Experienced Powerful Orchestration
- Elastic Compute
- Infinite Reliable Storage
- Synergies with Cray Supercomputers
- A pangeo trained python science force

# Genius!
` Genius`
**amazing**


> lets save the planet now - then drink wine tonight!

> a one to one comparison between HPC and Cloud Parallel Cluster - is reductive in both directions.

> the cloud is waiting/begging to accelerate science

# Plans
- wait for the team to get formed with critical mass
- `test parallel cluster with Watersmart Production`
- trade study of 3 scaling methods
    - `Parallel Cluster`
    - gitlab scheduler
    - AWS Batch
- eliminated from the trade study
    - kubernetes
    - dask
    - mpi
    - home grown docker orchestration
    - docker swarm
    - ARGO
    - Airflow
    - Nifi
    - dask again!
    - the next two are totally unrelated - just want to hate on em a bit:
        - SuperSet 
        - NGINX Traefic
- custom aws cost prometheous exporter - in Python
- automated Compute node IP and dynamic prometheous
- Implement a SARF like system to manage my time

# Progress
- set up 3 parallel clusters
    - Thanks Brandon Schulz for setting up the first one.
- wrote code for resource profiling
- wrote code to represent a minimal ARD case
    - ARD Tile Animator
    - Top 100 most populated cities - Sentinel-2 Animations
        - I like Sentinel way more than Landsat.
            - request-payer bugs = will never end and will hinder science
- stress tested the small cluster
- got prometheus and grafana to work
    - exporter for node, cluster and docker(soon)
    - dash boards for node cluster and docker(soon)
- IAC progress
    - initial terraform snippets for ec2 - security groups - basically all resources needed

# Problems
- Slurm prometheus exporter is written in GO
- prometheus has its own query language so in order
    - I love pandas
    - I tolerate SQL
    - I am confused by promQL
- AWS Cost models even just for ec2 - are ridiculous - pandas to the rescue
- AWS throws an error - Guy walks into a bar.
- AwS throws and error - availability of a particular node - C6i queue only and have noticed it in immature clusters, spot instances AMD processors - etc etc - 
- Active Directory still needs careful study
    - start with ROOT - DONE
    - test a single dumb user - dopey@10.12.70.70
- AWS security groups can take time to refine
    - if that is the case then Roles - Permissions - Rules/Policies takes time times ten

## GANTT CHART - Rough order of Magnitude

> Because exact deadlines don't take into account the uncertainties and challenges that may arise during the process, they are often counterproductive. Leaders who are deadline-focused can create disappointment and disillusionment as the hard targets they set are frequently missed.

[GANTT CHART](https://tonybutzer.github.io/bslurm2/pc_gantt.html)

# Context Danny Howard

Some general content I'd like to squeeze in there --- 
stage-setting stuff: Cover environmental variables…. 
 
1. Where we stand as science organization.... 
    - Reliant on HPC / on prem systems; big investments and push to Cloud by leadership
    - BUT - Learning curve and challenges related to doing R&D in the cloud
    - AND - Unknown costs in that pay as you go model
2. Introduce Parallel Cluster Concept… alternate pathways to the cloud (lower barrier to entry)
3. Where LCNext is at w/ setting this up and leveraging this
    
    - What we’ve learned?
    - Where do we go from here?
    - Currently have: Protections against run-away jobs (Slurm / configurations)

# Costs

```
$ daily-ws-costs
['awsprice.py', '']

      state                name            ip       i_type  monthly_cost
0   running     ws-costanalyzer  10.12.65.189     t3.small        15.184
1   stopped       ws-butzer-dev  10.12.65.180  t3a.2xlarge       219.584
2   stopped     ws-gparrish-dev  10.12.65.226  m6i.2xlarge       280.320
3   stopped      ws-pc-adminbox   10.12.65.33   t3a.medium        27.448
4   stopped     ws-ami-examiner  10.12.67.113   t3a.medium        27.448
5   stopped            ws-ami-2  10.12.67.199   t3a.medium        27.448
6   stopped      ws-ldap-tester  10.12.64.214   t3a.medium        27.448
7   stopped        ws-data-xfer  10.12.64.158   t3a.xlarge       109.792
8   stopped  ws-machinelearning  10.12.66.139  t3a.2xlarge       219.584
9   stopped      ws-ssebop-prod   10.12.66.40   m5.8xlarge      1121.280
10  stopped        ws-veget-dev  10.12.67.239  m6i.2xlarge       280.320
11  stopped          ws-kul-dev  10.12.64.123  r6a.2xlarge       331.128
12  stopped            HeadNode  10.12.64.196    t3.medium        30.368
==========================================================================================
==========================================================================================
     state             name            ip    i_type  monthly_cost
0  running  ws-costanalyzer  10.12.65.189  t3.small        15.184
========================================================================================================================
========================================================================================================================
['awsprice.py', '']

     state            name            ip       i_type  monthly_cost
0  stopped      mhasan-dev   10.12.71.39    t3a.large        54.896
1  running      butzer-dev    10.12.71.5  t3a.2xlarge       219.584
2  stopped  kruslander-dev  10.12.71.114    t3a.large        54.896
3  stopped      mlubke-dev  10.12.70.140    t3a.large        54.896
4  stopped      ashish-dev   10.12.70.88   r5a.xlarge       164.980
5  stopped    asampath-dev  10.12.70.199  t3a.2xlarge       219.584
==========================================================================================
==========================================================================================
     state        name          ip       i_type  monthly_cost
1  running  butzer-dev  10.12.71.5  t3a.2xlarge       219.584
========================================================================================================================
========================================================================================================================
```

###  butzer-dev  10.12.71.5  t3a.2xlarge       $219.584/month
- 8 cpus
- 32 gig memory
- 8 Exabytes of Disk
- Infinite s3 storage at 3 cents per gig

---

###    HeadNode  10.12.64.196    t3.medium        $30.368/month

### ws-gparrish-dev  10.12.65.226  m6i.2xlarge       $280.320/month
- 8 cpus
- 32 gig memory
- 60 bucks more - why
- intel verus amd is a factor 


# Disclaimers
- this is an very early prototype cluster demo
- this is a PATHFINDER PROTOTYPE
- the parallel cluster expert is finding his way back to the project
- this demo is scoped for a specific science project and works well there 
    - this is no guarantee that other workloads will work as expected in this type of cluster
- this demo was specifically scaled back to be in-expensive - more work on cost containment is needed
- that said we could do all of watersmart processing with this small 3 node cluster and it will be cost effective with simple cost guardrails and automatically shut down when not in use
- I want to improve Cost Containment, Observability, Customization, Instance Selection, Queue Optimization - basically do some robust engineering before turning it over

## Engineering Research Scope - Responsibilities

1. Technology Capability Research - not production grade
2. Solve Problems for:
    - Observability
    - baseline conda environment and possible solutions for conda env
        - per application
        - containers likely the best solution
    - cost estimator for ec2 - ballpark
        - detailed cost analysis outside this scope

## Production DevOps Items

1. Multiple users permissions
2. Cost Accounting
3. 

## Scientist Teams Responsibilities

1. Choosing between the cluster and other options
2. Best practices python development
3. Technology Debt collecting
4. Ready to run apps - simplification - containers

## PC Benefits

## Easier than most scale out technologies
- Same scaling language as HPCs:  Tallgrass, Denali, Hovenweep
- Very little scaffolding compared to Kubernetes
- Very Flexible on how many nodes and what size
- Cost containment and cost planning can easily be accomplished
    - with Developer and Cluster Admins working side by side.

> **DevOps** is a combination of software development (dev) and operations (ops). It is defined as a software engineering methodology which aims to integrate the work of development teams and operations teams by facilitating a culture of collaboration and shared responsibility.

## SLURM
SLURM is a queue management system and stands for i
- Simple 
- Linux 
- Utility for 
- Resource (CPU, MEMORY) Management.

## SLURM Benefits
- Slurm Benefits:

    Highly scalable and configurable.
    Optimized resource allocations for network topology and on-node topology.
    Sophisticated multifactor job prioritization algorithms.
    Real-time accounting down to the task level (identify specific tasks with high CPU or memory usage)

- Slurm may be the most widely accepted framework for AI applications, both in enterprise and academic use,
- HPC and the cloud look the same for orchestration

[slurm testimonials](https://slurm.schedmd.com/testimonials.html)

- **Slurm Overview:**
  - Slurm is an open-source cluster management and job scheduling system designed for Linux clusters, catering to both large and small setups.
  - It boasts fault-tolerance and high scalability, without requiring kernel modifications for operation.

- **Key Functions:**
  - **Resource Allocation:**
    - Slurm allocates exclusive and/or non-exclusive access to compute nodes for users, allowing them to perform work for a specified duration.

  - **Work Execution Framework:**
    - It provides a framework for initiating, executing, and monitoring work, typically parallel jobs, on the allocated set of nodes.

  - **Contending Resource Arbitration:**
    - Slurm manages a queue of pending work to arbitrate contention for resources, ensuring a smooth and organized workflow.

- **Optional Features and Plugins:**
  - **Accounting:**
    - Optional plugins can be employed for accounting purposes, tracking resource usage and job statistics.

  - **Advanced Reservation:**
    - Slurm supports advanced reservation of resources, allowing users to plan and reserve resources for future work.

  - **Backfill Scheduling:**
    - Slurm supports backfill scheduling, optimizing resource utilization by filling gaps in the schedule with suitable jobs.

  - **Topology Optimized Resource Selection:**
    - The system enables the selection of resources based on the cluster's topology, optimizing performance.

  - **Resource Limits and Prioritization:**
    - Optional plugins allow setting resource limits by user or bank account, and Slurm employs sophisticated multifactor job prioritization algorithms.

- **Self-Containment:**
  - Slurm is relatively self-contained, contributing to its operational simplicity and ease of integration with existing systems.



# The Demo

![cluster_create](https://github.com/tonybutzer/assets/blob/master/0_cluster/parallel_cluster_concept_to_real.JPG?raw=true)


## Creating the Creator ws-pc-admin-box

#### Terraform Variables

```
variable "region" {
  description = "The AWS region."
  default = "us-west-2"
}

variable "ship_instance_type" {
  description = "ships - The instance type."
  # default = "c5.9xlarge"
  default = "t3a.medium"
}

variable "subnet_id" {
  description = "The AWS network id representing the allowed vpc"
  default = "subnet-08f1118dd59133513"
}

variable "ship_userdata" {
  description = "user data os startup scripts"
  default = ["ship0.sh", "ship1.sh"]
}

variable "ship_name" {
  description = "ship names - DUH!"
  default = ["ws-pc-adminbox", "ws-gen-test-sship-1"]
}

variable "key_name" {
  description = "The AWS key pair to use for resources."
  default = "butzer@IGSKMNCNLT01529"
}

variable "ami" {
  description = "watersmart-developer"
  default = "ami-0258c61d5a80b6572"
}

variable "security_group_ssh" {
  description = "The AWS security group (privateinstancesSSH-sg)"
  # the bastion holds usgs vpn and eros class b addresses..
  default = "sg-067d5d0cb608f6af9"
}

variable "iam_role" {
  description = "The AWS iam role - limited access on these ec2s"
  default = "butzer-devops-profile"
}

```

## The Cluster itself is Created from pure yaml - COOL!

```
(aws-parallel-cluster) [ec2-user@ip-10-12-65-33 8a_ws_pcluster_admin]$ cat bbb.yaml
Region: us-west-2
CustomS3Bucket: dev-ws-parallelcluster-testbucket
Image:
  Os: alinux2
  CustomAmi: ami-067d504ae48dd3252
HeadNode:
  InstanceType: t3.medium
  Networking:
    SubnetId: subnet-08f1118dd59133513
    SecurityGroups:
      - sg-06842c1ea45eb2039
  Ssh:
    KeyName: ws-pcluster-keypair
  Iam:
    AdditionalIamPolicies:
      - Policy: arn:aws:iam::427491229895:policy/developer-policy
      - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
    S3Access:
      - BucketName: ws-out
Scheduling:
  Scheduler: slurm
  SlurmSettings:
    Dns:
      DisableManagedDns: true
      UseEc2Hostnames: true
  SlurmQueues:
  - Name: eco
    ComputeResources:
    - Name: t3a2x
      Instances:
      - InstanceType: t3a.2xlarge
      MinCount: 0
      MaxCount: 3
    Networking:
      SubnetIds:
      - subnet-08f1118dd59133513
      SecurityGroups:
        - sg-06842c1ea45eb2039
    Image:
      CustomAmi: ami-058297c4b7911f4e4
    Iam:
      AdditionalIamPolicies:
        - Policy: arn:aws:iam::427491229895:policy/developer-policy
        - Policy: arn:aws:iam::aws:policy/AmazonS3FullAccess
      S3Access:
        - BucketName: ws-out
Iam:
  PermissionsBoundary: arn:aws:iam::427491229895:policy/csr-Developer-Permissions-Boundary
SharedStorage:
  - MountDir: /wspcefs
    Name: wspcefs
    StorageType: Efs
    EfsSettings:
      Encrypted: false
      DeletionPolicy: Delete
```

1. start the headnode water smart
2. run ardanim/1_HPC/0_app/  ./bbb_v3......

3. watch -n 10 squeue
4. look at the Compute Nodes coming up
5. look at /wpcefs/opt/tony ... ls -l
6. look at .out logfiles

```
[ec2-user@ip-10-12-64-196 .out]$ pwd
/home/ec2-user/tony/ardanim/1_HPC/0_app/.out
[ec2-user@ip-10-12-64-196 .out]$ tail 20_13_2022.out
/wspcefs/opt/tony/browse_20_13/LC08_CU_020013_20220704_20220711_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC09_CU_020013_20221115_20230325_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC09_CU_020013_20220117_20230504_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC09_CU_020013_20220930_20230330_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC08_CU_020013_20220305_20220318_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC09_CU_020013_20220516_20230420_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC08_CU_020013_20221109_20221125_02_thumb_large.jpeg
/wspcefs/opt/tony/browse_20_13/LC09_CU_020013_20220218_20230430_02_thumb_large.jpeg
Building the animation ...
SUCCESS /wspcefs/opt/tony/animations/2022_20_13.gif created!
```


![email](https://github.com/tonybutzer/assets/blob/master/0_cluster/email_from_slurm.JPG?raw=true)

![detail](https://github.com/tonybutzer/assets/blob/master/0_cluster/email_time..JPG?raw=true)


## Shut'er Down

![shutdown](https://github.com/tonybutzer/assets/blob/master/0_cluster/compute_terminated.JPG?raw=true)


## Demo Again with Instruments

![instruments](https://media.tenor.com/iIKNUVgwi8kAAAAC/airplane-movies.gif)


## Prometheus

## Grafana

## What Have we Learned
- parallel clusters `rock` and will be an instrumental tool for science products
    - especially ARD tile time-series applications
- Monthly Patch Day - will create work for Parallel Cluster Managers and small aggravations for users.
    - building AMIs for the cluster is one of the slower things we do - and initially quite painful.
- You can get a Boatload of work done with cheap ec2 computers 
- not all work will be in cheap in the cloud - Vigilance and Diligence.
    - GPUS in the cloud hands-off for now - don't weep cause Hovenweep
    - pyCCD looks expensive wherever you run it.
- Its nice to have a mature scheduler like SLURM to manage resources
    - especially when it turns of the lights and contains costs automagically
- "Docker containers and gratitude share a common trait - they both possess superpowers." - Tony Butzer

## the stac browser 

- https://landsatlook.usgs.gov/stac-browser/collection02/DSWE/1991/CU/004/004/LT05_CU_004004_19910319_20210423_02_DSWE
- [browse away](https://landsatlook.usgs.gov/stac-browser/collection02/DSWE/1991/CU/004/004/LT05_CU_004004_19910319_20210423_02_DSWE)
- these data first ARD data FIRST
- this software has a nice look

![USGS STAC BROWSER](https://github.com/tonybutzer/assets/blob/master/0_cluster/stack_browser_noice.JPG?raw=true)
- 


# Whats Next?

- Test run Pat Danielsons - ARD Science Product Flows in an optimized cluster
- Refine Cluster - betterFasterCheaper - spot instances - resource groups - mitigate instance availability issues
- Hire a coder - make her malleable - Princess Malleable
    - reduce current technology debt
    - minimize future technology debt
    - develop a set of reusable python 2nd level libraries worth of the parallel cluster
<img src="https://github.com/tonybutzer/assets/blob/master/0_cluster/rico_lindsay.JPG?raw=true" alt="clone" title="Clone Rico Title" width="40%"/>
-- Clone Rylie!


---

#### more

- Disrupt the IT Service model
    - should be better integrated with our team
    - Quality and responsiveness needs to improve to match the Speed of Cloud.
    - DevOps by definition is a tightly coupled partnership
- Improve Training for everyone.
- Develop a Path to the Cluster
    - tested code
    - cluster appropriate test gate
    - bench mark and profile - compute and memory requirement analysis
    - instance type and number from the newTBD pcluster_resource_wizard
    - test one ARD or one scalable unit (one year, one tile)
    - storage strategy
- Determine mitigations for python conda hell

# Whats Next at High Level?

[GANTT CHART](https://tonybutzer.github.io/bslurm2/pc_gantt.html)


## Deep Dive on Cluster Tech Things

### A look deeper at only one thing --> Observability

    - docker dashboard (prometheus/grafana)
    - cost taxi cab meter (tbd)
    - log managment and analysis
    - alerting
    - pipeline health instrumentation - and retrys - like gitlab-runners.
    - a second look at elastic and kibana for some of these items
    - application observability - openTelemtry and Xray
    - https://superuser.com/questions/1330824/how-to-stop-tmux-from-launching-login-shells
    - "Who invented liquid soap and why?" - The Sure Thing


[observe monitor](https://last9.io/blog/observability-vs-telemetry-vs-monitoring/)

---

- Perfectionism is a refusal to accept any standard short of perfection.

- Idealism is the practice of pursuing ideals, even if they are unrealistic.

- Perfectionism is about rejection.

- Idealism is about practice.

# No
# Yes - but we will charge you and move the schedule to the right.
