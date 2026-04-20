---
title: Leafmap
description: The Leafmap QGIS plugin for interactive geospatial analysis and visualization of OPERA data products.
thumbnail: ../images/logo.png
---

# Leafmap

[![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-green.svg)](https://plugins.qgis.org/plugins/qgis_leafmap)
[![GitHub](https://img.shields.io/badge/GitHub-qgis--leafmap--plugin-blue.svg?logo=github)](https://github.com/opengeos/qgis-leafmap-plugin)

A QGIS plugin for interactive layer visualization and comparison, inspired
by the [leafmap](https://github.com/opengeos/leafmap) Python package.

- **Repository**: <https://github.com/opengeos/qgis-leafmap-plugin>
- **License**: MIT
- **Requires**: QGIS 3.28+, Python 3.10+

## Features

- **Layer Transparency Control**: Interactive slider to adjust layer
  transparency in real time for all loaded layers.
- **Layer Swipe Tool**: Compare two layers side-by-side with a draggable
  divider (similar to ipyleaflet's split control).
- **Dockable Panels**: All tools are available as dockable panels that can
  be positioned anywhere in the QGIS interface.
- **Plugin Update Checker**: Check for updates from GitHub and install them
  automatically.
- **Settings Panel**: Configure plugin options with persistent storage.

### Layer Transparency Panel

Control the transparency of all layers with individual sliders. Filter by
layer type (raster/vector) and visibility.

### Layer Swipe Tool

Compare two layers by swiping between them. Select left and right layers,
choose vertical or horizontal orientation, and drag the divider on the map.

## Video Tutorial

:::{iframe} https://www.youtube.com/embed/glBgnyS8IDY
:width: 100%
Compare Layers Visually in QGIS: New Leafmap Plugin Demo!
:::

## Installation

### Option A: QGIS Plugin Manager (Recommended)

1. Open QGIS.
2. Go to **Plugins > Manage and Install Plugins...**.
3. Go to the **Settings** tab.
4. Click **Add...** under "Plugin Repositories".
5. Give a name for the repository, e.g. "OpenGeos".
6. Enter the URL of the repository: <https://qgis.gishub.org/plugins.xml>.
7. Click **OK**.
8. Go to the **All** tab.
9. Search for "Leafmap".
10. Select the plugin and click **Install Plugin**.

### Option B: Install Script

Using Python:

```bash
git clone https://github.com/opengeos/qgis-leafmap-plugin.git
cd qgis-leafmap-plugin
python install.py
# Or remove
python install.py --remove
```

Using Bash:

```bash
chmod +x install.sh
./install.sh
# Or remove
./install.sh --remove
```

### Option C: Manual Installation

Copy the `qgis_leafmap` folder to your QGIS plugins directory:

- **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
- **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
- **Windows**: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`

## Usage

### Layer Transparency

1. Click the **Layer Transparency** button in the toolbar or go to
   **Leafmap > Layer Transparency**.
2. A dockable panel appears with a slider for each layer.
3. Drag the slider to adjust transparency (0% = opaque, 100% = transparent).
4. Use the filter options to show only raster or vector layers.
5. Use "Reset All" to restore all layers to 0% transparency.

### Layer Swipe Tool

1. Click the **Layer Swipe** button in the toolbar or go to
   **Leafmap > Layer Swipe**.
2. Select the **Left Layer** (shown on the left side of the divider).
3. Select the **Right Layer** (shown on the right side of the divider).
4. Choose **Vertical** or **Horizontal** orientation.
5. Click **Activate Swipe**.
6. Drag the divider on the map to compare layers.
7. Use the slider or quick buttons to adjust the divider position.
8. Click **Deactivate Swipe** when done.

### Settings

1. Go to **Leafmap > Settings**.
2. Adjust general, transparency, and swipe-tool options.
3. Click **Save Settings** to persist changes.

### Check for Updates

1. Go to **Leafmap > Check for Updates...**.
2. Click **Check for Updates** to see if a new version is available.
3. If an update is available, click **Download and Install Update**.
4. Restart QGIS to apply the update.

## Related Projects

- [leafmap](https://github.com/opengeos/leafmap): A Python package for
  interactive mapping and geospatial analysis.
- [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet): A Jupyter
  widget for Leaflet.js interactive maps.
- [geemap](https://github.com/gee-community/geemap): A Python package for
  interactive mapping with Google Earth Engine.

## Links

- [GitHub Repository](https://github.com/opengeos/qgis-leafmap-plugin)
- [Report Issues](https://github.com/opengeos/qgis-leafmap-plugin/issues)
- [Leafmap Documentation](https://leafmap.org)
