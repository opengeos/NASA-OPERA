---
title: NASA OPERA
description: The NASA OPERA QGIS plugin for no-code and low-code access to OPERA data products.
thumbnail: ../images/logo.png
---

# NASA OPERA

[![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-green.svg)](https://plugins.qgis.org/plugins/nasa_opera)
[![GitHub](https://img.shields.io/badge/GitHub-qgis--nasa--opera--plugin-blue.svg?logo=github)](https://github.com/opengeos/qgis-nasa-opera-plugin)

A QGIS plugin for searching, visualizing, and analyzing NASA OPERA
(Observational Products for End-Users from Remote Sensing Analysis)
satellite data products, with an AI assistant for natural-language interaction.

- **Repository**: <https://github.com/opengeos/qgis-nasa-opera-plugin>
- **License**: MIT
- **Requires**: QGIS 3.28+

## About NASA OPERA

OPERA is a NASA project that provides analysis-ready data products derived
from satellite observations, producing near-real-time and systematic global
data products from optical and SAR satellite imagery. Learn more at the
[NASA OPERA project page](https://www.jpl.nasa.gov/go/opera).

## Features

- **Search Interface**: Query NASA OPERA products by location, date range, and dataset type.
- **Footprint Visualization**: Display search-result footprints as vector layers on the map.
- **Raster Display**: Visualize OPERA raster data directly in QGIS with cloud-optimized streaming.
- **Virtual Mosaics**: Combine multiple granules into seamless mosaics via GDAL VRT.
- **AI Assistant**: Use natural language to search, display, and analyze OPERA data.
- **Multiple LLM Providers**: OpenAI, Anthropic, Amazon Bedrock, Google Gemini, and local Ollama.
- **Multiple Datasets**: Support for all OPERA products:
  - DSWX-HLS: Dynamic Surface Water Extent from Harmonized Landsat Sentinel-2
  - DSWX-S1: Dynamic Surface Water Extent from Sentinel-1
  - DIST-ALERT-HLS: Land Surface Disturbance Alert
  - DIST-ANN-HLS: Land Surface Disturbance Annual
  - RTC-S1: Radiometric Terrain Corrected SAR Backscatter
  - CSLC-S1: Coregistered Single-Look Complex
- **Settings Panel**: Configure Earthdata credentials, display options, and AI provider.
- **Update Checker**: Check for plugin updates from GitHub.

## Prerequisites

### NASA Earthdata Account

To access NASA OPERA data, a free NASA Earthdata account is required:

1. Register at [NASA Earthdata](https://urs.earthdata.nasa.gov/users/new)
2. Configure your credentials in the plugin settings.

### Python Dependencies

The plugin manages dependencies automatically via an isolated virtual
environment. On first use, open **Settings > Dependencies** and click
**Install Dependencies** to install:

- `earthaccess` for NASA Earthdata search and download
- `geopandas` for geospatial data manipulation
- `shapely` for geometry operations
- `pandas` for data analysis

For the AI Assistant, open **Settings > AI Assistant** and click
**Install AI Dependencies** to install `litellm` (a unified LLM interface
for multiple providers).

## Installation

### Method 1: Install from Source

```bash
git clone https://github.com/opengeos/qgis-nasa-opera-plugin.git
cd qgis-nasa-opera-plugin
# Linux/macOS
./install.sh
# Windows or cross-platform
python install.py
```

Restart QGIS, then enable the plugin via **Plugins > Manage and Install
Plugins...** and searching for "NASA OPERA".

### Method 2: Manual Installation

Copy the `nasa_opera` folder to your QGIS plugins directory:

- **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
- **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
- **Windows**: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`

Restart QGIS and enable the plugin.

## Usage

### Basic Workflow

1. **Open the Plugin**: Click the NASA OPERA toolbar icon or go to
   **NASA OPERA > NASA OPERA Search**.
2. **Select Dataset**: Choose the OPERA product to search for.
3. **Set Search Parameters**:
   - **Bounding Box**: Enter coordinates manually or click "Use Map Extent".
   - **Date Range**: Select start and end dates.
   - **Max Results**: Set the maximum number of results.
4. **Search**: Click the "Search" button to find available data.
5. **View Results**:
   - **Show Footprints**: Display the spatial coverage of search results.
   - **Display Single**: Load a specific granule's raster data.
   - **Display Mosaic**: Create a virtual mosaic from selected granules.

### AI Assistant

The AI Assistant lets you interact with NASA OPERA data using natural language.

1. **Setup**: Go to **NASA OPERA > Settings > AI Assistant**, install AI
   dependencies, select your LLM provider, enter an API key (not required
   for Ollama), and click "Test Connection".
2. **Open**: Click the AI Assistant toolbar icon or go to
   **NASA OPERA > AI Assistant**.
3. **Ask Questions**: Type natural language queries such as:
   - "What OPERA datasets are available?"
   - "Search for surface water data in my current map extent."
   - "Find land disturbance alerts in California from 2024."
   - "Show me the latest DSWX-HLS data for the Las Vegas area."
   - "Create a mosaic of the first 5 results."
   - "What layers do I have loaded?"

The AI Assistant can search data, display footprints, load rasters, create
mosaics, and manage map layers, all through conversation.

**Supported LLM providers:**

| Provider | Default Model | API Key Required |
|----------|---------------|------------------|
| OpenAI | gpt-4.1 | Yes |
| Anthropic | claude-sonnet-4-6 | Yes |
| Amazon Bedrock | claude-sonnet-4-20250514 | AWS credentials |
| Google Gemini | gemini-2.5-flash | Yes |
| Ollama | llama3.3 | No (local) |

### Settings

Access settings via **NASA OPERA > Settings**:

- **Dependencies**: Install and manage core Python packages.
- **Credentials**: Configure NASA Earthdata username and password.
- **Display**: Customize footprint styles and default colormap.
- **Advanced**: Set default search parameters and cache options.
- **AI Assistant**: Configure LLM provider, model, API key, and parameters.

### First-Time Authentication

When you first run a search, the plugin authenticates with NASA Earthdata.
If credentials are not configured, `earthaccess` will prompt for login and
store them in `~/.netrc` for future use. Credentials can also be configured
in the Settings panel.

## Support

- **Bug Reports / Feature Requests**: <https://github.com/opengeos/qgis-nasa-opera-plugin/issues>
- **Documentation**: <https://github.com/opengeos/qgis-nasa-opera-plugin/wiki>

## Acknowledgments

- [NASA OPERA Project](https://www.jpl.nasa.gov/go/opera) for the data products
- [earthaccess](https://github.com/nsidc/earthaccess) for NASA Earthdata access
- [litellm](https://github.com/BerriAI/litellm) for unified LLM provider access
- [leafmap](https://github.com/opengeos/leafmap) for GUI design inspiration
- The QGIS community for the GIS platform
