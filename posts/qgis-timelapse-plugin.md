---
title: "Create Satellite Timelapse Animations in QGIS with Google Earth Engine"
date: 2025-12-27
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A step-by-step tutorial on using the QGIS Timelapse Plugin to create animated GIF and MP4 timelapse videos from Landsat, Sentinel, MODIS, GOES, and NAIP imagery powered by Google Earth Engine.
thumbnail: https://img.youtube.com/vi/D_nkIL1JVU8/maxresdefault.jpg
tags:
  - QGIS
  - Google Earth Engine
  - Timelapse
  - Remote Sensing
  - Animation
keywords:
  - QGIS Timelapse
  - Google Earth Engine
  - Landsat
  - Sentinel-2
  - MODIS NDVI
  - GOES
  - Satellite Animation
---

# Create Satellite Timelapse Animations in QGIS with Google Earth Engine

Satellite timelapse animations are a powerful way to visualize environmental change, from urban expansion and deforestation to river dynamics and weather events. The [QGIS Timelapse Plugin](https://github.com/opengeos/qgis-timelapse-plugin) lets you create these animations for any location on Earth with just a few clicks, powered by Google Earth Engine's cloud computing. You draw a rectangle, choose a satellite, set the time range, and the plugin handles all the data processing, mosaicking, and animation generation without downloading any raw data.

In this tutorial, I walk through setting up the plugin and creating timelapse animations using Landsat, MODIS NDVI, and GOES weather satellite imagery.

:::{iframe} https://www.youtube.com/embed/D_nkIL1JVU8
:width: 100%
Video tutorial: QGIS Timelapse Plugin Tutorial
:::

## What You Will Need

- [QGIS](https://qgis.org) installed via [Pixi](https://pixi.sh)
- A [Google Earth Engine](https://earthengine.google.com) account
- Your Google Cloud project ID

## Set Up the Environment

### Install Pixi and create a project

```bash
pixi init geo
cd geo
pixi add qgis geemap earthengine-api pillow ffmpeg
```

The `pillow` package is needed for GIF generation and `ffmpeg` for MP4 conversion.

### Authenticate Google Earth Engine

```bash
pixi run earthengine authenticate
```

### Launch QGIS

```bash
pixi run qgis
```

## Install the Plugin

1. Go to **Plugins > Manage and Install Plugins**.
2. Go to **Settings** and add the custom repository URL from the [plugin page](https://github.com/opengeos/qgis-timelapse-plugin).
3. Search for **timelapse** and click **Install Plugin**.
4. The timelapse icon (a play button) appears in the toolbar and a **Timelapse** menu appears in the menu bar.

Use **Timelapse > Check for Updates** to get the latest version from GitHub.

## Supported Satellites

The plugin supports six satellite data sources:

- **Landsat**: 30 m resolution, global coverage from 1984 to present. Best for long-term change analysis.
- **Sentinel-2**: 10 m resolution, global coverage from 2015 to present. Higher spatial detail than Landsat.
- **Sentinel-1**: SAR imagery, not affected by clouds. Useful for all-weather monitoring.
- **MODIS NDVI**: 250 m resolution, global coverage from 2000 to present. Best for continental-scale vegetation monitoring.
- **GOES**: Geostationary weather satellite with imagery every few minutes. Best for monitoring weather events like hurricanes and volcanic eruptions.
- **NAIP**: Sub-meter aerial imagery for the United States only.

## Create a Landsat Timelapse

### Define the area of interest

1. Click the **Timelapse** icon in the toolbar.
2. In the **AOI** tab, either click **Use Map Extent** or click **Draw Bounding Box** and draw a rectangle on the map.
3. If your Earth Engine project ID is not set as an environment variable, enter it in the project ID field.

### Configure the imagery

1. Go to the **Imagery** tab.
2. Select **Landsat**.
3. Set the year range (e.g., 1984 to 2025 for the full Landsat archive).
4. Set the season (e.g., March to October to focus on snow-free months).
5. Choose the temporal frequency:
   - **Year**: One composite per year (best for multi-decade change)
   - **Quarter**: Four composites per year
   - **Month**: Monthly composites (keep the year range short to avoid too many frames)
   - **Date**: Individual image dates
6. Select the band combination (e.g., false color composite for highlighting vegetation, or true color for natural appearance).
7. Enable **cloud masking** to remove cloudy pixels from composites.

### Configure the output

1. Go to the **Output** tab.
2. Specify the output file path for the GIF animation.
3. Check **Create MP4** to also generate an MP4 video (requires ffmpeg).
4. Customize the title text, text color, font size, and progress bar appearance.

### Generate the animation

Click **Create Timelapse**. The plugin processes the data on Google Earth Engine's servers and generates the animation in roughly 30 seconds to a minute. The result plays directly in the QGIS panel.

### Example: Las Vegas Urban Growth

Drawing a rectangle around Las Vegas and creating a yearly Landsat timelapse from 1984 to 2025 produces a striking visualization of urban expansion. The animation clearly shows the city growing outward into the surrounding desert over four decades.

## Create a MODIS NDVI Timelapse

MODIS NDVI timelapses are ideal for visualizing vegetation dynamics at continental scales.

1. Draw a large rectangle (e.g., covering Africa).
2. Select **MODIS** and choose **NDVI** as the index.
3. Set the frequency to **Year**.
4. Click **Create Timelapse**.

The resulting animation shows the seasonal "green wave" of vegetation sweeping north during the northern hemisphere summer and south during winter, driven by rainfall patterns across the continent.

## Create a GOES Weather Timelapse

GOES satellites capture imagery every few minutes, making them ideal for monitoring fast-moving weather events.

1. Zoom to the area where the event occurred.
2. Select **GOES** and choose the appropriate satellite (GOES-16, 17, or 18 depending on the coverage area and time period).
3. Set the date and time range to cover the event. The time is in UTC.
4. Click **Create Timelapse**.

GOES timelapses are useful for visualizing hurricanes, volcanic eruptions, wildfires, and other dynamic atmospheric events. The high temporal frequency produces smooth animations that show cloud movement and storm development in detail.

## Tips

- **Too many frames**: If the plugin returns an error about too much data, reduce the time range, increase the temporal frequency (e.g., yearly instead of monthly), or draw a smaller area.
- **Band combinations**: Experiment with different band combinations. False color composites (e.g., B5, B4, B3 for Landsat) often reveal more detail than true color, especially for vegetation and water features.
- **Cloud masking**: Always enable cloud masking for optical imagery (Landsat, Sentinel-2) to get cleaner composites.
- **Output formats**: The GIF is useful for quick sharing on social media. The MP4 is better for presentations and video editing.

## Resources

- **Plugin Page**: [qgis.gishub.org](https://qgis.gishub.org)
- **GitHub Repository**: [github.com/opengeos/qgis-timelapse-plugin](https://github.com/opengeos/qgis-timelapse-plugin)
- **Google Earth Engine**: [earthengine.google.com](https://earthengine.google.com)

The plugin handles all the complexity of satellite data processing, from filtering and mosaicking to compositing and animation, so you can focus on choosing the right location, time period, and satellite for your story. Try it with your own area of interest and feel free to open an issue on the [GitHub repository](https://github.com/opengeos/qgis-timelapse-plugin) if you have questions or feature requests.
