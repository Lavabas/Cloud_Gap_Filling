# Cloud Gap Filling in Satellite Time Series Using Xee and Earth Engine: A Python-Based Approach

## Overview
Cloud contamination is a major challenge in using optical satellite imagery, especially in tropical regions like Sri Lanka where frequent cloud cover limits the availability of clear observations. These gaps pose a significant barrier to time-series analysis, which is critical for understanding land surface dynamics and environmental trends.

This project demonstrates a robust pipeline for cloud and shadow gap filling using the Xee Python API and Google Earth Engine (GEE). The method includes:
1. Accessing cloud-prone datasets (e.g., NDVI)
2. Applying pixel-level cloud and shadow masking
3. Filling missing values with temporal smoothing (e.g., rolling mean)

Although NDVI is used here as an example, the approach is adaptable to various Earth observation datasets such as temperature, precipitation, or land surface reflectance. The workflow is demonstrated over Northern Sri Lanka and the entire country, but can be applied globally.

## 1. Applied for Northern Region
### Cloud-Affected NDVI Time Series – January 2020 
<img width="2233" height="1190" alt="image" src="https://github.com/user-attachments/assets/69b20c4e-160c-4e2c-a980-3c918463a7d8" />

### Cloud-Filled NDVI Time Series – January 2020 
<img width="2233" height="1190" alt="image" src="https://github.com/user-attachments/assets/c8f192cd-3b91-42d0-a1a6-8e12ef55b6bc" />

## 2. Applied for Sri Lanka
### Cloud-Affected NDVI Time Series – January 2020
<img width="2244" height="1190" alt="srilanka-before-cloudfilling" src="https://github.com/user-attachments/assets/c48c286f-7024-4e12-8ba3-1d373bbd2c2c" />

### Cloud-Filled NDVI Time Series – January 2020 
<img width="2244" height="1190" alt="Srilanka-after-cloudfilling" src="https://github.com/user-attachments/assets/0664d04e-3cb8-49a2-8ccc-ccfc35386b6a" />

### NDVI Time Series for selected point in Jaffna  (Before Filling)
<img width="575" height="455" alt="image" src="https://github.com/user-attachments/assets/332ab263-a7f2-44b0-b9e2-c640ec389730" />

### NDVI Time Series for selected point in Jaffna  (After Filling)
<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/4c63e9dd-4a45-4173-b407-ae49593747f6" />

## Results
- NDVI maps show improved spatial completeness after gap filling
- Time series plots demonstrate smoothed curves and reduced artifacts
- By restoring temporal continuity in satellite-derived indicators, this technique enables more reliable analysis in domains such as: Agriculture and crop monitoring, Drought and flood impact assessment, Vegetation health and land degradation, and Water resource management and irrigation planning





