# Employee Dataset — Data Cleaning, Analysis & Visualisation

A data analytics project that takes a deliberately messy employee CSV, cleans it systematically, analyses the data statistically, detects outliers, and visualises the findings — including a Pearson correlation heatmap.

---

## 📁 Repository Contents

| File | Description |
|---|---|
| `messy_dataset_Mukesh.csv` | Raw input dataset (10 records, 6 columns) |
| `Messy_Dataset_Analysis.ipynb` | Jupyter notebook — full cleaning, analysis & visualisation pipeline |
| `Messy_Dataset_Analysis_Slideshow.pptx` | Presentation — findings explained for a non-technical audience |

---

## 📊 Dataset Overview

The raw dataset (`messy_dataset_Mukesh.csv`) contains employee records with the following columns:

| Column | Description |
|---|---|
| `ID` | Unique employee identifier |
| `Name` | Employee name |
| `Age` | Age in years |
| `Country` | Country of employment (`NZ` or `AUS`) |
| `Salary` | Annual salary in NZD |
| `Join Date` | Date the employee joined |

---

## 🧹 Data Quality Issues Found

The raw dataset contained **7 types of problems** that were identified and fixed before any analysis:

| Issue | Detail |
|---|---|
| Duplicate row | Bob (ID=2) appeared twice — once missing Age, once missing Salary |
| Missing values | Eve had no ID, one row had no Name, Heidi had no Age or Salary, Grace had no Country, Charlie had no Join Date |
| Text in numeric columns | Age contained `thirty-eight`, Salary contained `sixty five thousand` |
| Invalid date | `2019-13-01` — month 13 doesn't exist; interpreted as `2019-01-13` (DD/MM swap) |
| Inconsistent country codes | Australia written as both `AU` and `AUS` |
| Wrong data types | All columns loaded as plain text due to mixed content |
| Missing ID | Eve's ID was missing — filled by detecting gaps in the existing ID sequence |

---

## 🔧 Cleaning Approach

| Step | Problem | Fix Applied |
|---|---|---|
| 1 | Text in Age/Salary | Replaced word strings with numbers, then cast to numeric |
| 2 | Invalid/mixed date formats | Tried `DD/MM/YYYY` → `YYYY-MM-DD` → `YYYY-DD-MM` in order |
| 3 | Inconsistent country codes | Renamed `AU` → `AUS` |
| 4 | Missing ID | Detected gaps in the ID sequence and filled positionally |
| 5 | Missing Age & Salary | Filled with column **median** — robust to skewed distributions |
| 6 | Missing Country | Filled with column **mode** (most frequent value = `NZ`) |
| 7 | Missing Join Date | Forward-filled from the previous row |
| 8 | Duplicate row | Kept first occurrence of Bob, discarded the second |

---

## 📈 Key Findings

### Statistical Summary

| Metric | Age | Salary (NZD) |
|---|---|---|
| Mean | 30.5 years | $62,556 |
| Median | 29.5 years | $62,000 |
| Min | 22 years | $55,000 |
| Max | 40 years | $72,000 |

### Team Breakdown
- **NZ:** 6 employees (67%)
- **AUS:** 3 employees (33%)
- AUS employees have a slightly higher median salary and wider salary range

### Outlier Detection (IQR Method)
No outliers were found in either Age or Salary:

| Column | Lower Bound | Upper Bound | Outliers |
|---|---|---|---|
| Age | 15 years | 47 years | None |
| Salary | $50,000 | $74,000 | None |

### Pearson Correlation Results

| Pair | r | Interpretation |
|---|---|---|
| Age ↔ Salary | **0.63** | Moderate positive — older employees earn more |

---

## 🚀 Running the Notebook

1. Upload `messy_dataset_Mukesh.csv` and `Mukesh_Analysis.ipynb` to [Google Colab](https://colab.research.google.com) or open in Jupyter
2. Install dependencies if needed:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```
3. Run all cells in order — each task builds on the previous one

### Notebook Structure

| Task | Description |
|---|---|
| Task 1 | Load raw CSV and inspect data types and missing values |
| Task 2 | Fix all 7 data quality issues |
| Task 3 | Statistical summary (mean, median, min, max, std dev) |
| Task 4 | IQR outlier detection for Age and Salary with bar charts |
| Task 5 | Country pie chart + salary boxplot by country |
| Task 6 | Pearson correlation matrix, heatmap, Age vs Salary scatter |

---

## 🛠 Libraries Used

- `pandas` — data loading, cleaning, and manipulation
- `numpy` — numerical operations and trend line fitting
- `matplotlib` — bar charts, scatter plots, pie charts, boxplots
- `seaborn` — correlation heatmap
- `scipy` — statistical support

---

## 💡 Notes

- **Why median for missing Age/Salary?** The data is right-skewed with a small sample. Median is more representative of a typical value than the mean in this case.
- **Why mode for missing Country?** Country is categorical — median doesn't apply. The mode (NZ) is the most reasonable default.
- **Why forward-fill for Join Date?** Dates follow a time sequence. Carrying the previous date forward is more logical than injecting a global average date.
- **Why IQR for outliers?** IQR is robust to skewed distributions and doesn't assume a normal distribution — appropriate for a small dataset like this.
