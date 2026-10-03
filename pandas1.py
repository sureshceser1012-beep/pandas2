import pandas as pd

# 1. Read CSV files
products = pd.read_csv("products.csv")

transactions = pd.read_csv(
    "transactions.csv",
    parse_dates=["date"]
)

# 2. Rename columns to snake_case
products.columns = (
    products.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

transactions.columns = (
    transactions.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 3. Fill missing price with median
products["price"] = products["price"].fillna(
    products["price"].median()
)

# 4. Join price and category
transactions = transactions.merge(
    products[["product_id", "price", "category"]],
    on="product_id",
    how="left"
)

# 5. Calculate total amount
transactions["total_amount"] = (
    transactions["quantity"] * transactions["price"]
)

# 6. Filter last 30 days
latest_date = transactions["date"].max()

last_30_days = transactions[
    transactions["date"] >= latest_date - pd.Timedelta(days=30)
]

# 7. Group by category
category_sales_report = (
    last_30_days
    .groupby("category")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
)

print("Category Sales Report:")
print(category_sales_report)