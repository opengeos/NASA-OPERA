---
title: RTC-S1
---

# RTC-S1

## Overview

The **Radiometric Terrain-Corrected from Sentinel-1 ([RTC-S1](https://www.jpl.nasa.gov/go/opera/products/rtc-product))** product
provides calibrated, terrain-corrected SAR backscatter suitable for direct
analysis and change detection. RTC-S1 removes topographic distortions and
radiometric biases, enabling consistent multi-temporal comparison across
Sentinel-1 acquisitions, and is also used as input to OPERA's DSWx-S1 product.

## Product level & distribution

- Processing level: Level-2
- DAAC: ASF DAAC
- Project: NASA OPERA (JPL)

## Related product

- **RTC-S1-STATIC** — geometry layers (local incidence angle, layover/shadow
  masks, etc.) corresponding to RTC-S1 products.

## Applications

- Multi-temporal backscatter change detection
- Flood and surface-water mapping (input to DSWx-S1)
- Forest, wetland, and agricultural monitoring
- Analysis-ready SAR input for machine-learning workflows

## Inputs

- Sentinel-1 Single-Look Complex (SLC) data
- Precise Sentinel-1 orbit ephemerides
- Copernicus 30 m digital elevation model

## Coverage

Near-global — all land masses excluding Antarctica.

## References

- OPERA project page: <https://www.jpl.nasa.gov/go/opera>
- ASF DAAC: <https://asf.alaska.edu>
- RTC-S1 at ASF: <https://www.earthdata.nasa.gov/data/catalog/asf-opera-l2-rtc-s1-v1-1>
