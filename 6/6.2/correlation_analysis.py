import pandas as pd

# Read the dataset
df = pd.read_csv('Sample - Superstore.csv')

# Compute correlations between specific variables
correlation_matrix = df[['Sales', 'Profit', 'Quantity', 'Discount']].corr()
print("\nCorrelation Matrix:")
correlation_matrix
