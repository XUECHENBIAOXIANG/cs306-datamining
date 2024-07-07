import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
landslide_data = pd.read_csv("landslide_catalog.csv")
volcano_data = pd.read_csv("volcano_database.csv")


landslide_data['date'] = pd.to_datetime(landslide_data['date'], format='%m/%d/%y')

# Day plot for Landslide data
plt.figure(figsize=(10, 6))
landslide_data['date'].dt.day.value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Landslide Count by Day')
plt.xlabel('Day of the Month')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Week-of-day plot for Landslide data
plt.figure(figsize=(10, 6))
landslide_data['date'].dt.dayofweek.value_counts().sort_index().plot(kind='bar', color='lightgreen')
plt.title('Landslide Count by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(ticks=range(7), labels=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.tight_layout()
plt.show()