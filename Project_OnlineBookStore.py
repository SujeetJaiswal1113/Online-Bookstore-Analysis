import pandas as pd
books = pd.read_csv(
    r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\PYTHON\Project_OnlineBookStore\books.csv"
)
customers = pd.read_csv(
    r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\PYTHON\Project_OnlineBookStore\customers.csv"
)
orders = pd.read_csv(
    r"E:\AI Engineer\Lecture videos\DATA ANALYST learning from chat gpt\PYTHON\Project_OnlineBookStore\orders.csv"
)

print(books.head())
print(customers.head())
print(orders.head())

print(books.shape)
print(customers.shape)
print(orders.shape)

print(books.isnull().sum())
print(customers.isnull().sum())
print(orders.isnull().sum())

print(books.duplicated().sum())
print(customers.duplicated().sum())
print(orders.duplicated().sum())    

orders_customers = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="inner"
)

print(orders_customers.shape)

orders_books = pd.merge(
    orders,
    books,
    on="Book_ID",
    how="inner"
)

print(orders_books.shape)

final_df = pd.merge(
    orders,
    customers,
    on="Customer_ID"
)

final_df = pd.merge(
    final_df,
    books,
    on="Book_ID"
)

print(final_df.shape)

# Q1 Total Revenue. How much money did bookstore earn?
print(
    final_df["Total_Amount"].sum()
)

# Q2 Total Orders
print(
    final_df["Order_ID"].nunique()
)
# Q3 Total Customers
print(
    final_df["Customer_ID"].nunique()
)
# Q4 Average Order Value
print(
    final_df["Total_Amount"].mean()
)
# Q5 Top 10 Customers
print(
    final_df.groupby("Name")
    ["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# Q6 Top 10 Books
print(
    final_df.groupby("Title")
    ["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# Q7 Revenue by Genre
print(
    final_df.groupby("Genre")
    ["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)
# Q8 Revenue by Country
print(
    final_df.groupby("Country")
    ["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Date Analysis. Convert date:

final_df["Order_Date"] = pd.to_datetime(
    final_df["Order_Date"]
)
# Extract Year
final_df["Year"] = (
    final_df["Order_Date"]
    .dt.year
)
# Revenue by Year
print(
    final_df.groupby("Year")
    ["Total_Amount"]
    .sum()
)
# Orders by Year
print(
    final_df.groupby("Year")
    ["Order_ID"]
    .count()
)

# ==========================
# FEATURE ENGINEERING
# ==========================

# Create Price Category

def price_category(price):

    if price < 15:
        return "Cheap"

    elif price < 35:
        return "Medium"

    else:
        return "Expensive"

final_df["Price_Category"] = (
    final_df["Price"]
    .apply(price_category)
)

# Revenue by Price Category

print(
    final_df.groupby("Price_Category")
    ["Total_Amount"]
    .sum()
)

# Revenue by Price Category
def price_category(price):
    if price < 15:
        return "Cheap"
    elif price < 35:
        return "Medium"
    else:
        return "Expensive"

final_df["Price_Category"] = final_df["Price"].apply(price_category)

print(
    final_df.groupby("Price_Category")
    ["Total_Amount"]
    .sum()
    .sort_values(ascending=False)
)
# Monthly Revenue Trend
final_df["Month"] = final_df["Order_Date"].dt.month

print(
    final_df.groupby("Month")
    ["Total_Amount"]
    .sum()
)
# Top 5 Customers by Order Count
print(
    final_df.groupby("Name")
    ["Order_ID"]
    .count()
    .sort_values(ascending=False)
    .head()
)

final_df.info()
final_df.describe()

final_df.to_csv(
    "online_bookstore_final.csv",
    index=False
)
print("Dataset Exported Successfully")

#E1C233

#FFFDB9

#E8D166

#F0E199