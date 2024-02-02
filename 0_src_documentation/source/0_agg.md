# Planning for the Prototype Parallel Cluster

## GANTT CHART
[GANTT CHART](https://tonybutzer.github.io/bslurm2/pc_gantt.html)

- gantt chart here
![gantt](https://github.com/tonybutzer/bslurm2/blob/main/1_gantt/pc_gantt.png?raw=true)

---

- code name uberBrandon
- code name chaosMonkey - terraform creation IaC

# Current Week Ending 10/27/2023
- very busy - too busy

## terraform/terragrunt gitlab-runners

- setup gilab-runner on ws-ldap-test and practice connecting to eroslab
    - turn off enterprise runners in tfiac repo
- build initial tf scripts for AWS Resources
    - ws-pc-keypair
    - ws-pc-adminbox
- start with pure terraform and look at terragrunt - not likely anytime soon


## Allowing Pat and Kory on the Cluster - It takes a village
- action brandon schulz
#### Kelcy's Roadmap

Initial Tasks:

- Parallel Cluster access for Pat ©
- Parallel Cluster access for Kory ©
    - Stand up development EC-2 instance
- `Derive maximum water extent for one year for tile h16v05`
        - Derive earliest date pixel was called water for one year for test tile h16v05
        - Derive latest date pixel was called water for one year for test tile h16v05
        - Derive percentage pixel was called water for one year for test tile h16v05
        - Build complete annual product suite 1985-2023 for test tile
- Build job array orchestration for a list of tiles
- Produce annual (1985-2023) products for CONUS
    - Produce annual (1985-2023) product mosaics for CONUS
    - Deliver final product mosaics to Ceph

Outside Scope
    Enable user environment OpenMPI # Tony has no experience with OpenMPI - so he won't help here. ©
    Access C2 L3 DSWE data products on S3

 
# Current Week Ending October 27, 2023
## chaosMonkey 4 node parallel cluster in watersmart IAC

**Steps one per day**

    Set up GitLab project repository
    Create the Terraform configuration files
    Set up pipelines using .gitlab-ci.yml file
    Set up AWS Credentials in Gitlab
    Set up the remote backend for Terraform on Gitlab
    Configure the backend in the provider block for local development
    Implement conditions to enable destroy operation using pipeline

- Create cluster Config and Deploy

- btw LDAP Sucks even more than Postgres
    - databases will always suck - thanks Larry Elison.


# Current Sprint 
- Ending November 3, 2023 
- weekly status

## Analysis Focus

1. Develop LDAP Skills
2. Trade Study on M$ Active Directory vs. Pure LDAP
    - these user management platforms are potential rabbit holes - there be dragons
    - LDAP - likely the MVP (minimal viable product) - ssh keys will be used in production
    - M$ ActiveDirectory Enterprise to be used in Deployment Phase
    - to explore pythin-ldap for management of users and passwords - perhaps next sprint
3. Integration - connecting LDAP to parallel cluster from startup yaml file 
    - Goal is to support user, password initiation for cluster access
    - Instead of hard-coded sh keys - we can certainly use this for alpha testers - to be scheduled in a sprint
    - first planned science user test is Tonian's Composite Parallel Slurm Test - depending on when the code is ready
4. Terraform analysis and CICD pipeline for SDLC Deployment Phase - chaosMonkey

--- 
## Planning Focus
1. Writing Project Plan with SDLC Phases
    - strategy is to use this meeting time for internal planning blocks until our project matures or gels
2. Developing the project plan - draft to be published November 3.


### SDLC Phase Summary

    Stage 0: Feasibility and Concept Development
    Stage 1: Project Planning. The first stage of SDLC is all about “What do we want?” ...
    Stage 2: Gathering Requirements & Analysis. ...
    Stage 3: Design and Documentation. ...
    Stage 4: Coding or Implementation. ...
    Stage 5: Testing and Documentation. ...
    Stage 6: Deployment. ...
    Stage 7: Maintenance.


## User Story

> scientist walks into a website, types a username and password and runs a slurm, sbatch job ported from Tallgrass.

- minimal effort is needed to move from Tallgrass
- alpha test is ARD animations - Butzer
- **WE WILL BE USING SIMPLE SSH KEYS FOR THE FIRST 2 maybe 3 BETA TESTS**
    - LDAP and AD is the juice worth the squeeze?
- beta test 1 NOVEMBER - dynamic-surface-water-extent-science-product - Pat Danielson
	- https://www.usgs.gov/landsat-missions/landsat-collection-2-level-3-dynamic-surface-water-extent-science-product
![](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/styles/info_block/public/media/images/L8_CU_021010_20210412__02_DSWE_Wabash_OH.jpg?itok=_rNv8YYS)
- beta test 2 in ARD composites - Tonian Robinson

