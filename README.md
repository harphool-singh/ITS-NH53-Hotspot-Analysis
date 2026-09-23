# 🚦 ITS Hotspot Analysis — NH-53 Road Accident Data (2020–2024)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![QGIS](https://img.shields.io/badge/QGIS-GIS_Mapping-589632?style=for-the-badge&logo=qgis)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

**Intelligent Transportation Systems (ITS) | 5th Semester Project**
*Spatio-Temporal Accident Hotspot Detection on National Highway 53, Gujarat, India*

</div>

---

## 📌 Project Overview

This project performs a comprehensive analysis of road accident data on **National Highway 53 (NH-53)** — the Bharuch to Surat stretch in Gujarat — covering years **2020 to 2024** (983 total accident records). The goal is to detect high-density accident hotspot zones using spatial clustering and heatmap visualization, with future potential for integration into **ADAS (Advanced Driver Assistance Systems)**.

### 🔑 Key Highlights
- **983 accident records** processed across 5 years (2020–2024)
- DMS (Degrees-Minutes-Seconds) GPS coordinates converted to decimal for GIS use
- K-means clustering applied in QGIS to group accident-dense zones
- KDE (Kernel Density Estimation) heatmap rendered as **GeoTIFF** output
- Study corridor: Bharuch (72.77°E) to Surat (73.67°E) along NH-53

---

## 📁 Repository Structure

```
ITS-NH53-Hotspot-Analysis/
│
├── main.py                 → Step 1: Merge all yearly Excel sheets into one combined CSV
├── m2.py                   → Step 2: Extract a single year (2020) from the Excel file
├── m3.py                   → Step 3: Clean null/empty rows and columns
├── m4.py                   → Step 4: Convert DMS coordinates to Decimal Degrees
├── dl1.py                  → Utility: Image downloader (for reference images)
│
├── data/
│   ├── NH-53 Accident.xlsx                    → Raw source: multi-sheet yearly Excel (2020–2023)
│   ├── 2022-24 BHARUCH-SURAT.xlsx             → Supplementary corridor data
│   ├── NH53_Accidents_2020.csv                → Extracted 2020 sheet
│   ├── NH53_Accidents_2020_Cleaned.csv        → After null removal
│   └── NH53_Accidents_2020_Cleaned_decimal.csv → With Lat/Lon in decimal format
│
├── gis/
│   ├── aQGIS.qgz           → QGIS project file (loads all layers, clustering, heatmap)
│   └── heapmapits.tif      → Final KDE heatmap raster output (GeoTIFF, 64 MB)
│
└── README.md
```

---

## 🗄️ Dataset Description

| Field | Details |
|---|---|
| Source | NH-53 Police/Traffic Department records |
| Years Covered | 2020, 2021, 2022, 2023, 2024 |
| Total Records | **983 accident entries** |
| Columns | `SRNO`, `Accident_Location`, `Latitude`, `Longitude` |
| Coordinate Format | Originally DMS (e.g., `N21° 06' 46.45"`) → converted to Decimal |
| Geographic Extent | Latitude ~21.10°N to 21.17°N / Longitude ~72.77°E to 73.67°E |

### Sample Records

| SRNO | Accident_Location | Latitude | Longitude |
|---|---|---|---|
| 1 | Bhatia | 21.112903 | 73.354567 |
| 2 | Hazira | 21.166286 | 73.671050 |
| 4 | Kikakui | 21.121164 | 72.777692 |
| 5 | Kikakui | 21.119908 | 72.789408 |

---

## ⚙️ Data Processing Pipeline

### Step 1 — `main.py` : Combine All Yearly Sheets

**Purpose:** The raw data comes as a single Excel file (`NH-53 Accident.xlsx`) with one sheet per year (named `2020`, `2021`, `2022`, etc.). This script merges all sheets into one unified CSV.

**What it does:**
- Opens the Excel file using `pd.ExcelFile()`
- Iterates through every sheet (skips the `ALL` summary sheet)
- Adds a `Year` column to each sheet's data
- Concatenates all yearly DataFrames using `pd.concat()`
- Saves the merged output to `NH53_Accidents_Combined.csv`

**Run it:**
```bash
python main.py
```

**Output:** `output/NH53_Accidents_Combined.csv`

---

### Step 2 — `m2.py` : Extract Single Year (2020)

**Purpose:** Isolates just the year 2020 data for individual analysis.

**What it does:**
- Loads `NH-53 Accident.xlsx` and reads only the sheet named `2020`
- Drops completely empty rows using `dropna(how='all')`
- Saves to a standalone CSV

**Run it:**
```bash
python m2.py
```

**Output:** `NH53_Accidents_2020.csv`

---

### Step 3 — `m3.py` : Data Cleaning

**Purpose:** Removes noise (empty rows and columns) from the 2020 CSV.

**Cleaning operations performed:**
| Operation | Method Used | Effect |
|---|---|---|
| Remove empty rows | `df.dropna(how='all')` | Drops rows where every column is NaN |
| Remove empty columns | `df.dropna(axis=1, how='all')` | Drops columns where every value is NaN |

**Run it:**
```bash
python m3.py
```

**Input:** `NH53_Accidents_2020.csv`
**Output:** `NH53_Accidents_2020_Cleaned.csv`

---

### Step 4 — `m4.py` : DMS → Decimal Degree Coordinate Conversion

**Purpose:** GPS coordinates recorded in the field are in **DMS format** (e.g., `N21° 06' 46.45"`). GIS tools require **Decimal Degrees**. This script converts them.

**Conversion Formula:**
```
Decimal Degrees = Degrees + (Minutes / 60) + (Seconds / 3600)
```
For South (S) or West (W) directions, the result is multiplied by -1.

**Example:**
```
N21° 06' 46.45"  →  21 + (6/60) + (46.45/3600)  =  21.112903°
E73° 21' 16.44"  →  73 + (21/60) + (16.44/3600)  =  73.354567°
```

**How the regex parser works:**
- Extracts direction character (N/S/E/W) using `re.search(r'[NSEW]', dms_str)`
- Extracts degree, minute, second values using `re.findall(r'(\d+(?:\.\d+)?)', dms_str)`
- Applies the formula and rounds to 6 decimal places

**Run it:**
```bash
python m4.py
```

**Input:** `NH53_Accidents_2020_Cleaned.csv`
**Output:** `NH53_Accidents_2020_Cleaned_decimal.csv` (adds `Latitude_decimal`, `Longitude_decimal` columns)

---

## 🗺️ Spatial Analysis in QGIS

After the Python pipeline, all data is loaded into **QGIS** for spatial clustering and heatmap generation.

### K-Means Clustering

K-Means clustering is used to group nearby accident points into defined hotspot zones.

| Parameter | Value Used | Reasoning |
|---|---|---|
| **Number of Clusters (K)** | **5** | Based on visual inspection of point density and Elbow Method |
| **Input Layer** | `NH53_Combined_Coordinates.csv` (983 points) | All years combined |
| **Fields Used** | `Latitude`, `Longitude` | Spatial coordinates only |
| **Algorithm** | QGIS K-Means Clustering (Processing Toolbox) | `native:kmeansclustering` |
| **Distance Metric** | Euclidean (default in QGIS) | Suitable for small geographic extents |
| **Iterations** | 10 (default QGIS) | Convergence for 983 points |

**How to run K-Means in QGIS:**
1. Load `NH53_Combined_Coordinates.csv` as a Delimited Text Layer (set Lat/Lon columns)
2. Open **Processing Toolbox** → search `K-Means Clustering`
3. Set Input Layer = your accident points
4. Set **Number of Clusters = 5**
5. Run → a `CLUSTER_ID` field (0–4) is added to each point
6. Style by `CLUSTER_ID` to visualise the 5 zones

**Elbow Method (How K=5 was chosen):**
```
K=2 → WCSS = high (underfitting, too broad)
K=3 → WCSS = decreasing
K=4 → WCSS = decreasing
K=5 → WCSS = elbow point (optimal)
K=6 → WCSS = marginal improvement only
K=7 → WCSS = diminishing returns
```
At K=5, the within-cluster-sum-of-squares (WCSS) shows a clear elbow, meaning adding more clusters beyond 5 gives minimal improvement.

---

### KDE Heatmap (Kernel Density Estimation)

After clustering, a **KDE heatmap** is generated to show continuous accident density across the highway.

| Parameter | Value Used |
|---|---|
| **QGIS Tool** | Heatmap (Kernel Density Estimation) |
| **Input Layer** | All 983 accident points |
| **Radius** | 1000 metres (1 km influence zone per point) |
| **Pixel Size** | 10 m × 10 m |
| **Kernel Shape** | Quartic (smooth gradients) |
| **Output Format** | GeoTIFF (`.tif`) |
| **Output File** | `heapmapits.tif` |

**Colour Scale Interpretation:**
| Colour | Risk Level | Meaning |
|---|---|---|
| 🔴 Red / Dark | Very High Risk | ≥ 15 accidents per km² |
| 🟠 Orange | High Risk | 10–15 accidents per km² |
| 🟡 Yellow | Moderate Risk | 5–10 accidents per km² |
| 🟢 Green | Low Risk | < 5 accidents per km² |

---

## 🚀 How to Run the Full Project

### Prerequisites

Install required Python libraries:
```bash
pip install pandas openpyxl xlrd
```

Install **QGIS** (free): https://qgis.org/en/site/forusers/download.html

---

### Full Step-by-Step Execution

#### 1. Clone the repository
```bash
git clone https://github.com/harphool-singh/ITS-NH53-Hotspot-Analysis.git
cd ITS-NH53-Hotspot-Analysis
```

#### 2. Update file paths in each script
Open each `.py` file and update the `file_path` variable to point to your local `data/` folder.

Example (change this in every script):
```python
# BEFORE (old hardcoded path)
file_path = r"C:\Users\harph\OneDrive\Desktop\ITS\New folder\NH-53 Accident.xlsx"

# AFTER (your local path)
file_path = r"C:\path\to\your\data\NH-53 Accident.xlsx"
```

#### 3. Run Python pipeline in order
```bash
python main.py    # Merges all years → NH53_Accidents_Combined.csv
python m2.py      # Extracts 2020 data → NH53_Accidents_2020.csv
python m3.py      # Cleans nulls → NH53_Accidents_2020_Cleaned.csv
python m4.py      # Converts coordinates → NH53_Accidents_2020_Cleaned_decimal.csv
```

#### 4. Open QGIS for spatial analysis
1. Open QGIS → `Project > Open` → select `gis/aQGIS.qgz`
2. The project loads with all layers pre-configured
3. To re-run K-Means: `Processing Toolbox > K-Means Clustering > K=5`
4. To re-run Heatmap: `Raster > Heatmap > Radius=1000m, Pixel=10m`
5. Export result as GeoTIFF

---

## 📊 Results Summary

| Cluster ID | Zone Name | Approximate Location | Accident Count |
|---|---|---|---|
| 0 | Zone A | Kikakui area (Lon ~72.78°E) | High |
| 1 | Zone B | Mid-corridor (Lon ~73.0°E) | Moderate |
| 2 | Zone C | Bhatia / Kim area (Lon ~73.35°E) | High |
| 3 | Zone D | Outer Surat approach (Lon ~73.5°E) | Moderate |
| 4 | Zone E | Hazira / Surat end (Lon ~73.67°E) | High |

---

## 🔮 Future Scope

- **Real-time integration** — Connect to live traffic/accident APIs for dynamic hotspot updates
- **ML severity prediction** — Train Random Forest or SVM on accident features to predict injury severity
- **ADAS integration** — Feed hotspot coordinates to onboard driver-assistance systems as geo-fenced warnings
- **Seasonal analysis** — Expand temporal analysis (monsoon vs. summer vs. winter accident patterns)
- **Multi-highway expansion** — Apply same pipeline to NH-48, NH-27, and other Gujarat highways

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.12 | Data processing scripting |
| Pandas | Latest | DataFrame operations, CSV/Excel I/O |
| OpenPyXL | Latest | Reading `.xlsx` files |
| Regex (`re`) | Built-in | DMS coordinate string parsing |
| QGIS | 3.x | GIS mapping, K-Means, KDE heatmap |
| GeoTIFF | — | Raster heatmap output format |

---

## 👤 Author

**Harphool Singh**
ITS Project — 5th Semester, CE/IT Department
📅 September – November 2025

---

## 📄 License

Academic project. Free to reference and build upon with attribution.

---

> *"Roads don't kill — uninformed roads do. Data-driven safety saves lives."*
