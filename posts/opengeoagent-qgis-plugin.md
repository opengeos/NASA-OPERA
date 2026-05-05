---
title: "OpenGeoAgent: An Open-Source Multimodal AI Agent for Geospatial Analysis in QGIS"
date: 2026-05-03
authors:
  - name: Qiusheng Wu
    email: qwu18@utk.edu
    orcid: 0000-0001-5437-4073
    url: https://gishub.org
description: Introducing OpenGeoAgent, an open-source multimodal AI agent that automates geospatial analysis and visualization in QGIS through natural language and voice commands.
thumbnail: https://img.youtube.com/vi/5zkXQlHUsu8/maxresdefault.jpg
tags:
  - OpenGeoAgent
  - QGIS
  - GeoAI
  - WhiteboxTools
  - Google Earth Engine
keywords:
  - OpenGeoAgent
  - GeoAgent
  - QGIS Plugin
  - Multimodal AI Agent
  - Natural Language GIS
  - WhiteboxTools
  - Google Earth Engine
  - Voice Dictation
---

# OpenGeoAgent: An Open-Source Multimodal AI Agent for Geospatial Analysis in QGIS

I am excited to introduce [OpenGeoAgent](https://github.com/opengeos/GeoAgent), a new open-source multimodal AI agent for automated geospatial analysis and visualization. The agent accepts both text prompts and images, returns text and images, and runs your analysis under the hood by calling tools you can inspect and reuse. It supports three execution environments: a QGIS plugin, Jupyter notebooks, and standalone Python scripting. This tutorial focuses on the QGIS plugin, with notebook and scripting tutorials to follow in future posts.

If you have ever wanted to build a watershed, mosaic a year of Sentinel-2 imagery, or compute NDVI without writing a single line of code, this is the workflow you are looking for. You can even talk to the agent with your microphone, no typing required.

:::{iframe} https://www.youtube.com/embed/5zkXQlHUsu8
:width: 100%
Video tutorial: OpenGeoAgent QGIS Plugin Tutorial
:::

## What You Will Need

- [QGIS](https://qgis.org) desktop (any standard installation works).
- A [ChatGPT subscription](https://chat.openai.com) (recommended) or an API key from a supported provider: OpenAI, Anthropic, Amazon Bedrock, Google Gemini, or a local [Ollama](https://ollama.com) server.
- Optional: an OpenAI API key for voice dictation and image generation. These features are billed by usage rather than the flat ChatGPT subscription.

## Install the Plugin

The plugin is published in the official QGIS Plugin Repository:

1. Open **Plugins > Manage and Install Plugins**.
2. Search for **OpenGeoAgent**.
3. Click **Install Plugin**.

After installation, an **OpenGeoAgent** menu appears in the QGIS menu bar with four entries: **Settings**, **Open Chat**, **Check for Updates**, and **About**.

## Configure the Settings

Open **OpenGeoAgent > Settings** to set up the plugin.

### Install dependencies

The agent supports several modes (general QGIS, WhiteboxTools, Earth Engine, and more), each with its own Python dependencies. On the **Installer** tab, click **Install All** to install every dependency at once. This is the easiest option if you plan to explore all modes.

### Choose an AI provider

Switch to the **Models** tab. The simplest setup is to log in with your ChatGPT subscription. Click the ChatGPT login button and follow the prompts. Because subscriptions are a fixed monthly cost, you do not have to monitor token usage.

If you prefer an API key, the plugin supports OpenAI, Anthropic, Amazon Bedrock, Google Gemini, and local Ollama. Voice dictation and image generation always require an OpenAI key, which is separate from the ChatGPT subscription. Voice dictation costs roughly one cent per request, while image generation typically runs a few cents per image, so monitor usage if you enable them.

A local Ollama server can keep everything offline if you have a capable GPU, but expect slower responses and weaker tool calling than the cloud providers.

### Test the connection

At the bottom of the **Models** tab, click **Test Provider**. A success message at the top of the dialog confirms the agent is ready to use.

## The Chat Panel

Open the chat panel from **OpenGeoAgent > Open Chat**. The interface has a few important controls.

- **Agent mode** sets the toolset the agent has access to. Modes include general QGIS, WhiteboxTools, Earth Engine Data Catalog, NASA Earthdata, and STAC. Each mode exposes a different set of geoprocessing tools.
- **Model selector** lets you switch language models on the fly, which is handy for comparing responses across providers.
- **Permissions** controls how the agent invokes tools. **Trust auto-approve** is the most convenient choice for personal use.
- **Voice dictation** transcribes your speech into the prompt box. Press `Ctrl+Alt+Space` to start and stop recording.
- **Sample prompts** offers a dropdown of starter ideas for each mode.

To send a prompt, type or dictate, then press `Ctrl+Enter`. Long-running jobs appear in the jobs panel and can be cancelled at any time.

## Example 1: Map Navigation and Multimodal Prompts

Start with something simple to confirm everything works. With the chat panel open, send:

> Zoom to Seattle.

The agent figures out the coordinates and pans the canvas. You do not need to supply a bounding box.

The plugin is multimodal, which means you can attach screenshots to your prompts. Use the **Screenshot** dropdown to capture the map canvas, the full QGIS window, or a region you draw with the mouse. Attach an image and ask:

> What is in the image?

The agent describes what it sees: overhead imagery, streets, a red polygon outline, and so on. This is useful when you want the agent to interpret a map you have already styled.

## Example 2: Hydrological Analysis with WhiteboxTools

Switch the agent mode to **WhiteboxTools**. Load a digital elevation model (DEM) into QGIS. The official sample dataset on the [GitHub repository](https://github.com/opengeos/GeoAgent) includes a DEM, NAIP imagery, and a building footprint layer that you can use to follow along.

Send these prompts in order, pressing `Ctrl+Enter` after each one:

1. `Create a hillshade for the DEM.`
2. `Fill the depressions in the DEM.`
3. `Calculate flow accumulation based on the filled DEM.`
4. `Extract the stream network as vector data with a threshold of 10000 pixels.`
5. `Use red color for the stream network.`
6. `What is the total length of the stream network?`

Each step shows the tool that ran and the output that was saved, so you can see exactly which WhiteboxTools function was called. The whole pipeline (fill, flow accumulation, thresholding, vectorization, styling, and length computation) finishes in well under a minute. Doing the same workflow by hand would take several minutes of clicking and saving.

Every step also exposes a **Copy snippet** button that returns the underlying Python code. Paste it into a script for a fully reproducible version of the workflow.

## Example 3: Cloud Data Analysis with Google Earth Engine

Switch the agent mode to **Earth Engine Data Catalog**. This mode requires the [Earth Engine Data Catalogs plugin](https://github.com/opengeos/qgis-gee-data-catalogs-plugin) to be installed and authenticated with your Google Cloud project ID.

Try these prompts to explore global elevation and Sentinel-2 imagery without downloading any raw data:

1. `Add the global NASA DEM.`
2. `Use a terrain color palette.`
3. `Clip the DEM to the United States.`
4. `Add a cloud-free Sentinel-2 image over Seattle for summer 2025.`
5. `Use a max value of 0.3 for visualization.`
6. `Use a false color composite.`
7. `Calculate NDVI.`
8. `Extract vegetation using an NDVI threshold of 0.2.`
9. `Calculate NDWI.`

The agent picks the right Earth Engine collection, applies the cloud-masking and reducer logic, and adds the result as a tiled layer in QGIS. As with WhiteboxTools, the **Copy snippet** button returns ready-to-run Earth Engine Python code.

## Workflow Tips

- **Voice dictation**: press `Ctrl+Alt+Space` to start and stop recording. The plugin uses GPT-4o mini transcribe, which handles short geospatial commands quickly and cheaply.
- **Reproducibility**: every tool call has a **Copy snippet** button so you can rebuild any analysis in a Python script or notebook.
- **Chat history**: use **Export** in the chat panel to save the full conversation as a Markdown file. Saving the QGIS project also preserves the chat history with the project.
- **Model comparison**: switch models between prompts to A/B test how different LLMs handle the same geospatial task.

## Resources

- GitHub repository: [github.com/opengeos/GeoAgent](https://github.com/opengeos/GeoAgent)
- QGIS plugin homepage: [geoagent.gishub.org/qgis-plugin](https://geoagent.gishub.org/qgis-plugin)
- Video tutorial: [youtu.be/5zkXQlHUsu8](https://youtu.be/5zkXQlHUsu8)

OpenGeoAgent is brand new and under active development. If you run into bugs or have feature ideas, please open an issue on GitHub. Tutorials covering the Jupyter notebook interface and the standalone Python scripting workflow are coming soon, so subscribe on [YouTube](https://youtube.com/@giswqs) or follow the [RSS feed](/rss.xml) to catch them as they are released.
