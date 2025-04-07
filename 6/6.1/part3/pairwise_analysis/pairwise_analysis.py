import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Sample - Superstore.csv')

# Extract year from Order Date
df['Year'] = pd.to_datetime(df['Order Date']).dt.year

# Create pairwise plot
sns.set_style("whitegrid")
pairplot = sns.pairplot(data=df,
                       vars=['Sales', 'Profit', 'Quantity', 'Discount'],
                       hue='Year',
                       palette='Blues')

# Set title
plt.suptitle('Pairwise Relationships between Sales Metrics by Year', y=1.02)

# Adjust layout
plt.tight_layout()
