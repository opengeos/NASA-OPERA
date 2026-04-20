---
title: DSWx
description: Notebook examples demonstrating reproducible Python workflows for the OPERA DSWx surface-water product.
thumbnail: ../images/logo.png
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: geo
  language: python
  name: python3
---

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/leafmap/blob/master/docs/maplibre/nasa_opera.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/opengeos/leafmap/HEAD)


Started in April 2021, the Observational Products for End-Users from Remote Sensing Analysis ([OPERA](https://www.jpl.nasa.gov/go/opera)) project at the Jet Propulsion Laboratory collects data from satellite radar and optical instruments to generate six product suites:

* a near-global Surface Water Extent product suite
* a near-global Surface Disturbance product suite
* a near-global Radiometric Terrain Corrected product
* a North America Coregistered Single Look complex product suite
* a North America Displacement product suite
* a North America Vertical Land Motion product suite

This notebook demonstrates how to search and visualize NASA OPERA DSWx data products interactively using the `leafmap` Python package.

```{code-cell} ipython3
# %pip install -U "leafmap[maplibre]" earthaccess
```

```{code-cell} ipython3
import leafmap.maplibregl as leafmap
```

To download and access the data, you will need to create an Earthdata login. You can register for an account at [urs.earthdata.nasa.gov](https://urs.earthdata.nasa.gov).

```{code-cell} ipython3
leafmap.nasa_data_login()
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[-114.6581, 36.1711], zoom=10, sidebar_visible=True, sidebar_width=460, add_sidebar=True
)
m.add_basemap("Satellite")
m.add("NASA_OPERA")
m.add_draw_control()
m
```

Pan and zoom to your area of interest. Select a dataset from the Short Name dropdown list. Click the "Search" button to load the available datasets for the region. The footprints of the datasets will be displayed on the map. Click on a footprint to display the metadata of the dataset.

![image](https://github.com/user-attachments/assets/bca2f4de-84d2-4429-b076-a982279d3eaa)

+++

The footprints of the datasets can be accessed as a GeoPandas GeoDataFrame:

```{code-cell} ipython3
m._NASA_DATA_GDF.head()
```

Select a dataset from the Dataset dropdown list. Then, select a layer from the Layer dropdown list. Choose a appropriate colormap, then click on the "Display" button to display the selected layer on the map.

+++

The water classification layer:

![image](https://github.com/user-attachments/assets/48e9a0d2-0560-4a34-b727-413e1592b4d5)

+++

The selected layer added to the map can be accessed as a xarray Dataset:

```{code-cell} ipython3
m._NASA_DATA_DS
```

To save the displayed layer as a GeoTIFF file:

```{code-cell} ipython3
m._NASA_DATA_DS.rio.to_raster("DSWx.tif")
```

To download all the available datasets for the region:

```{code-cell} ipython3
leafmap.nasa_data_download(
    m._NASA_DATA_RESULTS[:1], out_dir="data", keywords=["_WTR.tif"]
)
```
