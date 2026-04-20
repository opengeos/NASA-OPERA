---
title: Earth Engine Data Catalogs
description: The Earth Engine Data Catalogs QGIS plugin for browsing and accessing Google Earth Engine datasets alongside OPERA products.
thumbnail: ../images/logo.png
---

# Earth Engine Data Catalogs

[![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-green.svg)](https://plugins.qgis.org/plugins/gee_data_catalogs)
[![GitHub](https://img.shields.io/badge/GitHub-qgis--gee--data--catalogs--plugin-blue.svg?logo=github)](https://github.com/opengeos/qgis-gee-data-catalogs-plugin)

A comprehensive QGIS plugin for browsing, searching, and loading Google
Earth Engine data catalogs directly in QGIS.

- **Repository**: <https://github.com/opengeos/qgis-gee-data-catalogs-plugin>
- **License**: MIT
- **Requires**: QGIS 3.28+, Google Earth Engine account

## Features

- **Dynamic Data Catalog Browser**: Automatically loads datasets from the
  official GEE catalog and community datasets:
  - [Official Earth Engine Data Catalog](https://github.com/opengeos/Earth-Engine-Catalog) with 780+ datasets
  - [Awesome GEE Community Catalog](https://github.com/samapriya/awesome-gee-community-datasets) with 4,360+ community datasets
- **Search & Filter**: Search datasets by keywords, tags, providers, data
  types, and sources.
- **Advanced Filtering for ImageCollections**: Date range, bounding box
  (current map extent), and cloud-cover percentage.
- **Time Series**: Create time-series layers from ImageCollections.
- **Pixel Time Series Inspector**: Click on the map to extract and chart
  time series at a point, similar to Earth Engine's
  `ui.Chart.image.series`.
- **Flexible Image Loading**: Load composite images (mosaic, median, mean,
  min, max) or select and load individual images from ImageCollections.
- **Code Console**: Write and execute geemap/Earth Engine Python code
  directly in QGIS.
- **Visualization Parameters**: Customize with bands, min/max values, and
  color palettes.
- **Conversion**: Convert Earth Engine JavaScript API code to Python API.
- **Inspector**: Inspect Earth Engine layer values at specific locations.
- **Export**: Export Earth Engine layers to various file formats.
- **Multiple Data Types**: Load EE Image, ImageCollection, and
  FeatureCollection layers.
- **Integration**: Works seamlessly with
  [qgis-geemap-plugin](https://github.com/opengeos/qgis-geemap-plugin).
- **Update Checker**: Built-in plugin update checker from GitHub.

## Data Sources

The plugin dynamically fetches catalog data from:

| Source | Datasets |
|--------|----------|
| [Official Earth Engine Data Catalog](https://raw.githubusercontent.com/opengeos/Earth-Engine-Catalog/master/gee_catalog.json) | 780+ |
| [Awesome GEE Community Catalog](https://raw.githubusercontent.com/samapriya/awesome-gee-community-datasets/master/community_datasets.json) | 4,360+ |

## Video Tutorials

:::{iframe} https://www.youtube.com/embed/nZ3D6wLKJQw
:width: 100%
This QGIS Plugin Unlocks 80 Petabytes of Satellite Data, For Free!
:::

:::{iframe} https://www.youtube.com/embed/8IW6XqnUjgg
:width: 100%
Create Stunning Time-Series Satellite Images in Seconds!
:::

## Installation

### Prerequisites

1. QGIS 3.28 or higher.
2. A Google Earth Engine account (sign up at
   [earthengine.google.com](https://earthengine.google.com/)).

### Install QGIS and Google Earth Engine with Pixi

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
pixi add qgis geemap geopandas xee rioxarray
```

#### 4. Authenticate Earth Engine

```bash
pixi run earthengine authenticate
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
9. Search for "Earth Engine Data Catalogs".
10. Select the plugin and click **Install Plugin**.

#### Method 2: From ZIP File

1. Download the latest release ZIP from <https://qgis.gishub.org>.
2. In QGIS, go to **Plugins > Manage and Install Plugins**.
3. Click **Install from ZIP** and select the downloaded file.
4. Enable the plugin in the **Installed** tab.

#### Method 3: Manual Installation

Copy the `gee_data_catalogs` folder to your QGIS plugins directory:

- **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
- **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
- **Windows**: `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`

Restart QGIS and enable the plugin.

## Usage

### Initialize Earth Engine

Before using the plugin, authenticate with Google Earth Engine:

1. Click the **Initialize Earth Engine** button in the toolbar.
2. If not authenticated, run `earthengine authenticate` in your terminal.
3. Set the `EE_PROJECT_ID` environment variable for auto-initialization.

### Browse Datasets

1. Click the **Data Catalog** button to open the catalog panel.
2. Browse datasets by category in the **Browse** tab.
3. Filter by source (Official/Community).
4. Click a dataset to view its information.
5. Click **Add to Map** to load with default visualization.

### Search Datasets

1. Go to the **Search** tab.
2. Enter keywords in the search box.
3. Filter by category, data type, or source.
4. Double-click a result to add it to the map.

### Time Series

1. Go to the **Time Series** tab.
2. Enter the dataset Asset ID.
3. Set the date range and optional filters.
4. Choose a frequency (e.g. month, year) and reducer (e.g. mean, median).
5. Click **Create Time Series** to build the time-series layer.
6. Use **Next** and **Previous** to navigate through the time series.

### Pixel Time Series Inspector

Extract time-series data at a clicked point location, similar to Earth
Engine's `ui.Chart.image.series`:

1. Go to the **Time Series** tab.
2. Enter the dataset Asset ID and configure date range and filters.
3. Scroll to the **Pixel Time Series Inspector** section.
4. Click **Start Pixel Inspector** to activate the map click tool.
5. Click anywhere on the map to select a pixel location.
6. (Optional) Specify bands to extract and set the scale (resolution).
7. Click **Extract & Chart** to extract values and open an interactive chart.
8. In the chart dialog, toggle bands/points/grid, view statistics (min,
   max, mean, std), export to CSV/JSON/PNG, or copy data to the clipboard.

### Load with Custom Parameters

1. Go to the **Load** tab.
2. Enter the dataset Asset ID.
3. Configure filters: date range for ImageCollections, cloud-cover
   threshold, spatial filter (current map extent).
4. Choose loading mode: **Composite** (mosaic, median, mean, min, max) or
   **Individual Images**.
5. Set visualization parameters.
6. Click **Load Dataset**.

### Code Console

1. Go to the **Code** tab.
2. Write Python code using the Earth Engine Python API and geemap syntax.
3. Click **Run Code** to execute.

### Conversion

1. Go to the **Conversion** tab.
2. Select an input layer.
3. Choose the conversion type (Image, ImageCollection, or FeatureCollection).
4. Configure the output options.

### Inspector

1. Go to the **Inspector** tab.
2. Click **Start Inspector**.
3. Click on the map to inspect Earth Engine layer values at that location.
4. Click **Clear** to clear the inspector.
5. Click **Refresh Layers** to refresh the layers.

### Export

1. Go to the **Export** tab.
2. Select an EE layer to export.
3. Choose the export region (map extent, vector bounds, drawn, or custom).
4. Set export options (scale, CRS, and format).
5. Choose an output file or leave it blank for a temporary export.
6. Click **Export**.

### Notes

- **Network timeout warnings**: You may see timeout warnings in the QGIS
  log when loading Earth Engine layers. These are normal and occur due to
  Earth Engine's tile serving; layers will still load, just wait for the
  tiles to appear.
- **Performance**: For large ImageCollections, use date and spatial filters
  to reduce the number of images processed.

## Available Dataset Categories

- **Landsat**: Landsat 5, 7, 8, 9 Collection 2
- **Sentinel**: Sentinel-1 SAR, Sentinel-2 MSI, Sentinel-3, Sentinel-5P
- **MODIS**: Vegetation indices, surface reflectance, temperature, snow, fire
- **Elevation**: SRTM, ALOS, Copernicus DEM, ASTER GDEM
- **Land Cover**: ESA WorldCover, Dynamic World, MODIS Land Cover, NLCD
- **Climate & Weather**: ERA5, CHIRPS, GPM, TRMM
- **Boundaries**: FAO GAUL, US Census TIGER, GADM
- **Night Lights**: VIIRS, DMSP-OLS
- **Population**: WorldPop, GPW, LandScan
- **Water**: JRC Global Surface Water
- **Vegetation**: NDVI, EVI, LAI, GPP products
- **Atmosphere**: Aerosol, Ozone, NO2, CO2
- **Agriculture**: Crop maps, harvest area, irrigation
- **Soil**: Soil properties, moisture, organic carbon
- **Fire**: Active fire, burned area
- **Ocean**: SST, chlorophyll, coral reefs
- **Urban**: Built-up areas, impervious surfaces

## Configuration

Access settings via the **Settings** toolbar button:

- **General**: Auto-initialization, notifications, default category.
- **Earth Engine**: Project ID, default filters, performance options.
- **Display**: Layer opacity, visualization defaults.

## Troubleshooting

### Authentication Issues

If you encounter errors like "Failed to initialize Google Earth Engine" or
"Request is missing required authentication credential":

#### Step 1: Authenticate Earth Engine (first time only)

Method A: Via QGIS Python Console:

```python
import ee
ee.Authenticate()
```

Method B: Via terminal:

```bash
earthengine authenticate
```

Follow the browser instructions and restart QGIS after authentication.

#### Step 2: Configure Your Project ID

Method A: Enter your Google Cloud Project ID in the plugin's Settings panel
under the **Earth Engine** tab, save, and click **Initialize Earth Engine**.

Method B: Set the `EE_PROJECT_ID` environment variable in your system or
QGIS profile.

#### Common Issues

1. **"Credentials not found"**: Run `ee.Authenticate()` first.
2. **"Failed to initialize"**: Set your Project ID in Settings.
3. **"Invalid project"**: Verify the Project ID and that Earth Engine is
   enabled for that project.
4. **Still not working**: Try `ee.Authenticate(force=True)` to
   re-authenticate.

For more help, check the QGIS message log under **View > Panels > Log
Messages** (filter by "GEE Data Catalogs"), or report issues at
<https://github.com/opengeos/qgis-gee-data-catalogs-plugin/issues>.

## Related Projects

- [geemap](https://github.com/gee-community/geemap): Python package for
  interactive mapping with Google Earth Engine.
- [qgis-geemap-plugin](https://github.com/opengeos/qgis-geemap-plugin):
  QGIS plugin for geemap integration.
- [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets): Official GEE dataset documentation.
- [Awesome GEE Community Datasets](https://github.com/samapriya/awesome-gee-community-datasets): Community-contributed datasets.
