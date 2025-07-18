# -*- coding: utf-8 -*-
"""Cloud_Gap_Filling-Northern.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10CXg2IWwptEkK0AJ-SVIePkZymD4ywHS
"""

import ee
import geemap
import xarray as xr

!pip install xee
import xee

ee.Authenticate()
ee.Initialize(project = 'ee-lavibas23', opt_url = 'https://earthengine-highvolume.googleapis.com')

map = geemap.Map(basemap = 'SATELLITE')
map

roi = map.draw_last_feature.geometry()
roi

ndvi = ee.ImageCollection("NOAA/CDR/VIIRS/NDVI/V1").select('NDVI', 'QA').filterDate('2020','2021')
ndvi

def cloud_mask(img):
  index = img.select('NDVI').multiply(0.0001)
  qa = img.select('QA')
  cloud = qa.bitwiseAnd(1 << 1).neq(0)
  shadow = qa.bitwiseAnd(1 << 2).neq(0)
  mask = cloud.Or(shadow).Not()
  return index.updateMask(mask).copyProperties(img, img.propertyNames())

ndvi_masked = ndvi.map(cloud_mask)
ndvi_masked

ds = xr.open_dataset(ndvi_masked, engine = 'ee', crs = 'EPSG:4326', scale = 0.005, geometry = roi )

ds

sub = ds.sel(time = ds.time.dt.month == 1)
sub

sub.NDVI.plot(x = 'lon', y = 'lat', col = 'time', col_wrap = 8, robust =True, cmap = 'RdYlGn')

point = ds.sel(lon=80.02, lat=9.68, time = ds.time.dt.month == 1, method ='nearest')

point.NDVI.plot()

rolling = ds.rolling(time = 10, min_periods = 1, center = True).mean()

ds_filled = ds.fillna(rolling)

sub2 = ds_filled.sel(time = ds_filled.time.dt.month == 1)

import matplotlib.pyplot as plt

sub2.NDVI.plot(x = 'lon', y = 'lat', col = 'time', col_wrap = 8, robust = True, cmap = 'RdYlGn')
plt.savefig('ndvi_filled.png', dpi = 360, bbox_inches = 'tight')

point2 = ds_filled.sel(lon=80.02, lat=9.68, time = ds.time.dt.month == 1, method ='nearest')

point2.NDVI.plot()