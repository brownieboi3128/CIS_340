import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Sample - Superstore.csv')

# Convert Order Date to datetime and extract year
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year

# Create a grouped dataframe by Region and Year, summing the Sales
sales_by_region_year = df.groupby(['Region', 'Year'])['Sales'].sum().reset_index()

# Create the categorical plot
plt.figure(figsize=(12, 6))
g = sns.catplot(data=sales_by_region_year, 
                x='Year', 
                y='Sales', 
                col='Region', 
                kind='bar',
                col_wrap=2,
                height=4,
                aspect=1.5)

# Customize the plot
g.fig.suptitle('Sales by Region and Year', y=1.05)
plt.tight_layout()
