---
title: "Access 120 Petabytes of NASA Data Directly in QGIS"
date: 2026-01-06
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A step-by-step tutorial on using the NASA Earthdata QGIS plugin to search, preview, and download satellite imagery and geospatial datasets from NASA's archive without programming.
thumbnail: https://img.youtube.com/vi/H78l-3nbPfk/maxresdefault.jpg
tags:
  - QGIS
  - NASA
  - Satellite Imagery
  - Remote Sensing
  - Open Data
keywords:
  - NASA Earthdata
  - QGIS Plugin
  - Satellite Data
  - Landsat
  - Remote Sensing
  - Data Download
---

# Access 120 Petabytes of NASA Data Directly in QGIS

NASA's Earthdata archive hosts over 120 petabytes of satellite imagery and geospatial datasets spanning multiple decades. Traditionally, accessing this data has required navigating complex web portals or writing code to query NASA's APIs. The [NASA Earthdata QGIS plugin](https://github.com/opengeos/qgis-nasa-earthdata-plugin) changes that by letting you search, filter, preview, and download NASA datasets directly inside QGIS, no programming needed.

In this tutorial, I walk through installing the plugin, setting up authentication, searching for datasets by keyword and area of interest, previewing Cloud Optimized GeoTIFF imagery on the map, and downloading data to your computer.

:::{iframe} https://www.youtube.com/embed/H78l-3nbPfk
:width: 100%
Video tutorial: NASA Earthdata Plugin for QGIS
:::

## What You Will Need

- [QGIS](https://qgis.org) installed via [Pixi](https://pixi.sh) (follow the plugin's [installation instructions](https://github.com/opengeos/qgis-nasa-earthdata-plugin) rather than using your existing QGIS installation, since the plugin requires the `earthaccess` Python package)
- A [NASA Earthdata](https://urs.earthdata.nasa.gov) account (free registration)

## How This Differs from the Earth Engine Plugin

I also released the [GEE Data Catalogs plugin](./gee-time-series) for accessing Google Earth Engine data. The two plugins serve different purposes:

- **Earth Engine Data Catalogs**: Access over 80 petabytes of standardized data. You can load imagery directly onto the map and run computations. Best for datasets that are already in the Earth Engine catalog.
- **NASA Earthdata**: Access over 120 petabytes from NASA's archive. Data formats vary widely, so some datasets can be visualized directly (Cloud Optimized GeoTIFF) while others need to be downloaded first. Best for datasets not available through Earth Engine.

## Install the Plugin

### Set up the environment with Pixi

The plugin requires the `earthaccess` Python package for NASA authentication, which has dependencies that may conflict with a standard QGIS installation. Using Pixi ensures a clean environment:

```bash
pixi init geo
cd geo
pixi add qgis geopandas
```

Wait for the dependencies to install, then launch QGIS:

```bash
pixi run qgis
```

### Install from the Plugin Manager

1. Go to **Plugins > Manage and Install Plugins**.
2. Search for **NASA Earthdata**.
3. Click **Install Plugin**.
4. After installation, go to **NASA Earthdata > Check for Updates** to get the latest version from GitHub.
5. Restart QGIS after updating.

## Set Up Authentication

You need a NASA Earthdata account to search and download data:

1. Register at [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov) if you do not have an account.
2. In QGIS, click the **NASA Earthdata Settings** button in the toolbar (or go to **NASA Earthdata > Settings**).
3. Enter your username and password.
4. Click **Test Credentials** to verify.
5. Click **Save** to store the credentials in a `.netrc` file in your home directory. You only need to do this once.

When the settings panel shows a green indicator next to the `.netrc` file path, authentication is configured correctly.

## Search for Datasets

1. Click the **NASA Earthdata** button in the toolbar to open the plugin panel.
2. Enter a keyword in the search box (e.g., "harmonized landsat" or "above ground biomass").
3. The dropdown list filters to show matching datasets. NASA's catalog contains tens of thousands of datasets, so keywords help narrow the results quickly.
4. Select a dataset from the list.

### Define the area of interest

- Zoom to your area of interest on the map.
- Click **Use Map Extent** to set the search bounds to the current map view.

### Set the date range

- Specify start and end dates. For example, January 2025 to January 2026 for the most recent year of data.

### Advanced options

Expand **Advanced Options** to add filters based on dataset properties. For example:

- Set **Cloud Cover** maximum to 10% to exclude cloudy scenes.
- Add custom property filters if you know the specific attribute names for your dataset.

### Run the search

Click **Search**. The plugin retrieves matching granules and displays their footprints on the map. A results table shows metadata for each item.

## Preview Data on the Map

For datasets stored as Cloud Optimized GeoTIFF (COG), you can preview individual bands directly on the map without downloading:

1. Select a granule from the results list.
2. Choose a band from the dropdown (e.g., Band 5 for near-infrared).
3. Click **Display COG**.

The imagery loads on demand from NASA's cloud storage. It may take a few seconds compared to tile-based services like Earth Engine, since it streams the COG directly. You can zoom in to see higher-resolution data as it loads progressively.

Not all datasets support direct visualization. Datasets in formats other than COG (such as HDF5 or NetCDF) need to be downloaded before they can be viewed.

## Download Data

To download data to your computer:

1. Select one or more granules from the results, or leave the selection empty to download all results.
2. Click **Download**.
3. Choose an output directory.

The plugin downloads all files for each granule automatically. For datasets like Harmonized Landsat Sentinel-2, each granule contains multiple band files (15 bands), all of which are downloaded together. A progress dialog shows the download status.

Once downloaded, you can drag the GeoTIFF files into QGIS to add them to the map.

## Explore NASA's Data Catalog

If you want to browse what is available before using the plugin, visit [earthdata.nasa.gov](https://earthdata.nasa.gov) and explore the data catalog. You can filter by:

- Data format (Cloud Optimized GeoTIFF, HDF5, NetCDF, etc.)
- Spatial coverage
- Temporal range
- Processing level

The keywords and dataset names you find on the website work the same way in the plugin's search box.

## Resources

- **QGIS Plugin Page**: [plugins.qgis.org/plugins/nasa_earthdata](https://plugins.qgis.org/plugins/nasa_earthdata)
- **GitHub Repository**: [github.com/opengeos/qgis-nasa-earthdata-plugin](https://github.com/opengeos/qgis-nasa-earthdata-plugin)
- **NASA Earthdata**: [earthdata.nasa.gov](https://earthdata.nasa.gov)

This plugin makes NASA's vast data archive accessible to anyone with QGIS, whether you are searching for satellite imagery, LiDAR data, biomass estimates, or any other dataset in the catalog. Feel free to open an issue on the [GitHub repository](https://github.com/opengeos/qgis-nasa-earthdata-plugin) if you run into any problems or have feature requests.
