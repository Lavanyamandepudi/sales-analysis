import pandas as pd

# Our sales data
data = {
    "Product": ["Pen", "Notebook", "Pen", "Bag", "Notebook", "Bag"],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Sales": [120, 200, 150, 300, 250, 280]
}

df = pd.DataFrame(data)

print("All sales data:")
print(df)
print()

print("Total sales:", df["Sales"].sum())
print("Average sale:", df["Sales"].mean())

print()
print("Total sales by product:")
print(df.groupby("Product")["Sales"].sum())