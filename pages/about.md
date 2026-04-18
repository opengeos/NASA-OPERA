---
title: About
description: This page provides an overview of the NASA OPERA project, including its objectives, technical approach, deliverables, project team and timeline, and acknowledgments.
thumbnail: images/logo.png
acknowledgments: null
---

# About

NASA's **Observational Products for End-Users from Remote Sensing Analysis ([OPERA](https://www.jpl.nasa.gov/go/opera))** project was established at the Jet Propulsion Laboratory (JPL) in 2020 to design, implement, and deliver satellite-derived data products that address the operational and scientific priorities identified by the Satellite Needs Working Group (SNWG). OPERA products span surface water dynamics, land surface change and disturbance, geodetic deformation, and vertical land motion, and are distributed through the NASA Earthdata archives. Although the products are freely available, many users still face challenges with discovery, data volume, cloud-based access, and integration into modern geospatial and AI-enabled workflows - particularly in desktop GIS environments.

This project, a collaboration between the **University of Tennessee** and **NASA JPL** led by Dr. [Qiusheng Wu](https://gishub.org), addresses those challenges by advancing OPERA product accessibility through open-source geospatial frameworks, native integration with the **[GeoAI](https://opengeoai.org)** Python package, and a dedicated **[NASA OPERA QGIS plugin](https://github.com/opengeos/qgis-nasa-opera-plugin)**. Together, these components bridge the gap between OPERA data availability, interactive visualization, and advanced AI-enabled analysis.

## Project Objectives

- Enable seamless discovery, visualization, and analysis of OPERA products within open-source geospatial frameworks.
- Provide native, standardized access to OPERA products within the GeoAI package for machine learning and deep learning workflows.
- Develop a NASA OPERA QGIS plugin that enables no-code and low-code access to OPERA products within a familiar desktop GIS environment.
- Develop cloud-native analytical workflows using cloud-computing platforms such as Google Earth Engine.
- Demonstrate AI and machine learning applications that leverage OPERA products in combination with complementary satellite datasets.
- Support OPERA stakeholder engagement through user-centered tools, examples, and training resources.

## Technical Approach

### Open-Source Framework Integration

OPERA products are being natively integrated into open-source geospatial frameworks, including **[Leafmap](https://leafmap.org)** and **[AnyMap](https://ts.anymap.dev)**, and a new **[MapLibre GL JS](https://maplibre.org)** plugin is under development to bring OPERA products into modern web-mapping applications. These integrations provide standardized, reusable APIs and interactive GUIs that support spatial and temporal subsetting, map-based visualization, and cloud-native data access across Python, JavaScript, and TypeScript environments.

### NASA OPERA QGIS Plugin

A dedicated **[NASA OPERA QGIS plugin](https://github.com/opengeos/qgis-nasa-opera-plugin)** enables direct, streamlined access to OPERA products within the QGIS desktop environment. The plugin supports product discovery with spatial, temporal, and product-type filters; interactive map-based previews; metadata inspection; and efficient data access from NASA Earthdata and cloud-hosted platforms such as Google Earth Engine. A curated set of Jupyter notebooks complements the plugin through the QGIS Notebook Plugin, allowing users to move smoothly from no-code exploration to programmatic analysis.

### GeoAI Integration

OPERA products are being integrated into the **[GeoAI](https://opengeoai.org)** package through standardized data loaders, preprocessing pipelines, and dataset abstractions aligned with OPERA formats and metadata conventions. The resulting workflows support feature extraction, temporal modeling, change detection, and multi-sensor data fusion, and are designed to interoperate with widely used deep learning frameworks. The effort also explores fine-tuning and transfer learning with Earth observation foundation models such as **Prithvi-EO-2.0** and **AlphaEarth**, plus feasibility studies of forecasting and anomaly-prediction scenarios built on OPERA time series.

### Cloud-Based and AI-Enabled Demonstrations

A suite of cloud-based demonstration applications showcases practical, AI-enabled uses of OPERA products on platforms such as **Google Earth Engine**, **AlphaEarth**, and the **Microsoft Planetary Computer**. Examples include multi-temporal analysis of surface water dynamics, detection and characterization of land surface disturbances, and exploratory assessment of deformation signals using OPERA products in combination with complementary satellite datasets — emphasizing reproducibility, scalability, and adaptability rather than operational production.

### Stakeholder Engagement and Training

The project treats stakeholder engagement and training as closely integrated efforts. Continuous two-way engagement with federal agency users and the broader OPERA community — including participation in the annual **OPERA Stakeholder Engagement Workshop** — guides technical priorities and product design. Hands-on training workshops, guided walkthroughs, and a series of **YouTube tutorials** complement live events and provide sustained, openly accessible learning resources for users at varying levels of technical expertise.

## Deliverables

- Open-source modules and plugins integrating OPERA products into Leafmap, AnyMap, and MapLibre GL JS.
- A fully documented NASA OPERA QGIS plugin enabling interactive access to OPERA products within QGIS.
- GeoAI package extensions providing standardized access and preprocessing support for OPERA products.
- Cloud-native and AI-enabled demonstration workflows combining OPERA products with GeoAI methods.
- Stakeholder-oriented application examples aligned with federal agency use cases.
- Publicly available training materials, documentation, and tutorials covering QGIS, cloud, and GeoAI workflows.

## Project Team and Timeline

This effort is led by **Dr. [Qiusheng Wu](https://gishub.org)** at the University of Tennessee, an established open-source geospatial software contributor and the creator and maintainer of widely adopted Python packages including **[Geemap](https://geemap.org)**, **[Leafmap](https://leafmap.org)**, **[SamGeo](https://samgeo.gishub.org)**, and **[GeoAI](https://opengeoai.org)**, as well as numerous QGIS plugins. The period of performance is **February 1, 2026 – September 26, 2027**. All materials are released publicly on GitHub to support adoption, reproducibility, and capacity building.

**Acknowledgments**

This project is supported by NASA Jet Propulsion Laboratory (JPL).
