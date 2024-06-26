import matplotlib.pyplot as plt
import seaborn as sns

# Plot histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['numeric_column'], bins=30)  # Replace 'numeric_column' with appropriate value
plt.title('Distribution of Numeric Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Plot scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='column_x', y='column_y')  # Replace 'column_x' and 'column_y' with appropriate values
plt.title('Scatter Plot of Column X vs Column Y')
plt.xlabel('Column X')
plt.ylabel('Column Y')
plt.show()
