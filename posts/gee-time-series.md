---
title: "Create Time-Series Satellite Images in Seconds with QGIS"
date: 2026-01-21
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A step-by-step tutorial on creating and downloading time-series satellite imagery using the GEE Data Catalogs Plugin v0.5 for QGIS, with no coding required.
thumbnail: https://img.youtube.com/vi/8IW6XqnUjgg/maxresdefault.jpg
tags:
  - QGIS
  - Google Earth Engine
  - Time Series
  - Remote Sensing
  - Landsat
keywords:
  - QGIS
  - Google Earth Engine
  - Time Series
  - Landsat
  - Sentinel-2
  - Satellite Imagery
---

# Create Time-Series Satellite Images in Seconds with QGIS

The timelapse plugin I covered in a previous tutorial is great for creating GIF animations of landscape change, but animations alone are not enough if you need the original satellite data for analysis. The [GEE Data Catalogs Plugin](https://github.com/opengeos/qgis-gee-data-catalogs-plugin) v0.5 for QGIS solves this by letting you create time-series satellite imagery and download the full-resolution data to your computer, all through a graphical interface with no coding required.

In this tutorial, I walk through how to generate annual Landsat composites for any location on Earth, visualize them with a time slider, compare changes with a swipe tool, and export the imagery to your local machine.

:::{iframe} https://www.youtube.com/embed/8IW6XqnUjgg
:width: 100%
Video tutorial: Create Time-Series Satellite Images in Seconds with QGIS
:::

## What You Will Need

- [QGIS](https://qgis.org) installed via [Pixi](https://pixi.sh) (follow the plugin's [installation instructions](https://github.com/opengeos/qgis-gee-data-catalogs-plugin))
- GEE Data Catalogs Plugin v0.5 or later
- A Google Earth Engine account
- Optionally, the [LeafMap](https://plugins.qgis.org/plugins/leafmap/) QGIS plugin for side-by-side layer comparison with the swipe tool

## Install and Update the Plugin

1. Go to **Plugins > Manage and Install Plugins**.
2. Search for **GEE Data Catalogs** (listed as "Earth Engine Data Catalog").
3. Click **Install Plugin** or **Upgrade Plugin** to get the latest version.
4. Alternatively, go to **GEE Data Catalogs > Check for Updates** to check for and install the latest release from GitHub.
5. Restart QGIS after updating.

I also recommend installing the **LeafMap** plugin from the Plugin Manager. It provides a swipe tool that makes it easy to compare two layers side by side.

## Select a Dataset

1. Click the **GEE Data Catalogs** button in the toolbar to open the plugin panel.
2. Browse the dataset list or go to the **Search** tab to find a specific dataset. The plugin provides access to over 80 petabytes of satellite and geospatial data from Google Earth Engine.
3. For this tutorial, select **Harmonized Landsat and Sentinel-2** (HLS). Two options are available:
   - Landsat 8 and 9 (data from 2013 onward)
   - Sentinel-2 A and B (data from 2015 onward)

Select the Landsat option for a longer time range.

## Configure the Time Series

After selecting a dataset, click the **Time Series** tab at the bottom of the plugin panel. The dataset information is populated automatically.

### Set the date range and filters

- The date range defaults to the full availability of the dataset (e.g., 2013 to present for Landsat).
- Check the **Cloud Cover** filter and set it to less than 20% to exclude cloudy images. This significantly reduces noise in the composites.

### Define the area of interest

- Click **Use Map Extent** to use the current map view, or click the **Draw** button and draw a rectangle on the map.
- Keep the area at a reasonable size. Larger areas require more processing time and produce larger downloads.

### Choose the temporal aggregation

- Select how the imagery should be grouped over time: **yearly**, **monthly**, **quarterly**, etc.
- For long-term change analysis, **yearly** composites work well. Each year's images are combined into a single composite.

### Select the reducer

- The **reducer** determines how multiple images within each time step are combined.
- **Median** is a good default because it effectively removes clouds and outliers.
- Use **Maximum** if you are analyzing vegetation indices and want to capture peak greenness.

### Set the visualization

Specify which bands to display and the value range:

- For a false color composite (which highlights vegetation): bands `B5`, `B4`, `B3` with min `0` and max `0.4`.
- For a true color composite: bands `B4`, `B3`, `B2`.
- You can look up available bands and their descriptions on the dataset's Google Earth Engine page.

### Preview and create

Click **Preview Info** to see how many images match your filters and how many time steps will be generated. For example, 894 matching images across 13 years produces 13 annual composites. Then click **Create Time Series**.

The time series is generated in seconds because the compositing and filtering run on Google Earth Engine's servers.

## Visualize with the Time Slider

Once the time series is created, a time slider appears at the bottom of the map. Use it to navigate through the years:

- Click the **Previous** and **Next** buttons to step through individual time steps.
- Drag the slider to jump to a specific year.
- Each frame is loaded on the fly from Earth Engine, so there may be a brief delay as the imagery renders.

The imagery is served as XYZ tiles at whatever zoom level you are viewing, so you can zoom in to see 30-meter Landsat detail without downloading anything.

## Compare Changes with the Swipe Tool

To compare two specific years side by side:

1. Navigate to the first year (e.g., 2013) and rename the layer to something descriptive (right-click the layer, select **Rename**).
2. Navigate to the last year (e.g., 2025) and rename that layer as well.
3. Open the **LeafMap** plugin and click **Layer Swipe**.
4. Select the two layers (e.g., 2013 on the left, 2025 on the right).
5. Click **Activate Swipe Tool** and drag the divider across the map to compare the two time periods.

This is especially effective for visualizing urban expansion, deforestation, river dynamics, or any other landscape change.

## Export Time Series to Your Computer

The plugin can download the full-resolution imagery to your local machine:

1. In the **Export Time Series** section, set the **resolution** (e.g., 30 meters for Landsat).
2. Check **Export Visualization Bands Only** if you only want the bands you selected for display (e.g., B5, B4, B3). Uncheck it to export all bands (10+ bands for Landsat).
3. Set the **coordinate reference system** (default is EPSG:3857, Web Mercator).
4. Enter a **base file name** (e.g., `landsat`). Each time step gets a separate file.
5. Select an **output directory**.
6. Click **Export**.

The plugin uses [xee](https://github.com/google/Xee) under the hood for downloading, which supports parallel processing and handles large data volumes better than the standard Earth Engine JavaScript export. Each exported file is a GeoTIFF that you can open in QGIS, Python, or any GIS software.

## Reproducible Code

The plugin also generates a Python code snippet for each time series you create. Click the **Code Snippet** button to see the Earth Engine Python code that reproduces your exact workflow. You can copy this code and run it in a Jupyter Notebook for scripted analysis or to share reproducible workflows with collaborators.

## Resources

- **GEE Data Catalogs Plugin**: [github.com/opengeos/qgis-gee-data-catalogs-plugin](https://github.com/opengeos/qgis-gee-data-catalogs-plugin)
- **QGIS Plugin Page**: [plugins.qgis.org/plugins/gee_data_catalogs](https://plugins.qgis.org/plugins/gee_data_catalogs)
- **LeafMap Plugin**: [plugins.qgis.org/plugins/leafmap](https://plugins.qgis.org/plugins/leafmap/)

This plugin works with any dataset in the Google Earth Engine catalog, not just Landsat. Try it with Sentinel-2 for higher spatial resolution (10 meters), MODIS for daily coverage, or any other dataset that fits your application. If you find the plugin useful, please give it an upvote on the [QGIS plugin page](https://plugins.qgis.org/plugins/gee_data_catalogs). Feel free to open an issue or feature request on the [GitHub repository](https://github.com/opengeos/qgis-gee-data-catalogs-plugin) if you run into any problems.
