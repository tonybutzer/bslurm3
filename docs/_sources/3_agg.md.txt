# DataOps Cookbook
## Data - ET Case Study 
- more to come ...

## Current Input data to the VegET model

## Detailed Input Description from Steffi

### Precipitation
___

**Gridmet precipitation**  
<br> gridMET is a dataset of daily high-spatial resolution (~4-km, 1/24th degree) surface meteorological data covering the contiguous US from 1979-yesterday.
+ http://www.climatologylab.org/gridmet.html
+ The format is in netcdf4 format and is updated daily with a 4-5 day delay.







### Potential ET
___

**Gridmet potential ET (PET)** 
<br> gridMET is a dataset of daily high-spatial resolution (~4-km, 1/24th degree) surface meteorological data covering the contiguous US from 1979-yesterday.
+ http://www.climatologylab.org/gridmet.html
+ The format is in netcdf4 format and is updated daily with a 4-5 day delay.



### Average air temperature
___

**Worldmet temperature** --> Daymet data for North America
<br> The Daymet dataset provides gridded estimates of daily weather parameters. Seven surface weather parameters are available at a daily time step, 1 km x 1 km spatial resolution, with a North American spatial extent. Access to the Daymet dataset is available from the ORNL DAAC through a variety of tools and formats allowing a rich resource of daily surface meteorology.
Daymet is supported by NASA through the Earth Science Data and Information System(ESDIS).
+ https://daymet.ornl.gov/
+ The data is updated once a year at the beginning of the calendar year.
+ netCDF file format that follow netCDF Climate and Forecast (CF) Metadata conventions


**Future use - Gridmet air temperature** 
<br> gridMET is a dataset of daily high-spatial resolution (~4-km, 1/24th degree) surface meteorological data covering the contiguous US from 1979-yesterday.
+ http://www.climatologylab.org/gridmet.html
+ The format is in netcdf4 format and is updated daily.


### NDVI - Normalized Difference Vegetation Index
___

**MODIS product MOD13Q1 - 1km**
<br> The MOD13Q1 Version 6 product provides Vegetation Index (VI) values at a per pixel basis at 250 meter (m) spatial resolution. There are two primary vegetation layers. The first is the Normalized Difference Vegetation Index (NDVI), which is referred to as the continuity index to the existing National Oceanic and Atmospheric Administration-Advanced Very High Resolution Radiometer (NOAA-AVHRR) derived NDVI.https://lpdaac.usgs.gov/products/mod13q1v006/
+ https://e4ftl01.cr.usgs.gov/MOLT/MOD13Q1.006/ what is the NASA Land Processes Distributed Active Archive Center (LP DAAC) Distribution Server hosted at the USGS Earth Resources Observation and Science (EROS) Center.
+ the format is hdf
+ the data is updated every 8-days, 2-5 days after an eight day period is completed
<br> Alternative is NDVI at 1km scale (https://lpdaac.usgs.gov/products/mod13a2v006/). The same properties apply.


**Possible Landsat 8 for NDVI calculation on the fly?**



### Soil Properties
___

**SoilGrids**
SoilGrids is a system for global digital soil mapping that uses state-of-the-art machine learning methods to map the spatial distribution of soil properties across the globe.
+ https://www.isric.org/explore/soilgrids
+ Those are static datasets for the globe


**U.S. soil data (gNATSGO)**
<br> The gridded National Soil Survey Geographic Database (gNATSGO) is a USDA-NRCS Soil & Plant Science Division (SPSD) composite database that provides complete coverage of the best available soils information for all areas of the United States and Island Territories. It was created by combining data from the Soil Survey Geographic Database (SSURGO), State Soil Geographic Database (STATSGO2), and Raster Soil Survey Databases (RSS) into a single seamless ESRI file geodatabase. The gNATSGO database contains a 10-meter raster of the soil map units and 70 related tables of soil properties and interpretations. It is designed to work with the SPSD gSSURGO ArcTools. Users can create full coverage thematic maps and grids of soil properties and interpretations for large geographic areas, such as the extent of a State or the conterminous United States.
https://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/survey/geo/?cid=NRCSEPRD1464625
+ the data is in a file geodatabase originally
+ processing required to get the data needed - output are geotiff files



### Data on AWS

#### Available data on AWS
+ Landsat 8  -  NDVI calculation? not ideal(yet)
+ NEXRAD precipitation  -  its daily data, updated daily. We have a python script running downloading NEXRAD data everyday
+ GOES 16 and 17  - 
+ NASA NEX - includes MOD13Q1(250m)
+ MODIS MYD13A1, MOD13A1, MYD11A1, MOD11A1, MCD43A4  -  NDVI 500m
+ ECMWF ERA5 Reanalysis - possible air temperature source?  https://github.com/planet-os/notebooks/blob/master/aws/era5-pds.md

#### Missing data on AWS

+ potential ET data
<br> We could use our own creation of climatology dataset!!
<br> ETo dataset, daily 1984-2017 - 366 files = 1.23 GB

+ air temperature
<br> air temp to be discussed

+ soil data



## Questions

1. Landsat data is the big gorilla in the room.
	- Collection-2 is relevant?
		- Which Bands?
			- Surface Temperature?
			- Surface Reflectance?
			- Aerosols?
	- ANSWER - Not yet except for some possible animations for show of AOI
	- LATER - ET will explore bands in Collection-2 in a merged ET product - SSEBop and VegET and Landsat - TBD
2. 

## Assumptions

1. Direct access to data in object buckets is useful
2. Xarray abstractions will provide the right slicing methods to leverage the ET time series information
3. Spelling is not important in this website :-)
4. 

## What Data is in the "CLOUD" ?

## Where 

## How


## Notes

https://explorer.digitalearth.africa/ga_ls8c_gm_2_annual


## AWS Registry
https://aws.amazon.com/earth/


## More Portals and Buckets

- look at the nasa catalogs and portals
- Earth Explorer
- Sentinel Hub

- list from MacKenzie F - place in notes for now

- find chris holmes talk on death of the portal

## LPDAAC

![lpdaac](https://github.com/tonybutzer/assets/blob/master/et/lpdaac_data.png?raw=true)


## The Keystone Product MODIS 250m NDVI 16 Day Sinusoidal Tiles.

### MOD13Q1 v6

![](https://github.com/tonybutzer/assets/blob/master/et/great-skew.jpg?raw=true)


---

![](https://github.com/tonybutzer/assets/blob/master/et/imgo.jpg?raw=true)

## Data Wrangle

## rclone is THE BOMB!

`rclone copy MODIS_NDVI/ et-data:/ga-et-data/MODIS_NDVI/  -P`

```
tony@qotom ~ $ rclone copy MODIS_NDVI/ et-data:/ga-et-data/MODIS_NDVI/  -P 
Transferred:   	   43.191G / 46.937 GBytes, 92%, 1.255 MBytes/s, ETA 50m56s
Transferred:         1009 / 1099, 92%
Elapsed time:   9h47m18.8s
Transferring:
 *            2016/2016335.1_km_16_days_NDVI.tif: 91% /131.284M, 66.102k/s, 2m51s
Transferred:   	   43.241G / 46.937 GBytes, 92%, 1.255 MBytes/s, ETA 50m15s
Transferred:         1009 / 1099, 92%
Elapsed time:   9h47m59.3s
Transferring:
 *            2016/2016335.1_km_16_days_NDVI.tif: 95% /131.284M, 106.963k/s, 1m0s
Transferred:   	   43.959G / 46.937 GBytes, 94%, 1.255 MBytes/s, ETA 40m29s
Transferred:         1033 / 1099, 94%
Elapsed time:   9h57m47.3s
Transferring:
 *            2016/2016343.1_km_16_days_NDVI.tif: 27% /131.284M, 296.605k/s, 5m29s
 *            2016/2016344.1_km_16_days_NDVI.tif: 22% /131.284M, 312.016k/s, 5m32s
 *            2016/2016345.1_km_16_days_NDVI.tif: 19% /131.284M, 281.528k/s, 6m22s
 *            2016/2016346.1_km_16_days_NDVI.tif: 17% /131.284M, 405.909k/s, 4m33s

```

## Using the NETAPP

1. docker container on llsrlscd04
2. rclone container
3. docker exec -it rclone bash
4. su butzer

```
rclone copy /mnt/Projects/Cloud_Veg_ET/Data/ETO/ et-data:/ga-et-data/Cloud_Veg_ET/Data/ETO/ -P

rclone copy /mnt/Projects/Cloud_Veg_ET/Data/NDVI et-data:/ga-et-data/Cloud_Veg_ET/Data/NDVI -P

PPT
```

rclone copy et-data:ga-et-data/v1DRB_outputs/model_outputs/ /mnt/Projects/Cloud_Veg_ET/fromtony/ -P

### Notes

### Air Temperature

*./push-scp-ga.sh air_temperature*:

loading from local disk to cloud EBS

```
Mon, Feb 24, 2020  1:19:16 PM

Mon, Feb 24, 2020  2:51:21 PM

```

4.6 Gigabytes in an hour an a half - thru the VPN and TIC.

- more to come ....


### Sync to Bucket

- make a inputsv0 prefix

`aws s3api put-object --bucket ga-et-data-west --key inputsv0/ `


### Actual Sync

#### Dry run

```  aws s3 sync ./air_temperature s3://ga-et-data-west/inputsv0/air_temperature --dryrun ```

#### For Reals

```  time aws s3 sync ./air_temperature s3://ga-et-data-west/inputsv0/air_temperature ```

```
real    1m44.966s
user    0m39.020s
sys     0m23.729s
```

what took *an hour and a half* - can be done in *1 minute and a half*

- that's the cloud - its awesome - S3 is powerful
- and everyone can access the same buckets directly - think about it and *smile* :-)


### Nuke prefix

``` aws s3 rm --recursive  s3://ga-et-data-west/inputsv0/ --dryrun```

### Precipitation


```  aws s3 sync ./precipitation s3://ga-et-data-west/inputsv0/precipitation --dryrun ```

#### For Reals

```  time aws s3 sync ./precipitation s3://ga-et-data-west/inputsv0/precipitation ```

```
real    2m43.137s
user    0m33.461s
sys     0m7.885s
```

### Git Issue?

# Data Science Cookbook

https://discourse.holoviz.org/t/simple-panel-example-of-map-time-series-interaction-for-data-cube/1485/2

https://github.com/tonybutzer/notebook

https://github.com/tonybutzer/notebook/blob/master/00-Viz/panel-timeseries-get-x-y-and-plot.ipynb
