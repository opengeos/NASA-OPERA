---
title: "GeoAI QGIS Plugin v1.0: One-Click Installation for Geospatial AI"
date: 2026-02-25
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: Announcing GeoAI QGIS Plugin v1.0 with one-click installation, SAM 3, water segmentation, forest segmentation, and export to vector, raster, COCO, YOLO, and Pascal VOC formats.
thumbnail: https://img.youtube.com/vi/L90id_ESQME/maxresdefault.jpg
tags:
  - GeoAI
  - QGIS
  - Segmentation
  - Tutorial
  - Deep Learning
keywords:
  - GeoAI
  - QGIS
  - SAM 3
  - Segmentation
  - Deep Learning
  - DeepForest
  - OmniWaterMask
  - Moondream
---

# GeoAI QGIS Plugin v1.0: One-Click Installation for Geospatial AI

I am excited to announce version 1.0 of the GeoAI QGIS plugin. This release completely redesigns the installation process. Previously, getting GeoAI to work inside QGIS required wrestling with pip, CUDA dependencies, and Python environment conflicts, especially on Windows and macOS. Now you can install it with a single click directly from the QGIS Plugin Manager, and it works smoothly on Linux, Windows, and macOS. In this tutorial, I walk through the full setup process and demonstrate several of the plugin's capabilities, including SAM 3 segmentation, water segmentation, and vector export.

:::{iframe} https://www.youtube.com/embed/L90id_ESQME
:width: 100%
Video tutorial: GeoAI QGIS Plugin v1.0 Installation and Demo
:::

## What Is New in v1.0

- **One-click installation**: No more pip or manual dependency management. The plugin installs all dependencies (including CUDA/GPU support) into an isolated environment automatically.
- **Semantic segmentation**: Classify pixels into categories across an entire image.
- **Instance segmentation**: Detect and delineate individual objects.
- **SAM 3**: The latest Segment Anything Model for interactive and text-based segmentation (requires Hugging Face access request).
- **Moondream vision-language model**: Use natural language prompts with imagery.
- **Forest segmentation**: Powered by [DeepForest](https://github.com/weecology/DeepForest).
- **Water segmentation**: Powered by [OmniWaterMask](https://github.com/DPIRD-DMA/OmniWaterMask), works across different satellite sensors including multispectral imagery.
- **Export formats**: Save results as vector (GeoPackage, Shapefile) or raster, and export training data in COCO, YOLO, and Pascal VOC formats.

## What You Will Need

- [QGIS](https://qgis.org) desktop (free and open source).
- A GPU with at least 8 GB of memory is recommended for best performance. The plugin also works on CPU, though it will be significantly slower (roughly 10-20x). On macOS, it can use Apple's MPS acceleration.
- For SAM 3 specifically, you need a [Hugging Face](https://huggingface.co) account with approved access to the SAM 3 model.

## Install the Plugin

If you have a previous version of the GeoAI plugin installed, uninstall it first:

1. Go to **Plugins > Manage and Install Plugins**.
2. Find the old GeoAI plugin and click **Uninstall Plugin**.
3. Close and reopen QGIS.

Then install the new version:

1. Go to **Plugins > Manage and Install Plugins**.
2. Search for **geoai**.
3. Click **Install Plugin**. It finishes within seconds.

After installation, you will see seven toolbar buttons and a GeoAI menu with all the available tools: semantic segmentation, instance segmentation, SAM 3, Moondream, forest segmentation, and water segmentation.

## Set Up the Environment

The first time you click any of the plugin's tool buttons, a setup panel appears on the right side of QGIS. This is where the plugin installs all Python and GPU dependencies into an isolated environment, completely separate from the QGIS Python environment.

1. The plugin automatically detects whether your computer has a GPU and which CUDA version is available.
2. Click **Install**. This takes roughly 10-15 minutes depending on your internet speed.
3. When the installation completes, the tool panel opens automatically.

The isolated environment is stored under your user directory in a folder called `qgis_geoai`. This approach avoids the dependency conflicts that made previous versions so difficult to install, since QGIS ships with pre-installed packages (NumPy, SciPy, etc.) that often conflicted with deep learning libraries.

Future plugin updates will only install missing dependencies, so updates are much faster than the initial setup.

## Request Access to SAM 3

Most tools in the plugin are freely available without any additional steps. The one exception is SAM 3, which requires you to request access through Hugging Face:

1. Create a [Hugging Face](https://huggingface.co) account if you do not have one.
2. Navigate to the SAM 3 model page and submit the access request form.
3. Once approved, run `hf auth login` or authenticate through the plugin interface to allow the model to download automatically.

The plugin will notify you if access has not been granted yet and point you to the documentation for setup instructions.

## Try SAM 3 Segmentation

Once the environment is ready:

1. Load a satellite image into QGIS. Sample datasets are available in the [plugin documentation](https://opengeoai.org/qgis_plugin).
2. Click the **SAM 3** button in the toolbar. The tool panel opens on the right.
3. Click **Load Model**. You can verify GPU usage with `nvidia-smi` on Linux or Task Manager on Windows.
4. Select your image layer in the dropdown and click **Set Image Layer**. Wait for the green confirmation text.

### Segment by Text

Switch to the text prompt tab, type a description like "building," and click **Segment by Text**. SAM 3 identifies and segments all matching objects in the image.

### Segment by Box

Draw a bounding box around an example object on the map and click **Segment by Box**. The model finds all similar objects across the image.

If the model detects too many objects, increase the confidence threshold. If it misses objects, lower the threshold. You can adjust this in the model settings panel.

### Export Results

Switch to the **Output** tab to choose the export format. Select **GeoPackage** to get vector polygons, which are easier to edit and produce smoother boundaries than raster masks. Run the segmentation again and the results will be saved in your chosen format.

## Try Water Segmentation

The water segmentation tool is powered by OmniWaterMask and works across different satellite sensors without requiring you to train a custom model.

1. Load a satellite image (Sentinel-2, for example).
2. Click the **Water Segmentation** button.
3. Select the image layer and specify the band combination. For Sentinel-2, the default mapping works: Red (Band 4), Green (Band 3), Blue (Band 2), and Near-Infrared (Band 8). For other sensors, customize the band assignment.
4. Click **Run Segmentation**.

The tool automatically downloads OpenStreetMap water reference data and road masks for post-processing, runs the segmentation model on your GPU, and produces both raster and vector water masks. The vector output is smoothed, so you get clean polygons without the jagged edges typical of raster-to-vector conversion.

This tool is particularly useful because, unlike SAM 3 (which expects RGB input in the 0-255 range), OmniWaterMask handles multispectral floating-point data natively.

## Update the Plugin

The plugin checks for updates automatically. You can also check manually:

1. Go to **GeoAI > Check for Updates**.
2. If a new version is available, it downloads directly from GitHub and installs with one click.

This is useful for getting the latest features quickly, since it can take a few days for updates to appear in the official QGIS Plugin Repository.

## Manage GPU Memory

If you run into memory issues with large images, try a smaller image first or release the GPU after finishing:

1. Click the **Release GPU** button in the tool panel to free memory.
2. For a full reset, restart QGIS.

## Resources

- **Documentation**: [opengeoai.org/qgis_plugin](https://opengeoai.org/qgis_plugin)
- **GitHub**: [github.com/opengeos/geoai](https://github.com/opengeos/geoai)
- **QGIS Plugin Page**: [plugins.qgis.org/plugins/geoai](https://plugins.qgis.org/plugins/geoai)

The one-click installation approach was inspired by [TerraLab's AI Segmentation plugin](https://github.com/TerraLabAI/QGIS_AI-Segmentation). Credits to the TerraLab AI team for pioneering this pattern. If you find the GeoAI plugin useful, please give it a thumbs-up on the [QGIS plugin page](https://plugins.qgis.org/plugins/geoai) so more people can discover it. Stay tuned for more detailed tutorials on individual tools like instance segmentation, forest segmentation, and training data export.
