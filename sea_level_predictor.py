
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data
df = pd.read_csv("C:/Users/YASH/OneDrive/Desktop/scipy.stats.linregress/epa-sea-level.csv")

# Create scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

# Create first line of best fit (for all data)
res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_all = pd.Series(range(1880, 2051))
y_all = res_all.slope * x_all + res_all.intercept
plt.plot(x_all, y_all, 'r', label='Best Fit Line: All Data')

# Create second line of best fit (from year 2000)
df_recent = df[df['Year'] >= 2000]
res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
x_recent = pd.Series(range(2000, 2051))
y_recent = res_recent.slope * x_recent + res_recent.intercept
plt.plot(x_recent, y_recent, 'g', label='Best Fit Line: Since 2000')

# Add labels and title
plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.legend()

# Save and show plot
plt.savefig('sea_level_plot.png')
plt.show()
