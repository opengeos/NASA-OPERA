---
title: GeoAI
description: The GeoAI QGIS plugin for geospatial AI with Moondream VLM, custom segmentation training/inference, and Segment Anything (SAM1/2/3).
thumbnail: ../images/logo.png
---

# GeoAI

[![QGIS Plugin](https://img.shields.io/badge/QGIS-Plugin-green.svg)](https://plugins.qgis.org/plugins/geoai)
[![GitHub](https://img.shields.io/badge/GitHub-geoai-blue.svg?logo=github)](https://github.com/opengeos/geoai)

A QGIS plugin that brings the [geoai](https://github.com/opengeos/geoai)
models into dockable panels (Moondream VLM, segmentation training and
inference, SamGeo), so you can keep QGIS as your main workspace while
experimenting with geospatial AI.

- **Repository**: <https://github.com/opengeos/geoai>
- **License**: MIT
- **Requires**: QGIS 3.28+, Python 3.10+, PyTorch (CUDA optional for GPU)

## Quick Start

- Create a Pixi project and install the dependencies.
- Install the QGIS plugin from the QGIS Plugin Manager.
- Enable the GeoAI plugin in QGIS.
- Restart QGIS.
- Open a GeoAI toolbar panel and try the sample datasets below.

## Video Tutorials

### Installation Tutorial

:::{iframe} https://www.youtube.com/embed/TJmZQXJK-IU
:width: 100%
GeoAI QGIS Plugin Installation on Linux and Windows
:::

### Usage Tutorial

:::{iframe} https://www.youtube.com/embed/8-OhlqeoyiY
:width: 100%
Full Usage Tutorial for the GeoAI QGIS Plugin
:::

:::{iframe} https://www.youtube.com/embed/Esr_e6_P1is
:width: 100%
GeoAI QGIS Plugin Short Demo
:::

## Features

Each tool lives inside a dockable panel that can be attached to either
side of the QGIS interface, so you can keep layers, maps, and models
visible simultaneously.

### Moondream Vision-Language Model Panel

- **Caption**: Generate descriptions of geospatial imagery (short, normal,
  or long).
- **Query**: Ask questions about images using natural language.
- **Detect**: Detect and locate objects with bounding boxes.
- **Point**: Locate specific objects with point markers.

### Segmentation Panel (Combined Training and Inference)

- **Tab 1 - Create Training Data**: Export GeoTIFF tiles from raster and
  vector data.
- **Tab 2 - Train Models**: Train custom segmentation models (U-Net,
  DeepLabV3+, FPN, etc.).
- **Tab 3 - Run Inference**: Apply trained models to new imagery and
  vectorize results. Vector outputs can optionally be smoothed or
  simplified for immediate use in GIS workflows.

### SamGeo Panel (Segment Anything Model)

- **Model Tab**: Load SAM models (SAM1, SAM2, or SAM3) with configurable
  backend and device settings.
- **Text Tab**: Segment objects using text prompts (e.g. "tree",
  "building", "road").
- **Interactive Tab**: Segment using point prompts (foreground/background)
  or box prompts drawn on the map.
- **Batch Tab**: Process multiple points interactively or from vector
  files/layers.
- **Output Tab**: Save results as raster (GeoTIFF) or vector (GeoPackage,
  Shapefile) with optional regularization (orthogonalize polygons, filter
  by minimum area).

### GPU Memory Management

- **Clear GPU Memory**: Release GPU memory and clear CUDA cache for all
  loaded models.

## Installation

### 1. Set Up the Environment

Installing the GeoAI QGIS plugin can be challenging due to the complicated
PyTorch/CUDA dependencies. Conda or mamba might take a while to resolve
dependencies, while pip might fail to install them properly. Using
[pixi](https://pixi.prefix.dev/latest) is recommended to avoid these
issues.

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

#### 3. Configure `pixi.toml`

Open `pixi.toml` in the `geo` directory and replace its contents with one
of the configurations below depending on your system. If you have an
NVIDIA GPU, run `nvidia-smi` to check your CUDA version.

**GPU with CUDA 12.x:**

```toml
[workspace]
channels = ["https://prefix.dev/conda-forge"]
name = "geo"
platforms = ["linux-64", "win-64"]

[system-requirements]
cuda = "12.0"

[dependencies]
python = "3.12.*"
pytorch-gpu = ">=2.7.1,<3"
qgis = "3.42.*"
pyqt = "5.15.*"
geoai = ">=0.24.0"
segment-geospatial = ">=1.2.0"
sam3 = ">=0.1.0.20251211"
libopenblas = ">=0.3.30"
```

**GPU with CUDA 13.x:**

```toml
[workspace]
channels = ["https://prefix.dev/conda-forge"]
name = "geo"
platforms = ["linux-64", "win-64"]

[system-requirements]
cuda = "13.0"

[dependencies]
python = "3.12.*"
pytorch-gpu = ">=2.7.1,<3"
qgis = "3.42.*"
pyqt = "5.15.*"
geoai = ">=0.24.0"
segment-geospatial = ">=1.2.0"
sam3 = ">=0.1.0.20251211"
```

**CPU only:**

```toml
[workspace]
channels = ["https://prefix.dev/conda-forge"]
name = "geo"
platforms = ["linux-64", "win-64"]

[dependencies]
python = "3.12.*"
pytorch-cpu = ">=2.7.1,<3"
qgis = "3.42.*"
pyqt = "5.15.*"
geoai = ">=0.24.0"
segment-geospatial = ">=1.2.0"
sam3 = ">=0.1.0.20251211"
libopenblas = ">=0.3.30"
```

#### 4. Install the Environment

From the `geo` folder:

```bash
pixi install
```

This step may take several minutes on first install depending on your
internet connection and system.

#### 5. Verify PyTorch + CUDA

If you have an NVIDIA GPU with CUDA, verify the installation:

```bash
pixi run python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available()); print('GPU:', (torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'))"
```

Expected output should look like:

- `PyTorch: 2.9.1`
- `CUDA available: True`
- `GPU: NVIDIA RTX 4090`

If CUDA is `False`, check that `nvidia-smi` works and that your NVIDIA
driver is up to date.

#### Request Access to SAM 3

To use SAM 3, request access at
<https://huggingface.co/facebook/sam3>. Once approved, authenticate and
download the model:

```bash
pixi run hf auth login
pixi run hf download facebook/sam3
```

**Note**: SAM 3 currently requires an NVIDIA GPU with CUDA support and
will not run on CPU-only systems.

### 2. Install the QGIS Plugin

#### Option A: QGIS Plugin Manager (Recommended)

GeoAI is available in the official
[QGIS plugin repository](https://plugins.qgis.org/plugins/geoai):

1. Launch QGIS: `pixi run qgis`.
2. Go to **Plugins > Manage and Install Plugins...**.
3. Switch to the **All** tab, search for `GeoAI`, select it, and click
   **Install Plugin**.

If an error dialog appears after installation, click **Close**, toggle
the checkbox next to the **GeoAI** plugin to enable it, close any
subsequent error dialogs, and restart QGIS to reload the plugin.

#### Option B: Helper Script

```bash
git clone https://github.com/opengeos/geoai.git
cd geoai/qgis_plugin
python install.py
# Remove with:
python install.py --remove
```

This links or copies the plugin into your active QGIS profile. Re-run
after pulling updates.

#### Option C: Manual Copy

Copy the `qgis_plugin` folder to your QGIS plugins directory:

- **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
- **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
- **Windows**: `C:\Users\<username>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`

### 3. Enable in QGIS

Launch QGIS (`pixi run qgis`), then go to **Plugins > Manage and Install
Plugins...** and enable **GeoAI**. After updates, toggle the plugin
off/on or restart QGIS to reload.

## Usage

### Moondream Vision-Language Model

Sample dataset:
[parking_lot.tif](https://huggingface.co/datasets/giswqs/geospatial/resolve/main/parking_lot.tif)

1. Click the **Moondream** button in the GeoAI toolbar (or
   **GeoAI > Moondream VLM**).
2. Load a Moondream model (default: `vikhyatk/moondream2`).
3. Select a raster layer or browse for an image file.
4. Choose a mode:
   - **Caption**: Generate a description of the image.
   - **Query**: Ask a question about the image.
   - **Detect**: Detect objects by type (e.g. "building", "car").
   - **Point**: Locate specific objects.
5. Click **Run**.
6. Results are displayed and optionally added to the map. Save the output
   table or vector layer to reuse detections later.

### Segmentation Panel (Create Data, Train, Inference)

Sample datasets:

- [naip_rgb_train.tif](https://huggingface.co/datasets/giswqs/geospatial/resolve/main/naip_rgb_train.tif)
- [naip_test.tif](https://huggingface.co/datasets/giswqs/geospatial/resolve/main/naip_test.tif)
- [naip_train_buildings.geojson](https://huggingface.co/datasets/giswqs/geospatial/resolve/main/naip_train_buildings.geojson)

1. Download the sample datasets or prepare your own imagery and vector
   labels. Store them in a folder accessible to the pixi project.
2. Click the **Segmentation** button in the GeoAI toolbar (or
   **GeoAI > Segmentation**).
3. Use the tabs at the top of the panel to switch between:
   - **Create Training Data**: Select input raster and vector labels,
     configure tile size and stride, and export tiles to a directory.
   - **Train Model**: Select the images and labels directories, choose
     model architecture (U-Net, DeepLabV3+, etc.), configure training
     parameters, and start training.
   - **Run Inference**: Select input raster layer or file, specify the
     trained model path, configure inference parameters, run inference,
     and optionally vectorize the results.

### SamGeo Panel (Segment Anything Model)

Sample datasets:

- [uc_berkeley.tif](https://huggingface.co/datasets/giswqs/geospatial/resolve/main/uc_berkeley.tif)
- [wa_building_image.tif](https://github.com/opengeos/datasets/releases/download/places/wa_building_image.tif)
- [wa_building_centroids.geojson](https://github.com/opengeos/datasets/releases/download/places/wa_building_centroids.geojson)
- [wa_building_bboxes.geojson](https://github.com/opengeos/datasets/releases/download/places/wa_building_bboxes.geojson)

1. Click the **SamGeo** button in the GeoAI toolbar (or
   **GeoAI > SamGeo**).
2. In the **Model** tab:
   - Select the SAM model version (SamGeo3/SAM3, SamGeo2/SAM2, or
     SamGeo/SAM1).
   - Configure backend (`meta` or `transformers`) and device (`auto`,
     `cuda`, `cpu`).
   - Click **Load Model** to initialize the model.
   - Select a raster layer or browse for an image file and click
     **Set Image**.
3. Choose a segmentation method:
   - **Text Tab**: Enter text prompts describing objects (e.g.
     "tree, building").
   - **Interactive Tab**: Click **Add Foreground Points** /
     **Add Background Points** and click on the map, or click **Draw Box**
     and drag a rectangle, then click **Segment by Points** or
     **Segment by Box**.
   - **Batch Tab**: Add multiple points interactively or load from a
     vector file/layer.
4. In the **Output** tab:
   - Select output format (Raster GeoTIFF, Vector GeoPackage, or Vector
     Shapefile).
   - For vector output, optionally enable regularization: check
     "Regularize polygons (orthogonalize)" and set Epsilon (simplification
     tolerance) and Min Area (filter small polygons).
   - Click **Save Masks** to export results.

### Clear GPU Memory

Click the **GPU** button in the GeoAI toolbar to release GPU memory from
all loaded models (Moondream, SamGeo, etc.) and clear the CUDA cache. Use
this frequently when switching between large models to prevent
out-of-memory errors.

### Plugin Update Checker

Go to **GeoAI > Check for Updates...** to see if a newer version is
available. Click **Check for Updates** to fetch the latest version info
from GitHub, then **Download and Install Update** to install it. Restart
QGIS to apply the update.

## Supported Model Architectures (Segmentation)

The QGIS plugin supports any models available through
[PyTorch Segmentation Models](https://smp.readthedocs.io/en/latest/models.html),
including:

- U-Net, U-Net++
- DeepLabV3, DeepLabV3+
- FPN (Feature Pyramid Network)
- PSPNet, LinkNet, MANet, PAN
- UperNet, SegFormer, DPT

## Supported Encoders (Segmentation)

- ResNet (34, 50, 101, 152)
- EfficientNet (b0-b4)
- MobileNetV2
- VGG (16, 19)

## Supported SAM Models (SamGeo)

- **SamGeo3 (SAM3)**: Latest version with text, point, and box prompts.
- **SamGeo2 (SAM2)**: Improved version with better performance.
- **SamGeo (SAM1)**: Original Segment Anything Model.

## Troubleshooting

- **Plugin missing after install**: Confirm the plugin folder exists in
  your QGIS profile path and that you restarted QGIS.
- **CUDA OOM**: Use the **GPU** button to clear cache, lower batch sizes,
  or switch to CPU for smaller runs.
- **Model download failures**: Check network/firewall, then retry loading
  models from the panel.

## Links

- [GeoAI Documentation](https://opengeoai.org)
- [SamGeo Documentation](https://samgeo.gishub.org)
- [GitHub Repository](https://github.com/opengeos/geoai)
- [Report Issues](https://github.com/opengeos/geoai/issues)
