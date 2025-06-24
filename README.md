# Task 1 – Population Distribution Bar Chart

## 🎯 Objective
Visualize the top 10 most populous countries/entities for the latest year.

## 📁 Dataset
- Source: World Bank – _Population, total_ (indicator `SP.POP.TOTL`)
- Year used: 2023

## 🛠 Methodology
1. Load CSV using `pandas`, skipping metadata rows.
2. Remove empty "Unnamed" columns.
3. Detect the latest year with data (2023).
4. Extract top 10 entries.
5. Plot bar chart using `matplotlib` & `seaborn`.
6. Save chart as `images/top10_population.png`.

## 🔍 Insights
- Global population exceeded ~8.1 billion in 2023.
- India (~1.43 B) and China (~1.42 B) are the most populous.
- Other top countries: USA, Indonesia, Pakistan, Nigeria, Brazil, Bangladesh, Russia, Mexico.

## 🚀 How to Run
```bash
pip install -r requirements.txt
python Task1.py
