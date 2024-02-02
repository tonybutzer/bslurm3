# Stage 5: Testing and Documentation.
    Stage 0: Feasibility and Concept Development
    Stage 1: Project Planning. The first stage of SDLC is all about “What do we want?” ...
    Stage 2: Gathering Requirements & Analysis. ...
    Stage 3: Design and Documentation. ...
    Stage 4: Coding or Implementation. ...
    Stage 5: Testing and Documentation. ...
    Stage 6: Deployment. ...
    Stage 7: Maintenance.

## SCience Workload Alpha Tesing

### Pat Danielson Dynamic Surface Water Extent

Pat Danielson wants to alpha test 

- i told him we can dedicate the Nov4 sprint to him

- https://www.usgs.gov/landsat-missions/landsat-collection-2-level-3-dynamic-surface-water-extent-science-product

 

- that is the model we will be running 
- starting with a single ARD tile 
- and testing various gridding and compute combinations

> there are several questions we want to answer and use some of the baselining tools I have developed for my animation prototype.
- this is straight forward: but will require focused work 
- the lessons learned will be valuable for future workloads.
- i don't know how long 
- but likely at least two weeks to get a good test done with resource data for compute, memory and tile size.

#### WBS
1. Get code ready to work on single ARD Tile - Pat
2. DEmonstrate this via slurm/sbatch - and play with c N n 

```bash
#!/bin/sh

# We assume running this from the script directory
job_directory=$PWD/.job
#data_dir="${SCRATCH}/project/LizardLips"

lizards=("14_05_2022" "14_06_2022" "15_05_2022" "15_06_2022")

for lizard in ${lizards[@]}; do

    job_file="${job_directory}/${lizard}.job"

    echo "#!/bin/bash
#SBATCH --account=impd
#SBATCH --time=00:20:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=butzer@contractor.usgs.gov
#SBATCH --job-name=${lizard}.job
#SBATCH --output=.out/${lizard}.out
#SBATCH --error=.out/${lizard}.err
source /home/butzer/miniconda3/bin/activate nlcd2
python3 anim.py ${lizard}" > $job_file
    sbatch $job_file

done
```

```
(nlcd2) ec2-user@ip-172-16-60-64 ~/tony/opt/bslurm/1_HPC/0_app$ cat v2_multi_tile_sbatch.sh
#!/bin/sh

# We assume running this from the script directory
job_directory=$PWD/.job
#data_dir="${SCRATCH}/project/LizardLips"

lizards=("14_05_2022" "14_06_2022" "15_05_2022" "15_06_2022")

yr=2022
for h in {15..20}; do
        for vt in {8..13} ; do
                v=$(echo $vt | awk '{printf("%02d", $1)}')
                lizard=${h}_${v}_$yr

#for lizard in ${lizards[@]}; do

    job_file="${job_directory}/${lizard}.job"

    echo "#!/bin/bash
#SBATCH --account=butzer
#SBATCH --time=00:20:00
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=butzer@contractor.usgs.gov
#SBATCH --job-name=${lizard}.job
#SBATCH --output=.out/${lizard}.out
#SBATCH --error=.out/${lizard}.err
source /home/ec2-user/tony/source_conda.src
## source /home/butzer/miniconda3/bin/activate nlcd2
python3 anim.py ${lizard}" > $job_file
    sbatch $job_file

        done
done
```
