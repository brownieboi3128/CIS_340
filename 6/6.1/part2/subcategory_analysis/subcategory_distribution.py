import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Sample - Superstore.csv')

# Create categorical plot for sub-categories
plt.figure(figsize=(15, 6))
g = sns.catplot(data=df,
                x='Sub-Category',
                kind='count',
                height=6,
                aspect=2,
                order=df['Sub-Category'].value_counts().index)

# Customize the plot
g.fig.suptitle('Distribution of Product Sub-Categories', y=1.02)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
