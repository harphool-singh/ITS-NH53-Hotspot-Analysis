# 🚦 ITS Hotspot Analysis – NH-53 Road Accident Data

> **Intelligent Transportation Systems (ITS) Project**
> *Spatio-Temporal Hotspot Detection on National Highway 53 (Bharuch–Surat Corridor)*

---

## 📌 Overview

This project analyses multi-year road accident data (2020–2023) along **National Highway 53 (NH-53)** — the Bharuch to Surat corridor in Gujarat, India — to identify high-risk accident hotspot zones using **spatio-temporal clustering** and **statistical analysis** techniques.

The system is designed for potential integration into **ADAS (Advanced Driver Assistance Systems)** to deliver real-time hazard warnings and improve road safety outcomes.

---

## 🎯 Objectives

- Identify accident-prone **hotspot zones** along NH-53 using spatial clustering
- Detect **seasonal trends** and temporal patterns in accident frequency
- Generate **visualizations** (heatmaps, GIS maps) to highlight peak-risk segments
- Provide actionable insights for traffic safety authorities and ADAS integration

---

## 📁 Project Structure

`
ITS-NH53-Hotspot-Analysis/
│
├── main.py                              # Step 1 – Combine multi-year Excel sheets into one CSV
├── m2.py                                # Step 2 – Extract 2020 accident data from Excel
├── m3.py                                # Step 3 – Data cleaning (drop null rows/columns)
├── m4.py                                # Step 4 – Convert DMS coordinates to Decimal Degrees
├── dl1.py                               # Utility – Image downloader script
│
├── data/
│   ├── NH-53 Accident.xlsx              # Raw accident data (2020–2023, multi-sheet Excel)
│   ├── 2022-24 BHARUCH-SURAT.xlsx       # Supplementary corridor data
│   ├── NH53_Accidents_2020.csv          # Extracted 2020 data
│   ├── NH53_Accidents_2020_Cleaned.csv  # Cleaned 2020 data
│   └── NH53_Accidents_2020_Cleaned_decimal.csv  # With decimal lat/lon coordinates
│
├── gis/
│   ├── aQGIS.qgz                        # QGIS project file
│   └── heapmapits.tif                   # Generated heatmap raster (GeoTIFF)
│
└── README.md
`

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| **Python 3.x** | Core scripting language |
| **Pandas** | Data loading, cleaning, transformation |
| **QGIS** | GIS-based spatial visualization |
| **GeoTIFF / Raster** | Heatmap output format |
| **Regex** | DMS-to-Decimal coordinate parsing |
| **OpenPyXL / xlrd** | Excel file reading |

---

## Pipeline Overview

`
Raw Excel (NH-53 Accident.xlsx)
        |
        v
[main.py]  -->  Combine all yearly sheets --> NH53_Accidents_Combined.csv
        |
        v
[m2.py]   -->  Extract specific year (2020) --> NH53_Accidents_2020.csv
        |
        v
[m3.py]   -->  Clean nulls & empty rows --> NH53_Accidents_2020_Cleaned.csv
        |
        v
[m4.py]   -->  Convert DMS coords to Decimal --> NH53_Accidents_2020_Cleaned_decimal.csv
        |
        v
[QGIS]    -->  Spatial hotspot mapping --> heapmapits.tif (Heatmap)
`

---

## 🚀 Getting Started

### Prerequisites

`ash
pip install pandas openpyxl xlrd
`

QGIS is required for GIS visualization. Download from https://qgis.org

### Setup

1. Clone the repository:
   `ash
   git clone https://github.com/YOUR_USERNAME/ITS-NH53-Hotspot-Analysis.git
   cd ITS-NH53-Hotspot-Analysis
   `

2. Place your data files in the data/ folder.

3. Update file paths in each script to point to your local data directory.

4. Run the pipeline in order:
   `ash
   python main.py
   python m2.py
   python m3.py
   python m4.py
   `

5. Open QGIS and load gis/aQGIS.qgz to view the hotspot visualization.

---

## 📊 Key Features

- Multi-year data aggregation – Combines Excel sheets from 2020–2023 into a unified dataset
- Automated data cleaning – Removes null rows/columns systematically
- DMS to Decimal coordinate conversion – Enables GIS-compatible spatial analysis
- Heatmap generation – Visual hotspot raster output via QGIS
- ADAS-ready design – Architecture supports real-time hazard warning integration

---

## 🗺️ Study Area

| Parameter | Details |
|---|---|
| **Highway** | NH-53 (National Highway 53) |
| **Corridor** | Bharuch – Surat, Gujarat, India |
| **Data Period** | 2020 – 2023 |
| **Project Period** | September – November 2025 |

---

## 📈 Results

The QGIS heatmap (heapmapits.tif) highlights:
- High-risk zones – Accident clusters with highest density
- Moderate-risk segments – Seasonal or recurring accident spots
- Low-risk areas – Relatively safe stretches of NH-53

---

## 🔮 Future Scope

- Real-time accident data integration via traffic APIs
- Machine learning-based accident severity prediction (SVM, Random Forest)
- Integration with ADAS hardware for live hazard alerts
- Mobile dashboard for traffic safety officials
- Expansion to other national highways

---

## 👤 Author

Harph — ITS Project, 5th Semester
September – November 2025

---

## 📄 License

This project is for academic purposes. Feel free to reference with attribution.
