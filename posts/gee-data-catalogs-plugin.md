---
title: "Unlock 80+ Petabytes of Earth Engine Data in QGIS with Zero Coding"
date: 2026-01-03
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: Introducing the GEE Data Catalogs Plugin for QGIS, providing access to over 5,000 datasets from the official Earth Engine catalog and the Awesome GEE Community Catalog with no coding required.
thumbnail: https://img.youtube.com/vi/nZ3D6wLKJQw/maxresdefault.jpg
tags:
  - QGIS
  - Google Earth Engine
  - Remote Sensing
  - Open Source
  - Satellite Imagery
keywords:
  - Google Earth Engine
  - QGIS Plugin
  - GEE Data Catalog
  - Awesome GEE Community Catalog
  - Satellite Imagery
  - Geospatial Data
---

# Unlock 80+ Petabytes of Earth Engine Data in QGIS with Zero Coding

Happy New Year! As my first project of 2026, I am sharing what might be one of the most powerful QGIS plugins I have built so far. The [GEE Data Catalogs Plugin](https://github.com/opengeos/qgis-gee-data-catalogs-plugin) makes it incredibly easy to explore the official [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets) (780+ datasets) and the [Awesome GEE Community Catalog](https://gee-community-catalog.org) (4,300+ datasets) directly inside QGIS, totaling over 5,000 datasets and 80+ petabytes of data.

With just a few clicks, you can browse datasets, visualize them on the map, generate satellite time series, export data to your computer, inspect pixel values, and even convert Earth Engine JavaScript code to Python, all without writing a single line of code.

:::{iframe} https://www.youtube.com/embed/nZ3D6wLKJQw
:width: 100%
Video tutorial: GEE Data Catalogs Plugin for QGIS
:::

## What You Will Need

- [QGIS](https://qgis.org) installed via [Pixi](https://pixi.sh) (do not use your existing QGIS installation due to dependency requirements)
- A [Google Earth Engine](https://earthengine.google.com) account (free for research and education)
- Optionally, the [LeafMap](https://plugins.qgis.org/plugins/leafmap/) QGIS plugin for layer transparency and swipe tools

## Set Up the Environment

### Install Pixi and create a project

```bash
pixi init geo
cd geo
pixi add qgis geemap xee rioxarray geopandas
```

### Authenticate Google Earth Engine

```bash
pixi run earthengine authenticate
```

This opens a browser tab for Google authentication. The credential is saved locally and typically lasts about a week before re-authentication is needed.

### Launch QGIS

```bash
pixi run qgis
```

## Install the Plugin

1. Go to **Plugins > Manage and Install Plugins**.
2. Search for **Earth Engine Data Catalog**.
3. Click **Install Plugin**.
4. Go to **GEE Data Catalogs > Check for Updates** to get the latest version from GitHub (the official repository may lag behind by a few days).
5. Restart QGIS after updating.

I also recommend installing the **LeafMap** plugin for layer transparency and swipe tools.

## Initialize Earth Engine

Before using the plugin, you need to initialize Earth Engine with your project ID:

1. Click the **GEE Data Catalogs Settings** button in the toolbar.
2. Enter your Google Earth Engine project ID (find it at [code.earthengine.google.com](https://code.earthengine.google.com) under your profile).
3. Click **Save Settings**, then **Initialize Earth Engine**.
4. A green confirmation message indicates success.

If you encounter errors, open the QGIS Python console and run:

```python
import ee
ee.Authenticate()
ee.Initialize(project="your-project-id")
```

## Browse and Load Datasets

The plugin opens a panel on the right side of QGIS with multiple tabs for different workflows.

### Browse tab

The browse tab lists all 5,000+ datasets. You can filter by source:

- **All**: Both official and community datasets
- **Official**: The 780+ datasets in Google's official catalog
- **Community**: The 4,300+ datasets from the Awesome GEE Community Catalog

Click any dataset to see a preview at the bottom of the panel, including the dataset ID, provider, date range, and a link to the full documentation page.

To load a dataset onto the map, simply **double-click** it. The imagery appears on the map within seconds, streamed directly from Earth Engine without downloading anything.

### Search tab

If you know what you are looking for, use the search tab to filter by keyword. Type a term like "land cover" or "elevation" and the list updates to show matching datasets. Select a dataset and click **Add to Map** or **Config and Add** for more control over visualization parameters.

## Inspect Data

The **Inspector** tab works like the Earth Engine Code Editor's inspector:

1. Click **Inspector** and then click anywhere on the map.
2. The panel shows pixel values for all loaded raster layers and attribute values for vector layers (feature collections).

This is useful for quickly checking data values without writing any code.

## Load Individual Images from a Collection

For image collections like Harmonized Landsat Sentinel-2, you often want specific images rather than the entire collection:

1. Search for your dataset (e.g., "harmonized landsat").
2. Click **Config and Add** to open the load tab with full configuration options.
3. Set the **date range** (e.g., December 2025).
4. Enable **cloud cover filter** (e.g., less than 5%).
5. Define the **area of interest** using the map extent or by drawing a bounding box.
6. Select **Individual Images** mode and set a limit (e.g., 10 images).
7. Click **Fetch Available Images**.

The plugin returns a list of matching images. Select any image to preview its bands, then click **Load Dataset** to add it to the map. Specify band combinations (e.g., B5, B4, B3 for false color) and min/max values for proper visualization.

## Create Time Series

One of the most powerful features is generating composite time series for any image collection:

1. Search for and select a dataset.
2. Click the **Time Series** button at the bottom.
3. Configure:
   - **Date range**: e.g., January 1, 2025 to December 31, 2025
   - **Cloud cover**: e.g., less than 10%
   - **Area of interest**: draw a bounding box on the map
   - **Temporal frequency**: monthly, quarterly, or yearly
   - **Reducer**: median (good for cloud removal), mean, or maximum (for peak vegetation)
   - **Visualization**: band combination and value range
4. Click **Preview Info** to see how many images match (e.g., 89 images, 12 time steps).
5. Click **Create Time Series**.

The time series generates in seconds. A **time slider** appears at the bottom of the map, letting you navigate through each time step. Each frame is loaded on the fly from Earth Engine. You can also click the play button to animate through the series.

## Export Data

The **Export** tab lets you download data to your local computer:

### Raster export

1. Select the data layer to export.
2. Define the extent (map extent or drawn bounding box).
3. Set the resolution (e.g., 30 m for Landsat).
4. Choose the coordinate system (default: EPSG:3857).
5. Click **Export**.

The plugin uses [xee](https://github.com/google/Xee) under the hood, which handles larger exports than the standard Earth Engine JavaScript API allows. Exported files are Cloud Optimized GeoTIFF.

### Vector export

For feature collections (e.g., country boundaries):

1. Select the vector layer.
2. Define the extent to export a subset, or leave it for the full dataset.
3. Choose the output format (GeoPackage, GeoJSON, Shapefile, etc.).
4. Click **Export**.

## Convert JavaScript to Python

The **Conversion** tab converts Earth Engine JavaScript code to Python automatically:

1. Copy any JavaScript snippet from the [Earth Engine Code Editor](https://code.earthengine.google.com) or documentation.
2. Paste it in the conversion tab.
3. Click **Convert to Python**.
4. The converted code appears using [geemap](https://geemap.org) syntax.
5. Click **Run** to execute it and add the results to the map.

This is especially useful for datasets that only provide JavaScript examples in their documentation.

## Run Custom Python Code

The **Code** tab provides a Python console where you can run any Earth Engine Python code using geemap. Every time you load a dataset through the GUI, the corresponding Python code is automatically copied to your clipboard, so you can paste it into a notebook or script for reproducible workflows.

## Resources

- **QGIS Plugin Page**: [plugins.qgis.org/plugins/gee_data_catalogs](https://plugins.qgis.org/plugins/gee_data_catalogs)
- **GitHub Repository**: [github.com/opengeos/qgis-gee-data-catalogs-plugin](https://github.com/opengeos/qgis-gee-data-catalogs-plugin)
- **Earth Engine Data Catalog**: [developers.google.com/earth-engine/datasets](https://developers.google.com/earth-engine/datasets)
- **Awesome GEE Community Catalog**: [gee-community-catalog.org](https://gee-community-catalog.org)

This plugin puts over 80 petabytes of geospatial data at your fingertips without requiring any programming knowledge. Whether you are exploring land cover changes, creating satellite time series, or downloading data for local analysis, everything happens inside QGIS with a few clicks. If you find it useful, please give it an upvote on the [QGIS plugin page](https://plugins.qgis.org/plugins/gee_data_catalogs). Feel free to open an issue or feature request on the [GitHub repository](https://github.com/opengeos/qgis-gee-data-catalogs-plugin) if you run into any problems.
