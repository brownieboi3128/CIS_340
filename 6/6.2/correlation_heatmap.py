import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('Sample - Superstore.csv')

# Compute correlations
correlation_matrix = df[['Sales', 'Profit', 'Quantity', 'Discount']].corr()

# Create figure with specified size
plt.figure(figsize=(5, 5))

# Create heatmap
sns.heatmap(correlation_matrix, 
            annot=True,  # Show annotations
            square=True,  # Make it square
            cmap='coolwarm',
            vmin=-1, vmax=1)

plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
