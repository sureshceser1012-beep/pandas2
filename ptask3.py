import pandas as pd

# 1. Load and Inspect
df = pd.read_csv("sales3.csv")

print("First 5 Rows:")
print(df.head())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# 2. Filter, Slice, and Add

filtered = df.loc[
    (df["units_sold"] > 50) & (df["store_id"] == 3),
    ["date", "product", "revenue", "units_sold"]
].copy()

filtered["revenue_per_unit"] = (
    filtered["revenue"] / filtered["units_sold"]
)

top_10 = filtered.sort_values(
    "revenue_per_unit",
    ascending=False
).head(10)

print("\nTop 10 Revenue Per Unit:")
print(top_10)


# 3. Group-by and Aggregate

store_summary = (
    df.groupby("store_id")
    .agg(
        total_units_sold=("units_sold", "sum"),
        average_revenue=("revenue", "mean")
    )
    .reset_index()
)

print("\nStore Summary:")
print(store_summary)


# 4. Pivot

product_pivot = (
    df.pivot_table(
        columns="product",
        values="units_sold",
        aggfunc="sum",
        fill_value=0
    )
)

print("\nProduct Pivot:")
print(product_pivot)