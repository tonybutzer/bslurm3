# bslurm
benchmark slurm - conv repo

## WIP

- conda items
    - removing /opt/miniconda3
    - source conda env and document here

- IAM Roles, Security Groups, Permissions AWS oh-my
    - cluster nodes too restrictive
        - no s3 access
        - no describe instances

## Tests
    - run interactive shell on elastic compute node = DONE!
        - make salloc
        - make shell

    - run animation creator interactive - Pending s3 access
    - run animator sbatch 

### Work Arounds
    - manually change the IAM role to nlcd developer
        - check box compute --> Actions --> Security

### Git
    - using tokens and theBigGithub bslurm
