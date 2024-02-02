# Week 10 - We are Really on to Something Here:

---
![](http://ontheworldmap.com/usa/state/maine/map-of-maine.jpg)


---

### A lot to cover today

- Remember: - Tony does topical small sessions on specific topics as part of the Pangeo/Open Data Cube outreach project

---
---

---
[UTM Link svg](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system#/media/File:Universal_Transverse_Mercator_zones.svg)


### Tony yamls on 
- http://www.yamllint.com/
- https://jsonlint.com/

## Next 2 classes - Yaml
```
Today: '2-16-2021'
  Theme: 'Sentinel Data Exploration and Discovery'
  Title: 'Cloud Based Sentinel CogS'
  Sensor: 'Sentinel'
  Data_Tier: 'L2A'
  Projection: 'UTM'
  Science_Application: 'Compositing'
  Sandbox: 'pangeo.chs.usgs.gov'
  Status: 'Exploration early R&D'
  Purpose: 'Class Example'
  AWS_Document: 'https://registry.opendata.aws/sentinel-2-l2a-cogs/'
  AOI: 'Maine'
  City: 'Augusta'
  Subtopics: ['Browse', 'Tiles', 'Clouds', 'Geojson', 'Google_Maps']
  Git_Repo_Ref: 'https://github.com/tonybutzer/composite/tree/main/00-notebooks/00-wip-geojson-viewer'
```

---



---

## Everyone loves a Grid

---
![hls](./Assets/hls-grid-conus.PNG)

---

![a](https://dragon3.esa.int/documents/247904/266366/Sentinel-2-MSI_Product_Types_Figure_1_v3/262f604c-de1e-4cf7-b4f6-abdd7f0dc5fd?t=1523262257162)
https://earth-info.nga.mil/GandG/update/index.php?action=home#tab_coord-data

![](https://earth-info.nga.mil/GandG/update/img/MGRS_1km_Polygon_Shapefiles_Coverage.jpg)

https://www.usgs.gov/centers/eros/science/usgs-eros-archive-sentinel-2?qt-science_center_objects=0#qt-science_center_objects

- The Sentinel-2 tiling grid is referenced to the U.S. Military Grid Reference System (MGRS). 
- Tiles can be fully or `partially` covered by image data. 
    - Partially covered tiles correspond to those at the edge of the swath.


### Demo - klm - shapefiles - geoviews - maps

```
--- 
Notebook: 00-sentinel-klm-study
Purpose: "geometry vector intersection example"
AOI: "Maine and tiles"
Python_Packages: 
  - geopandas
  - shapely
  - feona
  
Sandbox: pangeo.chs.usgs.gov
User: butzer@contractor.usgs.gov
github: composite
path: opt/composite00-notebooks/00-wip-geojson-viewer
Opinion: "geoviews base * maine layers cool - zoom them"

COOL_FEATURES:
  - prune by geometric intesection operation with state of maine
  - save as geojson --> geojson.io
  - save as klm --> maps    https://www.google.com/maps/d/home
```

---
---
# Week 11

> "One of the advantages of doing science in general in the cloud is the potential to facilitate interagency collaboration in terms of people and data sets. That is a fundamental objective of new analysis environments coming on the scene, such as `PANGEO` and Open Data Cube. And because these are open source, they can operate on any cloud or on-prem platform. In late 2019, we (NLI, EROS, and CHS folks) began discussing these kinds of joint development opportunities with NASA and NOAA, which are continuing. That’s a pretty exciting prospect for EROS.” -- Pete Doucette 


## Class Recap

- I want to demystify the cloud.
    - i.e. -- cost for CONUS Evapo is $100
- I want to accelerate science to keep up with the earth and human challenges we face
    - Early results are quite promising - more to come ...
- I will be asking you folks lots of questions about the effectiveness of Jupyter and how to work with such a diverse group of folks.
- Should folks be trained on linux, python, jupyter, docker? – Can I help with that training?
    - In many cases people are already skilled here. 
    - Just need to increase the opportunities to exploit those skills on behalf of science
- Techniques to reduce Data Wrangling?


## What's Happening in Pangeo Land

- Kevin Costinett's team fixing some of the Collection-2 STAC rough spots
- Rich Signell has been working on improving the Pangeo
- We have a fledgeling DataLake in the dev-et-data - can access it from pangeo.cr.usgs.gov
    - Now that Kristi Kline is on the case we may get more attention on a USGS cloud S3 based Data Lake.
- LCMAP exploring AWS - they have an account and are playing with Xarray and Dask
- Discussion with Neal, Dev, Logan on HLS, docker, mini-pangeo python GDAL upgrade
- Steffi Kagone data validation tools - slicing xarrays as pixel drill time series
- compositing Maine with clouds using Sentinel data in the cloud and pangeo.chs.usgs.gov
    - deploying panel apps with usgs urls and docker - Rich Signell
    - AI - it may be the future for better land characterization - lets use the cloud for that as well
    - A quick look at the cloud buckets for ET and ECO
- Guest Speakers Dahal, Devendra (Contractor) and Megard, Logan J on HLS
    - Megard, Logan J on Logan's simple library of AWS Jupyter Examples - or how to really write tutorials.
        - even smaller bites with no assembly required - just git clone and run
    - Tony will do a short intro to github and https://code.usgs.gov - and how to use SSH KEYS!
- Evapotranspiration Demos coming next week
    - How to slice Xarray data in multiple ways


## Data Wrangling Working Group

## Data Lake Work

- Class A Data Assets
    - Landsat Collection-2
    - Sentinel Cogs
    - Harmonized Landsat Sentinel (1.5)

- Class B Data Assets
    - NLCD
    - LCMAP Products

- Class C Data Assets
    - Soil ...

- Collaborative data wangling pipelines and datalakes of key science input datasets will reduce the burden of portals
- AWS S3 > portals --- Google > Portals - Chris Holmes

- Tony to introduce the Data Wrangling Working Group DWWG Concept Only
        
- Team Members so far (Blue Sky)
    - Danielson, Patrick (Contractor) - NLCD wrangle chair
    - Megard, Logan J, Dahal, Devendra (Contractor) -- HLS1.5 cloud pipelines
    - Boiko, Olena - Soil Data and Climate Data
    - Tony  - infrastructure advisory and data lakes - plus COG  enthusiast - network tools/tecniques
    
Concepts:
   - shared data - makes less wrangling
   - shared python code - allows reuse
   - cross-project communication - breaks silos and diverse teams build better solutions
   - data deluge is coming - lets be ready to filter and use what we want
        
        
    
# Signell Reading List

- https://github.com/pangeo-data/cog-best-practices
- https://github.com/intake/intake-stac/tree/main/examples    
        

---
![https://www.usgs.gov/center-news/doucette-discusses-future-eros-science-earthmap-new-branch-chief](https://www.usgs.gov/center-news/doucette-discusses-future-eros-science-earthmap-new-branch-chief)

## Now a word from ssh - its the key to every door

### ssh keys

- nice article here
- [https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)


#### SSH Summary

- SSH is a secure protocol used as the primary means of connecting to Linux servers remotely.
    - and github and gitlab -- code.usgs.gov
- SSH is a secure protocol used as the primary means of connecting to Linux servers remotely.
- you will be dropped into a shell session, which is a text-based interface where you can interact with your server.
- Clients generally authenticate either using passwords (less secure and not recommended) or SSH keys, which are very secure.
    - I miss usercode and password - sometimes
- SSH keys are a matching set of cryptographic keys which can be used for authentication.
    - public --- share with everyone
    - private - never share or you will get in trouble


- ssh-keygen ---- # generates a key pair PAIR
    - ~/.ssh/id_rsa: The private key. DO NOT SHARE THIS FILE!
    - ~/.ssh/id_rsa.pub: The associated public key. This can be shared freely without consequence.

#### Where they go
- the public key must be copied to a file within the user’s home directory at `~/.ssh/authorized_keys`
- or in a github/gitlab - central repository  using settings --> keys ... 
#### They look like this

```
tony@jose ~ $ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDcy3arx6+bW7LIVtgRgkfB/1tGieIVt6Id90qMnve2kRBBK3qlzEFgtwIsl8Io8Rr9Ip3e0apJQwSw3rTXkLd11J6xDLjkRBKWU2jsaYOn8iSfbaHT5JHMEAfTEZ49AELjdMNSBTb0TYw/cmKE9bLNMchmYNvfPnCidv/TakOY+DB1ZdSfDgI+NKoPZQ+Y9sK4Hl8xIEevwR2C0oP7S4+ekU9Fd3tx34R66vDyeCQeJItFp9Q1a7mW+wmulafAdr/Y3vxcEe4ArCPsDRgs8ElT0mrYD7csXZGNjqBxmSe/rNvknD/byE7SgMWvodWOpWRdN8/0eHzSsPJ1zvfnAW49 tony@jose
```

#### The belong here
- the public key must be copied to a file within the user’s home directory at `~/.ssh/authorized_keys`
- or in a github/gitlab - central repository  using settings --> keys ... 

- 

### SSH Use Cases

- local laptop - to cloud ec2 instance
- pangeo jupyter - to git repo - such as code.usgs.gov
- ec2 instance --> denali or tallgrass
- lots of scp scenarios


## Github and code.usgs.gov

### Create a repo - add a file - edit a file - git add - git push

### Windows Git Tools
- git bash
- git gui tools
- pycharm git integration - IDE based

## HLS - Next WEEK
![a](https://cdn.earthdata.nasa.gov/conduit/upload/14905/CMR_Overview.png)
## Brave Sir Logan and The CMR 
- Common Metadata Repository (CMR) - Earthdata - NASA
- Logan says register here:
    - I think you just need an earth data log in 
    - https://urs.earthdata.nasa.gov/


## geojson.io and google - measure distances - klm 

- demo cut and paste into geojson.io
- talk about importing as a kml in google maps
- all you need is a chromebook to do science.


[https://www.google.com/maps/d/?hl=en](https://www.google.com/maps/d/?hl=en)


### HLS GRID

![hls](./Assets/hls-grid-conus.PNG)


---
## Sentinel
- klm grid and google maps

![a](https://dragon3.esa.int/documents/247904/266366/Sentinel-2-MSI_Product_Types_Figure_1_v3/262f604c-de1e-4cf7-b4f6-abdd7f0dc5fd?t=1523262257162)

## Composite Work

### Pangeo Startup Sequence

![pang](./Assets/pangeo-k8s-startup-event-log.PNG)


---
## Landsat-8 TOA
## Simple Animations using Landsat-8 TOA


---
## Denali integration Scenarios

- composite on AWS --- Characterize on Denali or Tallgrass
- Water Evaporation and Runoff on AWS --- Evaluate Water Balance Model fidelity on Denali using Stream Guage Data

    - brand new USGS `Landsat Collection2` - Surface Reflectance in UTM
        - coming soon Albers
    - Experimental `Harmonized Landsat-Sentinel`
    - nearFuture Suomi NPP will carry five science instruments 
        - Suomi NPP is the first satellite mission to address the challenge of acquiring a wide range of land, ocean, and atmospheric measurements 
- Synergies with google maps and geojson.io
- NO LICENSE FEES
# Cloud

## Unpacking the AWS Cloud

> "Amazon has plans to build a new 120-acre data center park in Oregon's Umatilla County, reported The East Oregonian. The facility will join one of three sites in East Oregon. The existing two are located in the Port of Morrow Industrial Park (Boardman) and at the McNary industrial park just outside of Umatilla."

![oregon datacenter](https://raw.githubusercontent.com/tonybutzer/assets/master/et/50-cloud-boardman-oregon-aws.PNG)

### Location Location Location

![region cost graph](https://raw.githubusercontent.com/tonybutzer/assets/master/et/50-cloud-region-cost-variances.PNG)

### AWS Data Centers
![data center guts](https://raw.githubusercontent.com/tonybutzer/assets/master/et/50-cloud-data-center-guts.PNG)

## Cloud Advantages

1. elasticity and quick to scale
2. ephemeral - break it and rebuild 
3. economies of scale
4. many details are now someone else's problems
	- os patching
5. no down time
6. ubiquitous access
7. speed
8. autonomy - never blocked by human or policy

## Cloud Disadvantages

1. must trust the provider
2. when the meter is running - they are billing you
3. costs seem less tangible

## Managing Costs

1. s3 is $.02 per month per gigabyte
2. some instance types are free

` need to write a whole section here`
- point to a notebook and aws cost analyzer
- simple mitigation strategies
	- reserved instances?
	- spot instances
- cloudchecker - is that what ist called - gov and contractor - have and have nots

## Cattle versus Pets

- all compute servers and docker containers are disposable at a moments notice
- this is actually a really good thing
- decouple compute from code
- everything lives in the cloud
- everything can be instantly recreated from a github repo TEXT file
	- i think that is really cool!!!!!

### Pets Service Model

In the pets service model, each pet server is given a loving names like zeus, ares, hades, poseidon, and athena. They are “unique, lovingly hand-raised, and cared for, and when they get sick, you nurse them back to health”. You scale these up by making them bigger, and when they are unavailable, everyone notices.

Examples of pet servers include mainframes, solitary servers, load balancers and firewalls, database systems, and so on.

### Cattle Service Model

In the cattle service model, the servers are given identification numbers like web01, web02, web03, web04, and web05, much the same way cattle are given numbers tagged to their ear. Each server is “almost identical to each other” and “when one gets sick, you replace it with another one”. You scale these by creating more of them, and when one is unavailable, no one notices.

- from --> https://joachim8675309.medium.com/devops-concepts-pets-vs-cattle-2380b5aab313


## Bucket Permissions

### Cross Account

```
{
  "Version": "2012-10-17",
  "Id": "Policy1563360701540",
  "Statement": [
    {
      "Sid": "ListFrom-usgs-CHS-aws",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::574826924367:root"
      },
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::ga-et-data"
    },
    {
      "Sid": "GetFrom-usgs-CHS-aws",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::574826924367:root"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::ga-et-data/*"
    }
  ]
}
```
---
# Week 12

## Summary

- `Kelcy's notebook` -- Landsat Collection-2 and STAC
- `HLS` Notebooks for mosaic overlap issue
    - start with browse for less clouds and more coverage
    - Look for these NASA LPDAAC concepts in today's notebooks
        - CMR - Common Metdata Repository
        - UMM -- Unified Metadata Model
        - Authentication
- DAGs
- Data Wrangling
- Road to Reusable Code - How?
    - Start with common goals
        - Open Source Python
        - In the cloud
            - and in the HPC(s)
    - Use the same platform for sharing
        - Jupyter Notebooks
        - github and code.usgs.gov 
    - Refine and Refactor your Code so people want to reuse it
        - Self documented or well documented
        - Clean Code -- eliminate code smells
        - Make your code so simple people want to use it
            - good examples
                - xarray
                - hvplot
                - folium
                - pandas
        - Use opinionated approaches
            - xarray, pandas, geopandas - all reinforce rigor and reusability
    - good reusable code allows for lots of work done in few lines of code
    - good code is always a journey
    - Organize Science by common interests in addition to projects
        - Promote non-silo Communication
    - make it simple to install - advertise it

## Future Classes
- Model Analysis work Olena Boiko is working on for evapo
    - We will showcase these notebooks in a future class

### Direct S3 or portal or something in between
- STAC Assets
    - http (portal like)
    - s3://
    - gdal virtual filesystem specifiers /vsicurl/ -- /vsis3/
    - Kelcy and Nathan - map the http to s3 for collection2

---

### Some Folks Just Cannot Let Go of Portals https://landsatlook.usgs.gov/data

```
def convert_llurl(ll_url: str) -> str:
    """
    Convert a landsat look url to an S3 url
    """
    return ll_url.replace('https://landsatlook.usgs.gov/data', 's3://usgs-landsat')

def open_dateset(ll_url: str):
    """
    Open a file with gdal
    """
    with rasterio.open(convert_llurl(ll_url)) as f:
        return f
#     return gdal.Open(path, gdal.ReadOnly)---
```

---

## Kelcy Notebook


[https://code.usgs.gov/klsmith/pangeo-examples/-/blob/master/lcmap-time-series-ccd.ipynb](https://code.usgs.gov/klsmith/pangeo-examples/-/blob/master/lcmap-time-series-ccd.ipynb)


---

---


#### Nathan's less obvious method to cheat http by using s3

```
# remove 33 characters and replace them
#remove everything forward of /collection from the cloudfront object URL
greens = pd.DataFrame(greens['Green'].str[33:])
swirs = pd.DataFrame(swirs['Swirs'].str[33:])
#append s3://usgs-landsat to the front of the URLs
greens = pd.DataFrame("s3://usgs-landsat"+greens['Green'])
swirs = pd.DataFrame("s3://usgs-landsat"+swirs['Swirs'])
```

- kelcy's code is more readable IMHO


---
#### Sentinel COG Example

### Sentinel STAC gets this preference for direct S3 access correct

```
"href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/19/T/CJ/2020/10/S2A_19TCJ_20201014_0_L2A/B02.tif",
```

```
ubuntu@ip-10-12-69-188:~$ aws s3 ls sentinel-cogs
                           PRE sentinel-s2-l2a-cogs/
ubuntu@ip-10-12-69-188:~$ aws s3 ls sentinel-cogs/sentinel-s2-l2a-cogs/
                           PRE 1/
                           PRE 10/
                           PRE 11/
                            ...
```


#### HLS Example
- Buckets
    - lp-prod-protected
    - lp-prod-public

```
import rasterio as rio
e='https://lpdaac.earthdata.nasa.gov/lp-prod-protected/HLSS30.015/HLS.S30.T18TYR.2020278T154121.v1.5.B04.tif'
b04 = rio.open(e)

#dir(b09)
b04.shape


'href': 'https://lpdaac.earthdata.nasa.gov/lp-prod-public/HLSS30.015/HLS.S30.T19TCM.2020278T154121.v1.5.jpg'
```

[https://cmr.earthdata.nasa.gov/search/concepts/G1969487860-LPCLOUD.umm_json](https://cmr.earthdata.nasa.gov/search/concepts/G1969487860-LPCLOUD.umm_json)
```
"https://lpdaac.earthdata.nasa.gov/s3credentials"

Description:    "api endpoint to retrieve temporary credentials valid for same-region direct s3 access"
```

---
## Everyone is moving to the cloud -- getting there is ________

- Opening new horizons:
    - EU
    - How to migrate the Copernicus Global Land Service to a Cloud environment

- conversion of space-based Earth Observation information into `actionable` knowledge 
- Moving Global Land Services to another completely new and technological challenging cloud computing environment is `not a trivial job.`
- providing `clear suggestions` for an efficient ‘cloudification’ of the Copernicus global land production lines and user interfaces, 

- Benefits
    - greater transparency and reproducibility of the data processing chains, enhancing trust
    - better scalability to handle the large volume of data we expect from future satellites
    - better integration with downstream processing chains and thus more value delivered to research and industry

---

```
--- 
Group: "HLS Interest Group"
HLS: 
  - 
    ECO: 
      - "Sujan Parajuli"
      - "Devandra Dahal"
      - "Logan Megard"
      - "Neal Pastick"
      - "Mike Oimoen"
    LCMAP: 
      - "Kelcy Smith"
    LPDAAC: 
      - "Cole Krehbiel"
      - "Aaron Friesz"
    PANGEO: 
      - "Tony Butzer"
    VegDyn: 
      - "Dinesh Shrestha"
      - "Trenton Benedict"
```


## Class Recap

- Still attacking data wrangling
- people should get friendly with github/gitlab -- code.usgs.gov
- pangeo.chs.usgs.gov and other subsidized infrastructure platforms

### References

#### If the Mask fits .. understand it
[https://rasterio.readthedocs.io/en/latest/topics/masks.html](https://rasterio.readthedocs.io/en/latest/topics/masks.html)

### Nice Tutorials - Guest Teacher of the Week

- [https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/](https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/)
- Pat Danielson - volunteer

## Projections and Geoviews
[https://geoviews.org/user_guide/Projections.html](https://geoviews.org/user_guide/Projections.html)

- Managing Overlap in Albers 
- pangeo demos
- github albers-mosiac repo
    - https://github.com/tonybutzer/albers-mosaic



## What's Happening in Pangeo Land

- ECO team will continue to get high speed data access to HLS
    - we have just scratched the surface on how to scale
    - looking for an open source, xarray perhaps, solution to mosiacing like ARCMAP
        - needs to handle overlapping scenes intelligently
- Scotty H - has lots of great tutorials - a little over my head - but i'm learning.
- DataLake 
    - interim - s3://dev-et-data/data-lake - can access it from pangeo.cr.usgs.gov
    - Now that Kristi Kline is on the case we may get more attention on a USGS cloud S3 based Data Lake.
- Binder is pretty cool - more free pangeo compute - 
- The scientist is the critical resource on the planet - never compute


## Direct acyclic Graphs

- used in DASK
- used in python code graphing/flow charting - dependency trees
- graphviz and pyan3 # python analyzer
    - [https://graphviz.org/](https://graphviz.org/)
- consists of vertices and edges (also called arcs), with each edge directed from one vertex to another, such that following those directions will never form a closed loop.

![dag](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Tred-G.svg/440px-Tred-G.svg.png)

## Data Wrangling Working Group

## Data Lake Work

- Class A Data Assets
    - Landsat Collection-2
    - Sentinel Cogs
    - Harmonized Landsat Sentinel (1.5)

- Class B Data Assets
    - NLCD
    - LCMAP Products

- Class C Data Assets
    - Soil ...

Concepts:
   - shared data - makes less wrangling
   - shared python code - allows reuse
   - cross-project communication - breaks silos and diverse teams build better solutions
   - data deluge is coming - lets be ready to filter and use what we want
        
        
    
# Signell Reading List

- https://github.com/pangeo-data/cog-best-practices
- https://github.com/intake/intake-stac/tree/main/examples    

## Other

- https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/
        

---

### Pangeo Startup Sequence

![pang](./Assets/pangeo-k8s-startup-event-log.PNG)


---

---
## Denali integration Scenarios

- composite on AWS --- Characterize on Denali or Tallgrass
- Water Evaporation and Runoff on AWS --- Evaluate Water Balance Model fidelity on Denali using Stream Guage Data

    - brand new USGS `Landsat Collection2` - Surface Reflectance in UTM
        - coming soon Albers
    - Experimental `Harmonized Landsat-Sentinel`
    - nearFuture Suomi NPP will carry five science instruments 
        - Suomi NPP is the first satellite mission to address the challenge of acquiring a wide range of land, ocean, and atmospheric measurements 
- Synergies with google maps and geojson.io
- NO LICENSE FEES
- Jen Rover is in HPC school
- Should be able to use notebooks in both environments - cloud and HPC
    - IF the python `version monster` does not get you!

---

## END OF WEEK 12

---
# Glossary

---
- **Agency Problem:**
> The **agency problem** is a conflict of interest inherent in any relationship where one party is expected to act in another's best interests. In corporate finance, the agency problem usually refers to a conflict of interest between a company's management and the company's stockholders.  ['Windows OS', 'Kubernetes?', 'Jira/Confluence?']

![](./Assets/rest-of-the-herd.PNG)
---
- **COG**
> What are Cloud Optimized GeoTIFFs (COGs)?

> A **Cloud Optimized GeoTIFF (COG)** is a GeoTIFF file with an internal organization that enables more efficient workflows in the cloud environment.  It does this by leveraging the ability of clients issuing HTTP GET range requests to ask for just the parts of a file they need.
*Geek Hint:* Use rio info and gdalinfo to see the innards of a COG and the overviews associated with a COG.
For more info talk to THE GOOGLE.

---
- **Data Lake**
---
- **Data Wrangling**

- Transferring, organizing, reprojecting, verifying, locating, formatting, netcdf, geotiff, hdf, ascii, json, mtl, xml, storage, costs
- Downloading, portaling, machine-to-machining, researching, refreshing, forward-processing

---
- **DataOps**
> DataOps is an automated, process-oriented methodology, used by analytic and data teams, to improve the quality and reduce the cycle time of data analytics. While DataOps began as a set of best practices, it has now matured to become a new and independent approach to data analytics. - Cassandra Ladino USGS ACIO has experience in DataOps
---
> What is DataOps?

> DataOps is a collection of technical practices, workflows, cultural norms, and architectural patterns that enable:

    - Rapid innovation and experimentation, delivering new insights to customers with increasing velocity

    - Extremely high quality and very low error rates

    - Collaboration across complex arrays of people, technology, and environments

    - Clear measurement, monitoring and transparency of results


---
- **Dark Repository**



---
- **DevOps**
> DevOps Model Defined

---
> DevOps is the combination of cultural philosophies, practices, and tools that increases an organization’s ability to deliver applications and services at high velocity: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes. This speed enables organizations to better serve their customers and compete more effectively in the market. [https://aws.amazon.com/devops/what-is-devops/](https://aws.amazon.com/devops/what-is-devops/)


- **focused and diffuse thinking**
> In her book A Mind for Numbers, Barbara Oakley calls these two different ways of approaching a problem “focused thinking” and “diffuse thinking.” She claims that both of them are crucial for analytical and creative thinking, and that switching between the two modes is a great way to get unstuck when you’re facing a difficult problem.
> Diffuse thinking happens when you let your mind wander freely, making connections at random. The diffuse mode of thinking does not happen in any one area of the brain, but rather all over. The challenge for all is to cultivate an efficient state of mind, depending on what we wish to accomplish.

---
- **docker**
![](https://raw.githubusercontent.com/tonybutzer/data-curation/master/dataDog/eng/assets/dockerVirtualization.png)
---
- **Imposter Syndrome:**
> **Imposter syndrome** can be defined as a collection of feelings of inadequacy that persist despite evident success. 'Imposters' suffer from chronic self-doubt and a sense of intellectual fraudulence that override any feelings of success or external proof of their competence


---
- **Jupyter (Notebook and Hub)**

---
- **open source software**

> What is open source software?
Open source software is software with source code that anyone can inspect, modify, and enhance.

> "Source code" is the part of software that most computer users don't ever see; it's the code computer programmers can manipulate to change how a piece of software—a "program" or "application"—works. Programmers who have access to a computer program's source code can improve that program by adding features to it or fixing parts that don't always work correctly.
What's the difference between open source software and other types of software?

> Some software has source code that only the person, team, or organization who created it—and maintains exclusive control over it—can modify. People call this kind of software "proprietary" or "closed source" software.

> Only the original authors of proprietary software can legally copy, inspect, and alter that software. And in order to use proprietary software, computer users must agree (usually by signing a license displayed the first time they run this software) that they will not do anything with the software that the software's authors have not expressly permitted. Microsoft Office and Adobe Photoshop are examples of proprietary software. [here](https://opensource.com/resources/what-open-source)

---
- **PANGEO**



---
- **STAC**
> STAC is a standardized way to expose collections of spatial temporal data. ... It can be used for external access to your holdings, exposing your information to search engines and to a growing ecosystem of tools.
---
> "So STAC itself has no aim to provide one single index, but to encourage the basic unit of information from which a variety of indexes can be built. For STAC that basic unit is the actual geospatial asset and a JSON description of the core fields. This mirrors the design of the web as a whole: html pages are the basic unit of information, and companies like Google build the global search index. Creating a great geospatial search index is left to others to innovate on, but the STAC spec aims to encourage software implementations and data providers to expose their holdings in a way that everyone can understand." - Chris Holmes
---
> Chris Holmes Product Architect @ Planet, Board Member @ Open Geospatial Consortium, Technical Fellow @ Radiant.Earth -- Chris's medium articles contain well-written descriptuions of these cloud optimized ecosystems that can be exploited to simplify science.

---
- **terraform**

> Terraform is an open-source infrastructure as code software tool created by HashiCorp. Users define and provision data center infrastructure using a declarative configuration language known as HashiCorp Configuration Language, or optionally JSON. Terraform manages external resources with "providers"

> **terraform** creates infrastructure out of thin air - **terraform** allows tony to feel like Bob Ross painting infrastucture "lets have a nice litte server here ... next to our little network here and a lovely little data bucket over there."
```
$ scp bob_ross.PNG ubuntu@`resolv hweb`:.
```
![](./Assets/bob_ross.PNG)

---
- **Yak Shaving**

> **Yak shaving** refers to a task, that leads you to perform another related task and so on, and so on — all distracting you from your original goal. This is sometimes called “going down the rabbit hole.” 
- Donavon West
- American Express Developer Relations

<img src="https://americanexpress.io/_post_assets/yak-shaving/img/yak-shaving-small.png" width="30%">
# Week 13 - day in the life of ETa

### subtitle - Don't Tell My Boss

## Real World Scene

- My boss - says I have to get Tmin, Tmax and Tavg - done for 150 years - converted to Celsius
    - from that useless Kelvin data i gave her - she is not happy
    - she says I have until COB Friday or look for another job
    - The problem is it looks like golfing weather for Monday and Tuesday
    - So I think use the cloud and docker - maybe this can be done 
    - I spend a day figuring out the sophisticated algebra and try to play that up - But she is on to me.
    - docker - container from jupyter to orchestration in 2 easy steps

### run the orchestration


> two system engineers walk into a bar

- ... the first one asks why can't we do that simple Kelvin conversion by friday on our current platform

- ... the second eng says cause x and y suck

- ... the next day the 2nd eng is explaining this converstion to his Govt Sponsor as:

    - well you see the Netapp is bandwidth constrained and not really intended for large image data xfers and Microsoft has chosen Linux as its highly scalable platform for its Azure Cloud.

## Community Interest
- Looking at Pangeo and Docker on HPC
    - Could support nice hybrid solutions between the cloud and HPC(s) Denali, Tallgrass
    - need to examine Singularity and Shifter on the HPC
    - I may call my orchestration method - manual_transmission :-)
- Tony prefers scaling with docker versus other methods - Why:
    - MPI – Message Passing Interface¶
        - Distributed Memory Systems
        - More difficult to parallelize
        - Requires a change in fundamental programming
    - Kubernetes is well over 1 MILLION lines of code
    - Slurm - the s stands for simple - is over 500,000 lines of code
    - Simple Orchestration -  129 lines of code

```
ubuntu@ip-10-12-69-188:/opt/kelvin_celsius/api$ wc -l kelvin_*.py
129 kelvin_orchestration.py
```


## Community Case Studies
- VegET in the cloud
    - Cloud Scaling
    - Model validation without ARC tools
    - Simple Visualizations
    - Pathfinder project for other cloud enthusiasts
- ETa pipeline from SSEBoP (Google Earth Engine)
    - Pushing data into a Dark Repo
        - Web Interface for endusers
        - Many data users just want direct access to COGs


## Day in the Life of the low budget ET project

---
![](./Assets/VegET-DRB-Rouze.PNG)
---

1. Port the VegET model from Windows and Netapp  - to cloud, xarray and S3 data storage
2. Run the model on small AOIs
3. Scale the Model by slicing the problem spatially 
    - glue the parts together with simple xarray code and multiple docker containers for scaling
4. Wrangle and Wrangle Data for Delaware, Conus, NorthAmerica, Globe
    - Also just to make it more challenging - add projected or future model data for temperature and precip
    - do this with as few people as possible with tight deadlines
5. Run the model for 150 years over Delaware
    - Notice some data model issues over 2000-2020
    - Visually apparent with jupyter-python-panel-app.ipynb
5. Run DRB again for 70 years times 2 with different soil intercept values.
6. Hire a `Model Integrity Analyst` Olena 
    - Write a simple pandas model simulator
        - replaces old windows manual excel spreadsheet methods
    - Discovered Kelvin and Celsius Confusion
    - ![](https://www.nasa.gov/sites/default/files/styles/side_image/public/thumbnails/image/1979_hst_primary_mirror.jpg?itok=UJ4wDauY)
7. Wrote a very simple Kelvin-->Celsius Conversion Python Notebook --> Python App with Argparse API
    - Run this in class today 1950 --> 2099
        - Notebook prototype/bread-board    
            - Slicing in python and xarray - time-series
            - simple docker image
            - basic orchestration 101
            - functional programming like `ds = ds - 273.15`
8. Convert to pure Python - Olena and add argparse to replace hardcoded values
    - jupyter nbconvert --to script  my_ugly_notebook.ipynb
9. Create an orchestration python wrapper - borrow an old one and customize this
# Below HERE there be unfinished/unpolished work
## Project Execution Plan

```
Note - see the major milestones and break it down here 
or in the kanban
```

## December Milestone
- onboarding class and feedback
# Week 14 - Olena -- matplotlib and pandas

## Overview

1. Introduction - Tony
2. Evapo model evaluation landscape - `Stefanie Kagone`
3. Using Xarray slicing and Pandas to automate Spreadsheet Model Analysis - `Olena Boiko`
4. Apply cloud solutions to HLS plipelines - `Logan Megard`
5. Using Open Data Cube to align pixels and then bigPangeo (netcdf ingest) to look at clouds in the cloud - tony

---
# EROS Items of Interest

1. Science continues to elevate
    - Pete Doucette  - Data Center Director
    - Terry Sohl - Science Lead
2. Aaron Friez (Pangeo/DAAC/Science - Workshop/Lecture)
    - Organized -- April 5?
3. Cali - searching for an intern
    - In charge of collating disparate/disaggregated training
    - "Oh Cali" - "if the world could just be aggregated"
4. Summer Hours for AWS Onboarding - begin May 1. - 
    - Get Vaccinated - save a scientist we need them.
5. Evapo - seeks partnership with Jim Rowland on project cloud account similar to Neal's and Kelcy's
6. Evapo Actrivities
    - Next cloud model please - SSeBop - meets Modis meets cloud - Thanks Claudia, Olena and Steffi
    - Co-sponsor for NLCD data wrangling and emerging datalake prototype.
        - Dinesh and Trenton to test NLCD data lake and HLS access
    - HUC12 - zonal stats - impress your stakeholder with a map-reduced spreadsheet
        - Data starts to inform as information
7. HLS Activities Logan
    - Tony still does not like Authentication nuances
    - Rehearsing wrangling for Devandra and Sujan
8. Open Data Cube - cube-in-a-box - (now a word from my sponsor)
    - higher level abstraction - hint at what is possible. - black box - black magic approach.
    - Hey ODC don't make me index and learn Postgresql and PostGIS - my life is already disaggregated enough
9. Tony wakes up and uses github.io
    - Using the cloud == FAIL!
    - Using Tony's home server == FAIL
    - USING GITHUB.IO - I found Goldilocks - this one is just right!

## Favorite/Featured References

- http://gallery.pangeo.io/repos/pangeo-data/landsat-8-tutorial-gallery/landsat8.html
- https://docs.dea.ga.gov.au/notebooks/Frequently_used_code/Masking_data.html

### Pangeo Jupyter Book - that Ryan Abernathey has Created -->
- https://earth-env-data-science.github.io/intro


### Scott Henderson Medium Article

From

- https://medium.com/pangeo/intake-stac-nasa-4cd78d6246b7
- Scott Henderson - Dec 2020

### Overview
---

```yaml
--- 
Abstractions: 
  - openDataCube
  - stac-intake
Asset-Location: S3
Deployment-Technology: docker-compose
Format: COGS
Metadata-Containers: 
  - postgis-odc
  - stac-json
STAC_API_URL:
  - 'https://explorer.sandbox.dea.ga.gov.au/stac/'
  - 'https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs'
Sandboxes: 
  - cube-in-a-box
  - pangeo.chs.usgs.gov
  - etrocks-sandbox
Satellite: Sentinel-2A-2B
Topics: 
  - "Sentinel SCL"
  - ODC
  - Masking
  - Xarray-->netcdf
  - finding-clouds-in-the-cloud
```

---

# Featured Instructors - Key Points

- pandas, xarray, rasterio, matplotlib, holoviews - xarray.hvplot
- Innovative_Fast_solutions = open source + brainPower

- Olena and Steffi Model Verification
    - Significant as it directly and rapidly improves our scalable model code for Evapo
- Logan HLS 1.4 and 1.5 Research
- 

---

[https://www.usgs.gov/center-news/calibration-test-site-becomes-agricultural-hotspot?qt-news_science_products=2#qt-news_science_products](https://www.usgs.gov/center-news/calibration-test-site-becomes-agricultural-hotspot?qt-news_science_products=2#qt-news_science_products)



![](Assets/sentenel-scene-classification-levels.PNG)


---
### Open Data Cube (ODC) - glimpse

## Use Open Data Cube to extract Dwyer Cube from Sentinal S3 COGS

## Then use the big pangeo to explore Compositing with (Bunde, Postma, Danielson)

### ODC Outputs (netcdf/nc files in S3)
```
maine.nc
maine_ard.nc
maine_masked_s2_all_bands.nc
maine_s2_all_bands.nc
maine_s2_common_name_bands.nc
```

## maine_masked_s2_all_bands.nc
- main test nc file for compositing Maine - R&D only

- briefly understand cloud and shadow masking 

- [http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/2_tony_save_load_ard_all_bands.ipynb](http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/2_tony_save_load_ard_all_bands.ipynb)

- [http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/00_tony_class_exhibit_learning_odc_claibration_site_Sentinel_2.ipynb](http://10.12.68.246:8080/notebooks/composite/30-cubebox-helper/00_tony_class_exhibit_learning_odc_claibration_site_Sentinel_2.ipynb)






## Concept of Operations


## The Ecosystem

## Github

### since everything in the cloud is EPHEMERAL- GITHUB is CRUCIAL

## Compute aka ec2 instance(s)

## Storage aka s3 buckets

## Inputs
### Public Data Sets

## Processing

## Outputs


## Questions

## Pictures?
# Week 15 HPC Edition Pangeo + Singularity

# NEXT WEEK - Aaron Friesz - Teaches class on Monday 
- so no class on next tuesday
    - No class on next tuesday?
        - that's right no class next week -tony
- Tony's summer hiatus coming soon

## Overview
- around the projects
- datalake experiment
- hpc - denali and tallgrass
    - very similar to cloud 
    - different approach
    - sponsored $$$
        - compute
        - data storage
        - scaling - both have batch
        - rescale?
- pangeo demo on:
    - bigPangeo
    - miniPangeo
    - Tallgrass
- 

https://www.usgs.gov/center-news/denali-tallgrass-eros-launch-new-era-high-performance-computing-capabilities


## Around the Projects

- Logan continues to improve his orchestrated docker containers for downloading H:S and creating NDVI.
- Olena is working on Jupyter to explore the inverse relationship of NDVI and LST (temperature) for tuning Evaporation Models,
- Steffi is looking at ways to do CONUS scale VegET with the cloud and/or HPC (PANGEO-based)
- Tony is exploring Singularity and PANGEO on TALLGRASS - 
- Pat Danielson - is looking at ways to do better, faster, cheaper composites with scalable hardware and linux open-source.


![](https://media0.giphy.com/media/3d8mZpR1z4NFy6gIBA/giphy.gif?cid=ecf05e47w26iqr23x2mo46f6qgiia0cx7v6bmpvtsfz49u9t&rid=giphy.gif)

---

> “HPC is just another tool in the toolbox,” he said. “So, what we’re trying to do is get people more comfortable with running large-scale simulations of data analytics and modeling. We want to make that a fabric within USGS so that it changes the culture within the Survey. We don’t want people having to deal with things on their own. We want to make sure everybody has the right tools, or at least good enough tools, to get their jobs done.” - Falgout

- the right tools
- don't have people try to go this alone - collaborate
- get scientists comfortable with these disruptive scalable environments
- Falgout is on to something here

- https://www.usgs.gov/center-news/denali-tallgrass-eros-launch-new-era-high-performance-computing-capabilities
---

## HPC

#### I like Tallgrass vs. Denali

1. Because it has singularity for support of containers - more to come

#### BUT -->  salloc: Job 1567397 has exceeded its time limit and its allocation has been revoked.


#### Singularity Demo

```
make salloc

make shell


module load singularity

singularity shell docker://ubuntu:latest

singularity run library://sylabsed/examples/lolcow
```
---


### Singularity Features - why was it created?

1. No Root Access in Containers - you run as butzer 
2. Created for scientists on HPC
3. Integrated volumes - your home directory /home/butzer and Caldera are just there
4. Job Scheduling integration with slurm

I was not happy that I had to learn - yet another orchestration tool - let alone two - singularity and slurm

### Singularity Versus pure Docker
> For one, security. HPC environments are typically multi-user systems where users should only have access to their own data.

> For all practical purposes, docker gives superuser privileges. It’s hard to give someone limited Docker access.Sure there’s SELinux and the like, but Docker just wasn’t designed to keep users out of each other’s stuff. Singularity effectively runs as the running user and doesn’t result in elevated access.

> Another is scheduling. On my cluster we use slurm, and users submit jobs with CPU/memory/time requirements. The Docker command is just an API client that talks to the docker daemon, so the resource requests and actual usages don’t match. Singularity runs container processes without a daemon. They just run as child processes.



```

[butzer@ml-0001 ~]$ singularity shell library://sylabsed/examples/lolcow
Singularity lolcow_latest.sif:~> lolcat --help

Usage: lolcat [OPTION]... [FILE]...

Concatenate FILE(s), or standard input, to standard output.
With no FILE, or when FILE is -, read standard input.

    --spread, -p <f>:   Rainbow spread (default: 3.0)
      --freq, -F <f>:   Rainbow frequency (default: 0.1)
      --seed, -S <i>:   Rainbow seed, 0 = random (default: 0)
       --animate, -a:   Enable psychedelics
  --duration, -d <i>:   Animation duration (default: 12)
     --speed, -s <f>:   Animation speed (default: 20.0)
         --force, -f:   Force color even when stdout is not a tty
       --version, -v:   Print version and exit
          --help, -h:   Show this message

Examples:
  lolcat f - g      Output f's contents, then stdin, then g's contents.
  lolcat            Copy standard input to standard output.
  fortune | lolcat  Display a rainbow cookie.

Report lolcat bugs to <http://www.github.org/busyloop/lolcat/issues>
lolcat home page: <http://www.github.org/busyloop/lolcat/>
Report lolcat translation bugs to <http://speaklolcat.com/>

Singularity lolcow_latest.sif:~> which lolcat
/usr/games/lolcat
Singularity lolcow_latest.sif:~> cowsay -f tux  hello there | lolcat -a
 _____________
< hello there >
 -------------
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
```

- tony says - 'oh yeah what do you use your supercomputer for'


#### HPC DOC Walk Thru

[https://hpcportal.cr.usgs.gov/hpc-user-docs/Resources/Cheat_Sheets.html](https://hpcportal.cr.usgs.gov/hpc-user-docs/Resources/Cheat_Sheets.html)


[https://vim.rtorr.com/](https://vim.rtorr.com/)


[https://cheatography.com/davechild/cheat-sheets/linux-command-line/](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)

### Big Data and Data Cubes

> " Developments of sensing observations and producing information from it need to be accompanied by suitable storage, processing and retrieval systems. " - from ...
[https://www.tandfonline.com/doi/full/10.1080/17538947.2019.1585976](https://www.tandfonline.com/doi/full/10.1080/17538947.2019.1585976)


## Data Lake Discussion - Demo

- copied data from Neal's bucket eco-w1 to Caldera
- copied anhb nlcd fro Caldera to a usgsOPEN-bucket ... dev-et-data -- aka Steffie's bucket.

- demo access from Steffie's private mini-pangeo - http:/10.12.68.246
- demo access from theBigPangeo -- http://pangeo.chs.usgs.gov
- demo local Caldera access from Jupyter via Tallgrass

```
tallgrass

make salloc

make shell

(start jupyter)
./launch(TAB)

tunnel 8888
# cut/paste the ssh tunnel 8888


http://localhost:8888

```

## Two HPC Pangeo notebooks demos

- http://localhost:8888/notebooks/opt/etscrum/2_ET_HPC/00-notebooks/0_HPC_for_dummies_like_tony.ipynb
- http://localhost:8888/notebooks/opt/etscrum/3_nlcd_datalake/1_HPC_anhb-viewer.ipynb


### Steffi's mini pangeo 
- http://10.12.68.246/user/butzer/notebooks/opt/nlcd-datalake/scp-tools/1_nlcd-anhb-viewer.ipynb

### bigPangeo
- exact same notebook runs here 
- how is that possible
    - datalake!
    - notice caldera and home directory are ubiqutous accross - denali and tallgrasss
    - datalakes will be accessible world wide - the opposite of dark repositories of data
- notebook url HERE
- https://pangeo.chs.usgs.gov/user/butzer@contractor.usgs.gov/notebooks/nlcd-datalake/scp-tools/1_nlcd-anhb-viewer.ipynb

# Data Lake

#### approach

1. model a data lake in the dev-et-data bucket - USGS-wide access
2. infiltrate the CHS leaders and elevate the priority of a USGS datalake
3. find common data needs and practice wrangling them vis the Data Wrangling Working Group
    - remember data wrangling is still a real thing

![](https://raw.githubusercontent.com/tonybutzer/etscrum/a46efbe7884e936973cd7fe55162a295c700b02f/Attic/00-presentation/ard/datawrangling_is_real.PNG)

---

### DWWG next steps:

1. Determine VegDyn NLCD Needs (Trenton, Dinesh)
    - perhaps look at gridmet, daymet etc ...
2. Refine Logan's NLCD wrngling pipeline - add orchestration
3. Wrangle some more NLCD and test with VegDyn-centric notebooks
4. Move some of the VegET wrangling to the cloud - with branch to Caldera

## Show STAC - for maine and clipping and crs from plateCarree
- time permitting?

- find this demo - do it in the pangeo
- https://pangeo.chs.usgs.gov/user/butzer@contractor.usgs.gov/notebooks/opt/composite/40-intake-stac-henderson/1-just-aoi-intake-stac-egypt-calibration.ipynb
# Week 16 - Welcome Landfire

Today we welcome the Landfire, FireScience team to this community of best practices and this community of sharing, notebooks, concepts, code , data and most importantly - non-silo-ed talent. Welcome Tolk, Brian (Contractor) L  -- and Degaga, Erica J
 
## What is this class?
1. A community of cloud based Scientists that:
    - use the cloud
    - some have custom cloud accounts
    - some use the Landsat account
    - some use thebigPangeo
    - some have their own mini-Pangeos/jupyterHubs/sandboxes
    - 
2. Notable technologies
    - Python
    - Open Source
    - Image Processing and GIS
        - xarray, pandas, matplotlib, holoviews, geoviews, geopandas, rasterio, GDAL
3. Remote Sensing Cloud Stored assets
    - Landsat - utm/albers/ ---> ARD tiles
    - Sentinel-2-COGs
    - Hamonized Landsat Sentinel
4. Making birds-of-a-feather connections in science
5. focus on TRAINING - lets have a highly TRAINED Science team and a world class data center
    - start with simple get togethers - this class
    - jot some disorganized notes
    - share some draft notebooks
    - stuff code and docs in github
    - hire an intern to organize and collate this stuff
    - repetition
    - learn how to use git search in the meantime
    - reach out and ask for help - connectors include Rich Signell, Nathan, Aaron Friesz, tony ....

## Teams
1. Evapotranspiration -- Water - Steffi, Olena
2. Land Cover - Brett, Pat, Kory
3. LCMAP - Kelcy
4. Invasive - Sujan, Devandra, Logan, Neal
5. Web Development Team - Claudia, Maxwell, Michelle, Balu ...
6. VegDyn - Trent, Dinesh
7. Emerging AI experts ...


> Basically, ostensibly- lots of superior TALENT

## A group of experts 

- here are just a few - there are many i have not enumerated and some i have not yet discovered

1. Logan Megard - HLS -- DevOps
2. Steffi Kagone - Converting Models from ARCPY to rasterio
3. Olena Boiko - Data Wrangling Expert - MOdel QA Expert - Jupyter/matplotlib
4. Kelcy Smith - Python Expert, Jupyter Expert, time-series expert - STAC expert
5. Nathan Roberts - user service - data management 
6. tony - DevOps and OpenDataCube, docker, code portability, networking and file transfers

## Today
Today I am privileged to have guest instructors:
Kagone, Stefanie (Contractor) -- and -- Boiko, Olena are back for an encore lesson on how to use the bigPangeo - pangeo.chs.usgs.gov to look at refining the sophistication of the model by improving the fidelity of NDVI.  
 
also ...
Danielson, Patrick (Contractor) -- and -- Postma, Kory (Contractor) will give an opinionated demo of a notebook on STAC meets one of the mature STAC Catalogs for Sentinel-2-COGs.
 
We can talk a little about the data wrangling and scp and rclone we have been doing between the Netapp, Caldera and S3.
 
And we can talk about finding Albers Scenes for Landsat Compositing using the young, immature Landsat Stac Catalog.
 
Nathan Roberts and Rich Signell are both presenting Pangeo/OpenDataCube papers at conferences this month.
 
So the folks attending this class are Early Adopters of technology and infrastructure stacks that will revolutionize science in the next few years.

# Prepare the Pangeo - release the kracken
# start the pangeo tony START IT
- [https://pangeo.cr.usgs.gov](https://pangeo.cr.usgs.gov)
 
---

# Overview

## Steffi and Olena
#### Modis derived NDVI an Land Surface Temperature
- Uses the big pangeo
- uses R**2 to evaluate hypothesis
- ran in a $200 mini-pangeo - now runs in the freeFREEfree https://pangeo.chs.usgs.gov

## Pat and Kory
- so far many have come up to speed with Jupyter Lab/Notebook quickly
    - The ability to share snippets of code, concepts, visualizations - is a gamechanger
    - Jupyter is not a full-blown IDE - i say so what!
- these few weeks will look at composites with HLS, sentinel and Landsat - starting with data discover via STAC.
---


---

## Make friends with git
- https:/code.usgs.gov


## quit hiding your code and data -
### From Kindergarten

```
Share everything.

Play fair.

Don’t hit people.

Put things back where you found them.

Clean up your own mess.

Don’t take things that aren’t yours.

Say you’re sorry when you hurt somebody.

Wash your hands before you eat.
```


## Landsat Albers by way of BT detour.



## Data transfer - how do I get my data to and from the cloud 
- to is always free
- from can come with egress costs unless
    - you use rclone or some other sneaky method

- we were able to get these rates
    - 40 MBytes per second from cladera --> s3
    - 2 Mbytes per second using VDI machines for most transfers
    - .5 Mbytes when using windows and the VPN/PulseSecure

- we have played with many fileTransfer agents
    - tony's favorites are scp and rclone and perhaps some of their derivatives - like lftp
    - more to come - more help available ....



```
 rclone copy -P et-data:/dev-et-data/in/DelawareRiverBasin/PPT/2000/ tallgrass:/caldera/projects/usgs/water/impd/butzer/PPT/2000/
```


## Question of the Week - Partial Git Clones

```bash
#! /bin/bash

function git_sparse_clone() (
  rurl="$1" localdir="$2" && shift 2

  mkdir -p "$localdir"
  git config core.sparseCheckout true

  # Loops over remaining args
  for i; do
    echo "$i" >> .git/info/sparse-checkout
```

### use wget for single notebooks

1. find the raw link in github 
    - https://raw.githubusercontent.com/tonybutzer/composite/main/01-danielson/1_LANDSAT_ALBERS_MAINE/0_maine_landsat_albers.ipynb

```
wget https://raw.githubusercontent.com/tonybutzer/composite/main/01-danielson/1_LANDSAT_ALBERS_MAINE/0_maine_landsat_albers.ipynb
```

### Costs

```
ubuntu@ip-10-12-68-246:~$ docker run tbutzer/aws-price python awsprice.py butzer
['awsprice.py', 'butzer']
butzer
     state                     name            ip       i_type  monthly_cost
0  running  butzer-et-mini-pangeo-0  10.12.68.246  t3a.2xlarge       219.584
1  stopped        butzer-bigsship-0   10.12.69.45  m5a.4xlarge       502.240
2  running       butzer-tendollar-a  10.12.68.236     t2.micro         8.468
==========================================================================================
==========================================================================================
     state                     name            ip       i_type  monthly_cost
0  running  butzer-et-mini-pangeo-0  10.12.68.246  t3a.2xlarge       219.584
2  running       butzer-tendollar-a  10.12.68.236     t2.micro         8.468
========================================================================================================================
=====================================================================
```

[Harry House on Cost - The truthful answer to this question is “it’s complex, and it depends.](https://support.chs.usgs.gov/pages/viewpage.action?pageId=40370588)

> One would presume that most private companies would be aware of the total cost of ownership within their borders and may well be more likely to adopt the Cloud sooner from a cost perspective if nothing else. 

Here is a list of considerations when contemplating the Cloud or on-premises from the viewpoint of comparable expenses: 

For Using On-premises

    Cost to purchase the on-premises equipment

    Cost to configure and manage the on-premises equipment

    Cost to maintain the power and air conditioning in the computer room

    Cost of the system administrators to support the computer room and all the devices therein

    Cost of the floor space (rented or owned but not usable for other purposes) for the on-premises system

    Cost of on-site backups

    Cost of network connectivity

    Cost of meeting security controls related to the facility


## DevOps Consulting - tony

- terraform
- s3 tricks and traps
- docker
- ec2 and costs

## Prior videos are available in M$-stream
- you can watch these in 2x speed and skip around.

## Rich SigNELL hidden gem
BTW, I don't know if you think this is cool, but I found out something new about fsspec this morning... .It's more than just for s3!   
https://nbviewer.jupyter.org/gist/rsignell-usgs/8e3051974d0e3a1722369cafe9e0005e
# Week 17 Google Cloud and AWS Oh My

- so many technical options and choices - so little time.

## What does this class teach again?

1. How to exploit the AWS Cloud via CHS
2. PANGEO - Xarray, Pandas, Holoviews ...
3. DevOps for the science guys
4. Moving, Wrangling Data with less effort and less time
4. Don't MOVE your data - teleport to Oregon - us-west-2
5. Jupyter and Python - easy to write - easy to run
6. Docker its in there

## Future Classes
1. Logan - HLS experiments for ECO-invasive
2. Aaron - s3 direct access LPDAAC HLS
3. Kelcy - time series landsat
4. Pat Danielson, Kory, Brett, Brian Tolk -- Compositing - NLCD and FireScience
5. Simson --> Jupyter Quick Start
6. Erica Degagga --> Landfire Initiatives in the Cloud
7. Tony --> Searching disorganized git repos
8. Neal CoP presentation on using Cloud + Cloud + HPC + AI/ML/DL


## Past Videos

- teams does not make it easy to share for new users
    - past channel is not available
    - test with Simson negative result

- Game of Thrones is 67 hours -- this is less than 20 so far

### K 90daytemp

- k:/90daytemp/butzer/AWS_PANGEO_VIDEOS 

#### Featured Video
K:\90daytemp\butzer\AWS_PANGEO_VIDEOS\2020_12_08_AWS_PANGEO On-boarding with Tony and Neal.mp4


## Pangeo Access

- https://taskmgr.chs.usgs.gov/servicedesk/customer/portal/10/create/251
- https://taskmgr.chs.usgs.gov/servicedesk/customer/portal/10



### Evapo Cartoon
[https://github.com/tonybutzer/et/blob/master/docs/source/00status.md](https://github.com/tonybutzer/et/blob/master/docs/source/00status.md)

- https://github.com/tonybutzer/et/blob/master/docs/source/00status.md

## Class Context

1. Projects that use mutiple modern compute resources
2. CHS AWS development accounts - EC2 elastic, ephemeral computer -- with S3 and git for persistence
3. HPC - especially Tallgrass - cause its availabkle and has GPUs
4. Part of our model family SSEBop is computed/modeled using Google Cloud Platform and GEE
5. GSUTIL and RCLONE featured
6. Refresher on DOCKER and SINGULARITY
7. using pangeo.chs.usgs.gov for displaying ssebop
8. Open Data Cube abstractions BUT with PANGEO for Landsat Albers Scenes

## Demo Overview

1. Look at google cloud bucket assets - ssebop
2. demo how to replicate/sync/copy those to our AWS DataLake
3. demo using docker to build an image for gsutil -- google utility
4. demo running the container on AWS
5. demo running the container/sif on Tallgrass
6. demo looking at the tif file with Pangeo on tallgrass via ssh tunnel of port 8888

---
1. redo Nate's Waubay for albers and rgb
    - composite repo?

- https://console.cloud.google.com/storage/browser/ssebop-modis/Annual
## Rclone Examples

- tony --> umyssh minipangeo

```
 1984  cat Dockerfile
 1985  cat Makefile
 1986  cd
 1987  ls
 1988  rclone config
 1989  ls
 1990  rclone listremotes
 1991  rclone config
 1992  rlone ls sbop:/ssebop-modis/
 1993  rclone ls sbop:/ssebop-modis/
 1994  rclone sync -P sbop:/ssebop-modis/Annual et-data:/dev-et-data/datalake/ssebop-modis/Annual/
 1995  aws s3 ls dev-et-data/datalake/ssebop-modis/Annual/
 1996  aws s3 ls dev-et-data/datalake/ssebop-modis/Annual/ --human
 1997  gdalinfo /vsis3/dev-et-data/datalake/ssebop-modis/Annual/y2003_modisSSEBopETv4_actual_mm.tif
 1998  ls
 1999  ls -l
 2000  rclone listremotes
 2001  rclone ls sbop:/ssebop-modis
 2002  rclone ls sbop:/ssebop-modis --help
 2003  rclone lsjson sbop:/ssebop-modis
 2004  rclone lsjson sbop:/ssebop-modis/Annual
 2005  rclone ls sbop:/ssebop-modis/Annual
 2006  history
```

## ARCPY vs. Open Source


## Databases are so yesterday

## But if you insist on postgres
### I am talking to you OpenDataCube

- THEN - at least use docker to minimize the PAIN!

```
ubuntu@ip-10-12-68-246:/opt/cube-in-a-box$ more docker-compose.yml
version: '3'

services:
  postgres:
    image: postgis/postgis:10-2.5
    environment:
      - POSTGRES_DB=opendatacube
      - POSTGRES_PASSWORD=opendatacubepassword
      - POSTGRES_USER=opendatacube
    ports:
      - 5432:5432
    restart: always

  jupyter:
    build: .
    environment:
      - DB_HOSTNAME=postgres
      - DB_USERNAME=opendatacube
      - DB_PASSWORD=opendatacubepassword
      - DB_DATABASE=opendatacube
      - AWS_NO_SIGN_REQUEST=true
      - STAC_API_URL=https://earth-search.aws.element84.com/v0/
    ports:
      - "8080:8888"
    volumes:
      - ./notebooks:/notebooks
    restart: always
    command: jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='secretpassword'
```

## What does a world class data center look like?

1. lean and agile
2. Highly TRAINED
3. communicates across informal channels
4. Common Goal - effective use of the planet's limited resources - 
5. A world or universe view
6. fosters the right CULTURE
    - sharing and confidence
    - respects each other's expertise
    - has each other's back
    - has fun at work
    - rejects management styles that don't inspire

## These classes propose PANGEO as a way for science
- Open Data Cube - is an instance of PANGEO
    - its database for me represents a barrier to entry
    - that said its a cool and powerful abstraction for building xarray timeseries applications that run in Pangeos
## Sandbox

## Prototyping Phase

### Goals/Characteristics

1. Must allow nonUSGS Collaboration
2. Be affordable
3. Be Easy to use
4. Allow access to data bucket `dev-et-data`
5. Easy to slurp/clone github repos
	- VegET repo here

## USER TL;DR

## NEW USGS CHS SANDBOX
## http://TBD

## What about the big pangeo


### Technical Stack

1. uses TLJH - fairly nice for this purpose

# Week 18 HLS from S3 Aaron Friesz

### Science without the suffering
### Data without the dukkha
### Manifestations without the maya


## Aaron Friesz
    - LP DAAC
    - Works with the USGS and NASA
    - Develops Science Outreach Programs
    - Cole K. is one of his colleagues in crime

## Future Classes
    - May 4th -- Fire applications made easy by Pangeo in AWS -- tony
    - May 11th -- musings in change detection notebooks Kelcy Smith
    - May 17th - Erica Degaga - How we approach Explainable AI - XAI
        - Tensorflow, Sagemaker, Tools and Techniques - Tesnsorflow demo in the bigPangeo

## Hackathon, Problem Solving
    - Some Examples :
    - Update from Devandra
        - UTM to Albers to Merging of cross zone tiles - Sujan
    - Dealing with HDF4 until there are COGs
    - Zonal stats - be careful with some of the libraries - to be continued ...

## "COGs good!" - says OG (the caveman).
![](https://kokoalberti.com/articles/geotiff-compression-optimization-guide/tiled_vs_stripped.png)



## Campfire Anyone?

![](https://www.inforum.com/incoming/6976312-fkwbls-47-badlands-images.jpeg/alternates/BASE_FREE/47%20badlands%20images.jpeg)


### Past Pangeo Videos Here

- K:\90daytemp\butzer\AWS_PANGEO_VIDEOS

### In other news - don't get your NADs mixed up

Subject: REGISTER for 2021 Geospatial Summit, NGS/NOAA - May 4-5 - status for replacement of NAD 83 & NAVD 88 in 2022 
 
To all --

The National Geodetic Survey/NOAA plans to replace the North American Datum of 1983 (NAD 83) and the North American Vertical Datum of 1988 (NAVD 88) as part of modernizing the National Spatial Reference System (NSRS).


The purpose of the Geospatial Summit is to learn about the status and schedule for replacement of NAD 83 and NAVD 88, and the impact the transition to the modernized NSRS will have on USGS georeferenced products.


Below is a link to a draft agenda and to documents for background information.



# Week 19 Fire Science with Landsat Albers Scenes


## Two demo Notebooks

### Aaron Friesz - Lake Isabella Fire 2016 Animations

- Start with git
- Pangeo
- STAC and COGS
- Albers Scenes
- Pandas DataFrames
- Xarray eco-system

#### Benefits of these quick collaborations

- found several areas of improvement
    - implement measurement filtering
    - improve xarray attribute description
    - found a bug in the scale factor and offset in the xarray
    - "the biggest room in the house should be the room for improvement" - John Thune


### This class will evolve to a series of independent small labs and a class sylabus. - with luck and effort :-)


### Tony Butzer

- Teddy Roosevelt
- How do you get to true color with R G and B




## Future Classes

### Next week May 11 - Kelcy Smith - Dask and Land Change Detection

- Tony will be out of the office for the next class - Pat and Kelcy to run the session


## Class Moving to Mondays at Noon


### Composites

- This week was a quick detour into Fires with Albers Landsat Scenes
- In two weeks we will look at time series and composites in Maine
