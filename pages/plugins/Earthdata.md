---
title: NASA Earthdata
description: The NASA Earthdata QGIS plugin for searching, visualizing, and downloading NASA Earth science datasets directly in QGIS.
thumbnail: ../images/logo.png
---

# NASA Earthdata

[![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-green.svg)](https://plugins.qgis.org/plugins/nasa_earthdata)
[![GitHub](https://img.shields.io/badge/GitHub-qgis--nasa--earthdata--plugin-blue.svg?logo=github)](https://github.com/opengeos/qgis-nasa-earthdata-plugin)

A QGIS plugin for searching, visualizing, and downloading NASA Earthdata
products. Provides access to NASA's Earth science data catalog directly
within QGIS, supporting Cloud Optimized GeoTIFF (COG) visualization and
data footprint display.

- **Repository**: <https://github.com/opengeos/qgis-nasa-earthdata-plugin>
- **License**: MIT
- **Requires**: QGIS 3.28+, NASA Earthdata account

## Features

- **Search NASA Earthdata Catalog**: Browse and search thousands of NASA
  Earth science datasets using keywords, bounding boxes, and temporal filters.
- **Visualize Data Footprints**: Display search result footprints directly
  on the QGIS map canvas.
- **Cloud Optimized GeoTIFF (COG) Support**: Stream and visualize COG files
  directly without downloading.
- **Data Download**: Download granules for local processing and visualization.
- **Earthdata Login Integration**: Seamless authentication with NASA
  Earthdata Login credentials.
- **Settings Panel**: Configure credentials, download preferences, and
  plugin options.

## Video Tutorials

:::{iframe} https://www.youtube.com/embed/H78l-3nbPfk
:width: 100%
The Easiest Way to Access 120 Petabytes of NASA Data Inside QGIS
:::

:::{iframe} https://www.youtube.com/embed/oRTplHPf_T0
:width: 100%
How to Download and Visualize NISAR Data in QGIS
:::

## Installation

### Prerequisites

1. QGIS 3.28 or higher.
2. A NASA Earthdata account (sign up at
   [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov/)).

### Install QGIS with Pixi

#### 1. Install Pixi

Linux/macOS (bash/zsh):

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Close and re-open your terminal, then confirm with `pixi --version`.

#### 2. Create a Pixi Project

```bash
pixi init geo
cd geo
```

#### 3. Install the Environment

```bash
pixi add qgis earthaccess geopandas
```

### Installing the Plugin

#### Method 1: From QGIS Plugin Manager (Recommended)

1. Open QGIS using `pixi run qgis`.
2. Go to **Plugins > Manage and Install Plugins...**.
3. Go to the **Settings** tab.
4. Click **Add...** under "Plugin Repositories".
5. Give a name for the repository, e.g. "OpenGeos".
6. Enter the URL of the repository: <https://qgis.gishub.org/plugins.xml>.
7. Click **OK**.
8. Go to the **All** tab.
9. Search for "NASA Earthdata".
10. Select the plugin and click **Install Plugin**.

#### Method 2: From ZIP File

1. Download the latest release ZIP from <https://qgis.gishub.org>.
2. In QGIS, go to **Plugins > Manage and Install Plugins**.
3. Click **Install from ZIP** and select the downloaded file.
4. Enable the plugin in the **Installed** tab.

#### Method 3: Manual Installation

Copy the `nasa_earthdata` folder to your QGIS plugins directory:

- **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
- **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
- **Windows**: `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`

Restart QGIS and enable the plugin.

## Usage

### Authentication

Before using the plugin, configure your NASA Earthdata credentials:

1. Click **NASA Earthdata > Settings** in the menu.
2. Enter your Earthdata username and password.
3. Click **Test Credentials** to verify.
4. Click **Save Settings**.

Alternatively, configure credentials via:

- Environment variables: `EARTHDATA_USERNAME` and `EARTHDATA_PASSWORD`.
- A `.netrc` file with an entry for `urs.earthdata.nasa.gov`.

### Searching Data

1. Click the **NASA Earthdata Search** button in the toolbar.
2. Filter datasets by keyword (optional).
3. Select a dataset from the dropdown.
4. Set the bounding box (or use the current map extent).
5. Set the date range.
6. Click **Search**.

### Visualizing Data

- **Footprints**: Search results are automatically displayed as footprints
  on the map.
- **COG Layers**: Select results and click **Display COG** to stream Cloud
  Optimized GeoTIFFs.
- **Downloaded Data**: After downloading, raster files can be added
  directly to the map.

### Downloading Data

1. Select the granules to download from the results table.
2. Click **Download**.
3. Choose a destination folder.
4. Wait for the download to complete.
5. Optionally add downloaded files to the map.

## Supported Datasets

The plugin provides access to thousands of NASA datasets including:

- **GEDI**: Global Ecosystem Dynamics Investigation (forest structure,
  biomass)
- **MODIS**: Moderate Resolution Imaging Spectroradiometer
- **Landsat**: Landsat 8 and 9 imagery
- **VIIRS**: Visible Infrared Imaging Radiometer Suite
- **SMAP**: Soil Moisture Active Passive
- **ICESat-2**: Ice, Cloud, and land Elevation Satellite
- **OPERA**: Observational Products for End-Users from Remote Sensing
  Analysis
- And many more

## Troubleshooting

### Authentication Issues

1. Verify credentials at <https://urs.earthdata.nasa.gov/>.
2. Confirm you've accepted the EULA for the datasets you are accessing.
3. Try running `earthaccess.login()` in the QGIS Python console.

### Missing Dependencies

```bash
# Using pip
pip install earthaccess geopandas

# Using the QGIS Python environment (Linux)
~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/nasa_earthdata/
python3 -m pip install earthaccess geopandas
```

### COG Visualization Issues

- Ensure GDAL has network support enabled.
- Check that the data URL is accessible.
- Some datasets may require authentication for streaming.

## Links

- [GitHub Repository](https://github.com/opengeos/qgis-nasa-earthdata-plugin)
- [Issue Tracker](https://github.com/opengeos/qgis-nasa-earthdata-plugin/issues)
- [NASA Earthdata](https://earthdata.nasa.gov/)
- [NASA Earthdata Login](https://urs.earthdata.nasa.gov/)

## Acknowledgments

- [NASA Earthdata](https://earthdata.nasa.gov/) for providing access to
  Earth science data.
- [earthaccess](https://github.com/nsidc/earthaccess) for the NASA
  Earthdata API access library.
- [leafmap](https://github.com/opengeos/leafmap) for GUI design inspiration.
- [QGIS](https://qgis.org/) for the open-source GIS platform.
