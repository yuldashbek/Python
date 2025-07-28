import pandas as pd

df = pd.read_csv('sales_data.csv')

print(df.head())
category_stats = df.groupby('Category').agg(
    Total_Quantity=('Quantity', 'sum'),
    Avg_Price=('Price', 'mean'),
    Max_Quantity=('Quantity', 'max')
).reset_index()

print("\nCategory-wise Statistics:")
print(category_stats)
product_sales = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

# For each category, get product with highest quantity
top_products = product_sales.loc[product_sales.groupby('Category')['Quantity'].idxmax()].reset_index(drop=True)

print("\nTop-Selling Product in Each Category:")
print(top_products)
df['Sales'] = df['Quantity'] * df['Price']

date_sales = df.groupby('Date')['Sales'].sum()
max_sales_date = date_sales.idxmax()
max_sales_amount = date_sales.max()

print(f"\nDate with highest sales: {max_sales_date} (Total Sales: {max_sales_amount})")


import pandas as pd


df = pd.read_csv('customer_orders.csv')


print(df.head())


customer_order_counts = df.groupby('CustomerID')['OrderID'].nunique().reset_index(name='OrderCount')
active_customers = customer_order_counts[customer_order_counts['OrderCount'] >= 20]

print("\nCustomers with 20+ orders:")
print(active_customers)

customer_avg_price = df.groupby('CustomerID')['Price'].mean().reset_index(name='AvgPrice')
high_avg_price_customers = customer_avg_price[customer_avg_price['AvgPrice'] > 120]
print("\nCustomers with Avg Price > $120:")
print(high_avg_price_customers)

product_stats = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', lambda x: (x * df.loc[x.index, 'Quantity']).sum())
).reset_index()


filtered_products = product_stats[product_stats['Total_Quantity'] >= 5]

print("\nProducts with Total Quantity >= 5:")
print(filtered_products)


