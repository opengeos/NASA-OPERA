---
title: "Compare Geospatial Layers in QGIS with the LeafMap Plugin"
date: 2025-12-30
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: Introducing the LeafMap QGIS plugin with interactive layer transparency controls and a swipe tool for comparing geospatial layers side by side.
thumbnail: https://img.youtube.com/vi/glBgnyS8IDY/maxresdefault.jpg
tags:
  - QGIS
  - LeafMap
  - Visualization
  - Open Source
keywords:
  - LeafMap
  - QGIS Plugin
  - Layer Swipe
  - Layer Transparency
  - Change Detection
---

# Compare Geospatial Layers in QGIS with the LeafMap Plugin

If you have used [leafmap](https://leafmap.org) or [ipyleaflet](https://ipyleaflet.readthedocs.io), you are probably familiar with interactive tools like layer transparency sliders and split-map controls for comparing datasets side by side. I have not found a good QGIS plugin that provides similar functionality, so I built one. The [LeafMap QGIS plugin](https://github.com/opengeos/qgis-leafmap-plugin) brings two essential tools to QGIS: dynamic layer transparency and a layer swipe tool for comparing any two layers.

In this short tutorial, I walk through installing the plugin and using both features with real-world data, including a before-and-after comparison of the 2023 Libya flooding.

:::{iframe} https://www.youtube.com/embed/glBgnyS8IDY
:width: 100%
Video tutorial: LeafMap QGIS Plugin for Layer Comparison
:::

## What You Will Need

- [QGIS](https://qgis.org) desktop (any standard installation works; Pixi is not required for this plugin)

## Install the Plugin

The plugin is available in the official QGIS Plugin Repository:

1. Go to **Plugins > Manage and Install Plugins**.
2. Search for **leafmap**.
3. Click **Install Plugin**.

After installation, three buttons appear in the toolbar and a **LeafMap** menu appears in the menu bar. The plugin includes a built-in update checker: go to **LeafMap > Check for Updates** to get the latest version from GitHub.

## Layer Transparency

The layer transparency tool provides a real-time slider for adjusting the opacity of any layer without opening the layer properties dialog.

1. Click the **Layer Transparency** button in the toolbar.
2. A panel opens on the right showing all loaded layers with individual transparency sliders.
3. Drag a slider to the right to increase transparency (0% is fully opaque, 100% is fully transparent).

This is much faster than the built-in QGIS workflow of double-clicking a layer, navigating to the transparency tab, entering a value, and clicking OK. The slider updates the display in real time as you drag.

You can toggle between showing **all layers** or only **visible layers** using the checkbox at the top of the panel.

## Layer Swipe

The layer swipe tool lets you compare two layers side by side with a draggable divider, similar to the split-map controls in leafmap and ipyleaflet.

### Set up the comparison

1. Click the **Layer Swipe** button in the toolbar.
2. Select the **left layer** from the dropdown.
3. Select the **right layer** from the dropdown.
4. Choose the swipe direction: **vertical** (left/right divider) or **horizontal** (top/bottom divider).
5. Click **Activate Swipe**.

### Use the swipe

Drag the divider across the map to reveal more or less of each layer. You can also set the position precisely using the percentage buttons (25%, 50%, 75%).

When you are done, click **Deactivate Swipe** to return to normal map view.

## Example: Libya Flooding Change Detection

The swipe tool is particularly useful for comparing pre- and post-event satellite imagery. Using Maxar Open Data imagery from the 2023 Libya flooding:

1. Load two GeoTIFF files: one from July 1, 2023 (pre-event) and one from September 13, 2023 (post-event).
2. Open the swipe tool.
3. Set the July image as the left layer and the September image as the right layer.
4. Activate the swipe and drag the divider to compare.

The comparison clearly reveals the destruction: bridges collapsed, roads washed away, and the landscape dramatically altered by the flood. This kind of visual comparison is essential for damage assessment and change detection workflows.

## Works with Any Layer Type

The swipe tool works with any combination of QGIS layers:

- Raster vs. raster (satellite imagery comparison)
- Basemap vs. basemap (Google Satellite vs. OpenStreetMap)
- Vector vs. raster (boundaries overlaid on imagery)
- Any two layers you need to compare

## Resources

- **GitHub Repository**: [github.com/opengeos/qgis-leafmap-plugin](https://github.com/opengeos/qgis-leafmap-plugin)
- **LeafMap Documentation**: [leafmap.org](https://leafmap.org)

More features will be added to the plugin in future releases. Follow the [GitHub repository](https://github.com/opengeos/qgis-leafmap-plugin) for updates, and feel free to open an issue if you have feature requests or run into any problems.
