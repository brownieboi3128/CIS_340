import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('Sample - Superstore.csv')

# Create regression plot
sns.regplot(data=df, x='Discount', y='Profit')
plt.title('Profit vs Discount Regression Plot')
plt.show()
