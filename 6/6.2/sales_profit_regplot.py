import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('Sample - Superstore.csv')

# Create regression plot
sns.regplot(data=df, x='Sales', y='Profit')
plt.title('Profit vs Sales Regression Plot')
plt.show()
