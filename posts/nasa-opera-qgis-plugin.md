---
title: "Access NASA OPERA Data in QGIS with a Plugin and an AI Agent"
date: 2026-05-05
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: A step-by-step tutorial on installing the NASA OPERA QGIS plugin, searching and visualizing DSWx surface water products, and using an integrated AI agent to analyze flood events with natural language and voice commands.
thumbnail: https://img.youtube.com/vi/8J37g9NxHmM/maxresdefault.jpg
tags:
  - NASA OPERA
  - QGIS
  - OpenGeoAgent
  - GeoAI
  - Remote Sensing
keywords:
  - NASA OPERA
  - DSWx
  - QGIS Plugin
  - NASA Earthdata
  - Surface Water
  - Sentinel-1
  - Google Earth Engine
  - AI Agent
---

# Access NASA OPERA Data in QGIS with a Plugin and an AI Agent

[NASA OPERA](https://www.jpl.nasa.gov/go/opera) (Observational Products for End-Users from Remote Sensing Analysis) is a project led by NASA Jet Propulsion Laboratory that produces a suite of analysis-ready remote sensing data products, including dynamic surface water, land surface disturbance, surface displacement, and radiometric terrain corrected SAR imagery. In collaboration with JPL, I have been working on making these products easier to access through open-source geospatial tools, and the [OPERA project site](https://opera.opengeos.org) brings the documentation, an interactive web app, and tutorials together in one place.

In this tutorial, I walk through the [NASA OPERA QGIS plugin](https://github.com/opengeos/qgis-nasa-opera-plugin) I developed: how to install it, authenticate with NASA Earthdata, search and stream DSWx surface water products, and use the integrated AI agent to query OPERA data with natural language and voice commands. This is the first video in a planned series on the OPERA data products.

:::{iframe} https://www.youtube.com/embed/8J37g9NxHmM
:width: 100%
Video tutorial: QGIS NASA OPERA Plugin + AI Agent (Full Tutorial)
:::

## What You Will Need

- [QGIS](https://qgis.org) desktop (any standard installation works)
- A free [NASA Earthdata](https://urs.earthdata.nasa.gov) account for searching and downloading data
- A Google Cloud project ID, optional, only if you plan to query OPERA through the AI agent's Earth Engine mode
- A [ChatGPT](https://chat.openai.com) subscription (recommended) or an OpenAI API key, only if you plan to use the AI agent

## NASA OPERA Data Products

OPERA produces several product suites. The ones most users will reach for first are:

- **DSWx** (Dynamic Surface Water Extent), with two variants: **DSWx-HLS** derived from Harmonized Landsat and Sentinel-2, and **DSWx-S1** derived from Sentinel-1 SAR
- **DIST**, land surface disturbance products that flag changes such as deforestation, fires, and other disruptions
- **DISP**, surface displacement products useful for monitoring landslides, subsidence, and other deformation events
- **RTC**, radiometric terrain corrected Sentinel-1 SAR backscatter

A key advantage of OPERA is that the products are continuously updated as new source imagery becomes available. By contrast, widely used legacy datasets such as the JRC Global Surface Water are frozen at 2021, which makes them unsuitable for monitoring recent events. With OPERA, water and disturbance products typically become available within a couple of weeks of acquisition. Detailed product specification documents are linked from the [OPERA project site](https://www.jpl.nasa.gov/go/opera).

## Install the Plugins

Open **Plugins > Manage and Install Plugins** in QGIS and install the following from the official QGIS Plugin Repository:

1. **NASA OPERA**, the plugin this tutorial focuses on
2. **OpenGeoAgent**, the AI agent that integrates with the OPERA plugin
3. **Earth Engine Data Catalogs**, used for cloud-scale OPERA queries through the AI agent
4. **leafmap**, used for side-by-side layer comparison

After installation, each plugin appears in the QGIS menu bar with its own menu. If you only need to search and download OPERA data, the **NASA OPERA** plugin alone is sufficient. The other three are required for the AI workflow later in this tutorial.

## Authenticate with NASA Earthdata

You need a NASA Earthdata account to search and download data. If you do not have one, register at [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov).

To authenticate inside QGIS:

1. Open the NASA OPERA plugin and click the **Settings** icon.
2. Enter your Earthdata username and password.
3. Click **Test Credentials**. A success message confirms the connection.
4. Click **Save Settings**.

The credentials are written to your user directory and reloaded automatically the next time you open the plugin, so this is a one-time step. The first time you open the plugin you may also be prompted to install Python dependencies. Click **Install Dependencies** and follow the instructions.

## Search and Visualize DSWx Data

The plugin's main panel exposes a dropdown of OPERA product types. The DSWx surface water products are a good place to start.

1. Pick **DSWx-HLS** from the product dropdown for optical surface water from Landsat and Sentinel-2.
2. Set the area of interest. Click **Use Current Extent** to use the visible map canvas, or click **Draw Rectangle** to draw a bounding box. The coordinates appear in the upper right corner of the panel.
3. Adjust the **Date Range**. A shorter range returns fewer scenes, which is useful while you are exploring.
4. Adjust **Max Results** to cap how many scenes come back (10 is plenty for testing).
5. Click **Search**. The matching scenes appear in a results table on the right. Click any column header to sort. Each row shows the acquisition dates so you can pick the most recent imagery.
6. Select a row and click **Display Single** to stream that scene into QGIS.

The plugin uses cloud-optimized GeoTIFF streaming, so no full file is downloaded when you display a scene. Each DSWx scene contains 10 layers, including a multi-class water classification, a binary water layer, confidence layers, and quality masks. The full layer specification is documented in the DSWx-HLS product specification PDF, linked from the [OPERA project site](https://opera.opengeos.org). On the streamed layer, blue pixels typically indicate open water and lighter blue pixels indicate partial water, while values such as 252 represent snow and ice.

DSWx-HLS is optical and therefore affected by clouds. To avoid cloud gaps, repeat the search with **DSWx-S1** selected. Because Sentinel-1 is SAR, it sees through clouds and produces much more complete coverage in cloudy regions. The DSWx-S1 product encodes open water differently from DSWx-HLS, so consult the DSWx-S1 specification for the full class list.

## Mosaic Multiple Scenes

If your area of interest spans more than one scene, hold `Shift` and select multiple rows in the results table, then click **Display Mosaic**. The plugin builds a virtual mosaic on the fly through cloud-optimized GeoTIFF streaming, again without downloading the underlying files. Toggling the mosaic layer off in the QGIS Layers panel makes it easy to see how the individual tiles join together.

## Download Data

When you want to keep a layer locally for offline analysis or further processing:

1. Select the row of the scene you want.
2. Click **Download Selected Layer** to save a single layer, or **Download All** to save all 10 layers of the scene.
3. Choose a destination directory and click **Save**.

DSWx layers are small (often well under 1 MB per layer), so downloads usually finish in seconds. The downloaded files are standard GeoTIFFs that you can drop into any GIS or process with `rasterio`, `gdal`, `xarray`, and similar tools.

## Query OPERA with the AI Agent

The plugin's star icon opens an AI assistant powered by [OpenGeoAgent](https://github.com/opengeos/GeoAgent). If OpenGeoAgent is not installed yet, the plugin offers to install it for you. The agent can search and visualize OPERA data through either the NASA Earthdata provider or the Google Earth Engine Data Catalog provider, the latter giving you global-scale, cloud-side queries with no local downloads.

A few setup notes:

- In the agent **Settings**, choose a model provider on the **Models** tab. Logging in with a ChatGPT subscription is the easiest path because billing is a flat monthly cost.
- For Earth Engine mode, set your Google Cloud project ID in the agent settings or as an environment variable.
- For voice dictation and image interpretation, add an OpenAI API key. Voice runs about a cent per request, image interpretation a few cents per image.
- Press `Ctrl+Alt+Space` to start and stop voice dictation. Press `Ctrl+Enter` to submit a prompt.

For a deeper walkthrough of the agent itself, see the companion post [OpenGeoAgent: An Open-Source Multimodal AI Agent](./opengeoagent-qgis-plugin).

## Example: Map the July 2025 Texas Flood

Central Texas experienced a severe flooding event starting July 4, 2025. OPERA DSWx-S1 is a natural fit for mapping this kind of event because Sentinel-1 SAR cuts through cloud cover and the products are continuously updated. With the AI agent set to the **Earth Engine Data Catalog** provider and **trust auto-approve** enabled, send these prompts in order:

1. `Zoom to Austin, Texas.`
2. `Show NASA OPERA Sentinel-1 water data product for the current extent for June 2025.` (pre-event baseline)
3. `Show NASA OPERA Sentinel-1 water data product for the current extent for July 2025.` (post-event)
4. `Use red color for the water data in July 2025.`

The agent picks the right Earth Engine asset, applies date filters, runs a maximum reducer over the month, and adds the result as a tiled layer. The June layer shows the normal river network. The July layer, styled in red, reveals the flooded extent. Toggling the July layer on and off makes the inundation footprint immediately visible.

Every tool call exposes a **Copy Script** button that returns the underlying Earth Engine Python code. Paste it into a notebook or script for a fully reproducible version of the same workflow. This is also a useful way to learn how the agent constructs queries.

## Compare Layers Side by Side

To compare the June and July water masks more carefully, open the **leafmap** plugin and pick the two layers in the swipe widget. Activate **Swipe** and slide the divider across the canvas to see exactly which areas were dry in June but covered with water in July. This is the cleanest way to communicate a flooding footprint to a non-technical audience.

## Multimodal Image Interpretation

The agent is multimodal. Use the **Capture Map Canvas** screenshot tool, attach the screenshot to a prompt, and ask:

> What is in this image?

The agent describes what it sees on the map, including the data layers you just added. This is handy when you want a sanity check on an unfamiliar dataset, or when you need a written description of a map for a report. Vision features require an OpenAI API key.

## Resources

- QGIS plugin repository: [github.com/opengeos/qgis-nasa-opera-plugin](https://github.com/opengeos/qgis-nasa-opera-plugin)
- OPERA project site: [opera.opengeos.org](https://opera.opengeos.org)
- NASA OPERA mission page: [jpl.nasa.gov/go/opera](https://www.jpl.nasa.gov/go/opera)
- NASA Earthdata: [earthdata.nasa.gov](https://earthdata.nasa.gov)
- OpenGeoAgent: [github.com/opengeos/GeoAgent](https://github.com/opengeos/GeoAgent)
- Companion post: [OpenGeoAgent: An Open-Source Multimodal AI Agent](./opengeoagent-qgis-plugin)
- Video tutorial: [youtu.be/8J37g9NxHmM](https://youtu.be/8J37g9NxHmM)

This is the first tutorial in a planned series on the OPERA data products. Future videos will cover DIST, DISP, and RTC workflows, plus more advanced AI agent recipes such as automated change detection. If you run into bugs or have feature requests, please open an issue on the [GitHub repository](https://github.com/opengeos/qgis-nasa-opera-plugin), and subscribe on [YouTube](https://youtube.com/@giswqs) or follow the [RSS feed](/rss.xml) to catch the next post when it is released.
