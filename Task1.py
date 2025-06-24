import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
df = pd.read_csv('data/world_population.csv', skiprows=4)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Determine valid year columns with data
year_cols = [c for c in df.columns if c.isdigit()]
year_cols = [y for y in year_cols if df[y].notna().any()]
latest_year = sorted(year_cols)[-1]
print("Using latest_year:", latest_year)

# Extract top 10 and verify
df_subset = df[['Country Name', latest_year]].dropna()
top10 = df_subset.nlargest(10, latest_year)
print("Top 10 countries:\n", top10)

# Plot chart
plt.figure(figsize=(12, 6))
sns.barplot(x=latest_year, y='Country Name', data=top10, palette='viridis')
plt.title(f"Top 10 Most Populous Countries in {latest_year}")
plt.xlabel('Population')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('images/top10_population.png')
plt.show()
