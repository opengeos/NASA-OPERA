---
title: DSWx
description: Overview of the OPERA Dynamic Surface Water eXtent (DSWx) product suite for mapping inland and near-shore surface water from optical and SAR observations.
thumbnail: images/logo.png
---

# DSWx

## Overview

The **Dynamic Surface Water eXtent ([DSWx](https://www.jpl.nasa.gov/go/opera/products/dswx-product-suite))** product suite maps the presence and
extent of inland and near-shore surface water using optical and synthetic
aperture radar (SAR) observations. DSWx supports OPERA's surface-water mission
objective, providing frequent, analysis-ready water maps for hydrology,
flood response, and long-term water-resource monitoring.

## Product level & distribution

- Processing level: Level-3
- DAAC: PO.DAAC
- Project: NASA OPERA (JPL)

## Sub-products

- **DSWx-HLS** — derived from the Harmonized Landsat Sentinel-2 (HLS) dataset.
- **DSWx-S1** — derived from Sentinel-1 C-band SAR, enabling water mapping
  under cloud cover and at night.

::::{grid} 1 1 2 2

:::{card}
:link: https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-HLS_V1
![DSWx-HLS](https://podaac.jpl.nasa.gov/Podaac/thumbnails/OPERA_L3_DSWX-HLS_PROVISIONAL_V0.png)
+++
**DSWx-HLS**
:::

:::{card}
:link: https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-S1_V1
![DSWx-S1](https://podaac.jpl.nasa.gov/Podaac/thumbnails/OPERA_L3_DSWx-S1_V1.jpg)
+++
**DSWx-S1**
:::

::::

## Applications

- Inland surface-water mapping and change detection
- Flood monitoring and disaster response
- Seasonal and inter-annual water-body dynamics
- Inputs for hydrologic and climate studies

## Inputs

- Harmonized Landsat Sentinel-2 (HLS) surface reflectance (DSWx-HLS)
- Sentinel-1 SAR backscatter, e.g. OPERA RTC-S1 (DSWx-S1)
- Digital elevation model and ancillary water-reference layers

## Coverage

Near-global land coverage, with cadence driven by the revisit of the
underlying HLS and Sentinel-1 observations.

## References

- OPERA project page: <https://www.jpl.nasa.gov/go/opera>
- PO.DAAC: <https://podaac.jpl.nasa.gov>
- DSWx-HLS at PO.DAAC: <https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-HLS_V1>
- DSWx-S1 at PO.DAAC: <https://podaac.jpl.nasa.gov/dataset/OPERA_L3_DSWX-S1_V1>
