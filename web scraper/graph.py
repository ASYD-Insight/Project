import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('books.csv')
print("First few rows of the DataFrame:\n", df.head())
df['Price'] = pd.to_numeric(df['Price'].str.replace('£', ''), errors='coerce')
print("DataFrame Info:\n", df.info())
df['Initial'] = df['Title'].str[0].str.upper()
average_prices = df.groupby('Initial')['Price'].mean().sort_index()
print("Average Prices by Initial:\n", average_prices)
plt.figure(figsize=(40, 30))
average_prices.plot(kind='bar', color='blue')
plt.title('Average Price of Books by Initial Letter')
plt.xlabel('Initial Letter')
plt.ylabel('Average Price (£)')
plt.show()
