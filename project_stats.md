Here is a comprehensive, structured project summary designed to get your student oriented, excited, and clear on their objectives.

---

# Research Project: Spatial Climatology of the Alpine Massifs using the ROMMA Network

## Introduction

### Presentation of the ROMMA Network

The **ROMMA** (*Réseau d'Observations Météorologiques du Massif Alpin*) is an associative meteorological observation network spread across the French Alps. Combining data from both amateur weather enthusiasts and professional installations, it provides exceptionally high-density, real-time tracking of environmental factors across complex terrain (covering regions like Isère, Savoie, Haute-Savoie, Hautes-Alpes, and Drôme).

Standard institutional meteorological reporting often relies on a small handful of regional reference stations, which flattens the rich microtopographical variations of mountain ranges into single spatial averages. The true power of the ROMMA network lies in its density: by capturing data from dozens of valleys, plateaus, and peaks simultaneously, it allows researchers to look "under the hood" of large-scale climate reports and examine how local mountain geography interacts with thermodynamic physics.

### Scientific Context: The Atmospheric Lapse Rate

The foundational physical principle underpinning this project is the **environmental lapse rate**—the rate at which atmospheric temperature decreases with an increase in altitude. Statistically, tracking this relationship across the Alps yields a strong linear regression model:

However, the atmosphere is rarely uniform. Topographical anomalies, such as mountain massifs acting as physical weather blocks, give rise to unique localized microclimates. One of the most famous examples within the network is **Pelouse de Darbounouse** in the Vercors—a high-altitude limestone depression (*doline/polje*) where cold air pooling creates intense nocturnal frost hollows, pulling its temperature drastically below what a generic altitude regression model expects.

---

## Description of Tasks

This project is structured as an end-to-end data science pipeline, moving from raw web extraction to advanced geospatial statistics and physical modeling.

### Task 1: Web Scraping & Regular Expressions

* **Objective:** Extract real-time and historical station profiles from the ROMMA web infrastructure.
* **Methodology:** Write a Python script using robust regular expressions (`re`) to parse HTML patterns. The scraper must target station identifying details, names, altitudes, and raw coordinates.
* **The Challenge:** You must construct a regex pattern capable of cleanly bypassing leading junk characters (such as punctuation or spaces inside `<b>` tags) to begin capturing station names cleanly at the first uppercase letter `[A-Z]`.

### Task 2: Algorithmic Coordinate Conversion

* **Objective:** Convert raw spatial coordinates from text representations into mathematical floats.
* **Methodology:** The coordinates scraped directly from individual station pages are stored in traditional DMS format (**Degrees, Minutes, Seconds**), e.g., `Longitude: 05° 50' 05" E`. You will write a Python function to parse these strings and apply the algorithmic conversion:

$$\text{Decimal Degrees (DD)} = \text{Degrees} + \frac{\text{Minutes}}{60} + \frac{\text{Seconds}}{3600}$$


* **The Challenge:** Build a automated test script confirming that coordinates are accurately transformed into standard floating-point tuples `(Latitude, Longitude)` suitable for mapping.

### Task 3: Geospatial Pipeline & Point-in-Polygon (PIP) Joins

* **Objective:** Automate the classification of weather stations into their respective mountain massifs (e.g., Vercors, Chartreuse, Belledonne).
* **Methodology:** Utilizing the **GeoPandas** and **Shapely** libraries, you will ingest open-source GeoJSON vector files containing the boundary polygons of the official French Alpine massifs (such as SAFRAN meteorological boundaries from data.gouv.fr).
* **The Challenge:** Execute a spatial join (`gpd.sjoin`) to mathematically calculate which massif polygon each station point falls inside. This bypasses manual data entry, creating an automated classification pipeline that screens out non-alpine outlier stations (e.g., stations located outside the geographic bounding box of the Alps) completely automatically.

### Task 4: Climatological Analysis & Visual Models

* **Objective:** Analyze and visually compare localized lapse rates.
* **Methodology:** Instead of treating the Alps as a single, uniform dataset, use the massif classifications generated in Task 3 to color-code your plots and calculate *separate* regression lines for individual massifs using `scipy.stats.linregress`.

You can use the graphic below to understand what your initial baseline looks like before classifying by massif. Notice how global outliers stand out from the generic trend line:

```
                          Initial Baseline Analysis
  Temperature (°C)
     ^
     |  . [Outlier: e.g., Non-Alpine station]
     |     . .
     |        \ .  .
     |         \  . .
     |          \   .
     |           \    .  . [Outlier: e.g., Darbounouse inversion]
     |            \     .
     +----------------------------------------> Altitude (m)
                   (Global Trend Line)

```

* **The Challenge:** By comparing the distinct mathematical slopes ($\Delta^\circ\text{C} / 100\text{m}$) of the Vercors, Chartreuse, and Belledonne, you will physically interpret their microclimates. You will investigate how phenomena like daytime solar mixing, nocturnal radiative cooling, and valley thermal inversions cause specific massifs to deviate from the global average.

---

## Bibliography & Project Resources

To execute this project, you will rely on the following primary documentation and code repositories:

* **ROMMA Official Portal:** [romma.fr](https://www.romma.fr/)
*Use this to understand the network structure, view live data streams, and read through monthly regional climatological summaries.*
* **Project Code Repository:** [github.com/macbuse/ROMMA](https://github.com/macbuse/ROMMA/)
*Access this repository to review existing script frameworks, regular expression utilities, and sample datasets compiled for the Alpine network.*
* **GeoPandas Documentation:** [geopandas.org](https://geopandas.org/)
*Refer to this resource for tutorials on handling geographic vector data, coordinate reference systems (CRS), and spatial data joins.*
