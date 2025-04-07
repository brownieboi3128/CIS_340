import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Sample - Superstore.csv')

# Calculate total profit per category
category_profit = df.groupby('Category')['Profit'].sum().reset_index()

# Create the bar plot using catplot
plt.figure(figsize=(10, 6))
sns.catplot(data=category_profit, 
            x='Category', 
            y='Profit',
            kind='bar',
            height=6,
            aspect=1.5)

# Customize the plot
plt.title('Total Profit by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Profit ($)')

# Adjust layout
plt.tight_layout()
