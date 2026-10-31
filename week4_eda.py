# Week 4 - Task 1: Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel dataset
df = pd.read_excel("Sample data (1).xlsx")

# Step 2: Display the first five rows
print("\n--- First Five Rows ---")
print(df.head())

# Step 3: Display the number of rows and columns
print("\n--- Dataset Shape ---")
print(df.shape)

# Step 4: Display column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# Step 5: Display dataset information
print("\n--- Dataset Information ---")
df.info()

# Step 6: Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Step 7: Check for duplicate rows
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# Step 8: Display statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())

# Step 9: Display summary of categorical columns
print("\n--- Categorical Column Summary ---")
print(df.describe(include="object"))

# Step 10: Plot histograms for numerical columns
numeric_columns = df.select_dtypes(include="number").columns

if len(numeric_columns) > 0:
    df[numeric_columns].hist(figsize=(12, 8), bins=15)
    plt.suptitle("Distribution of Numerical Columns")
    plt.tight_layout()
    plt.show()
else:
    print("\nNo numerical columns available for histograms.")

# Step 11: Display correlation between numerical columns
if len(numeric_columns) >= 2:
    correlation = df[numeric_columns].corr()

    print("\n--- Correlation Between Numerical Columns ---")
    print(correlation)

    plt.figure(figsize=(10, 6))

    plt.imshow(correlation, cmap="coolwarm", aspect="auto", vmin=-1, vmax=1)
    plt.colorbar(label="Correlation")

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=45,
        ha="right"
    )

    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
else:
    print("\nNot enough numerical columns to calculate correlations.")

print("\nEDA completed successfully!")

# Step 12: Sales Analysis

print("\n--- Total Sales by Product ---")

sales_by_product = df.groupby("Product")[" Sales"].sum()

print(sales_by_product.sort_values(ascending=False))


print("\n--- Total Sales by Country ---")

sales_by_country = df.groupby("Country")[" Sales"].sum()

print(sales_by_country.sort_values(ascending=False))


print("\n--- Total Profit by Segment ---")

profit_by_segment = df.groupby("Segment")["Profit"].sum()

print(profit_by_segment.sort_values(ascending=False))


# Step 13: Visualize Sales by Product

sales_by_product.sort_values(ascending=False).plot(
    kind="bar",
    title="Total Sales by Product",
    xlabel="Product",
    ylabel="Total Sales"
)

plt.tight_layout()
plt.show()


# Step 14: Visualize Sales by Country

sales_by_country.sort_values(ascending=False).plot(
    kind="bar",
    title="Total Sales by Country",
    xlabel="Country",
    ylabel="Total Sales"
)

plt.tight_layout()
plt.show()


# Step 15: Visualize Profit by Segment

profit_by_segment.sort_values(ascending=False).plot(
    kind="bar",
    title="Total Profit by Customer Segment",
    xlabel="Segment",
    ylabel="Total Profit"
)

plt.tight_layout()
plt.show()

# Step 16: Monthly Sales Analysis

print("\n--- Monthly Sales Analysis ---")

monthly_sales = df.groupby(["Year", "Month Number", "Month Name"])[" Sales"].sum()

print(monthly_sales)


# Step 17: Visualize Monthly Sales Trend

monthly_sales = monthly_sales.reset_index()

monthly_sales["Period"] = (
    monthly_sales["Month Name"] + " " + monthly_sales["Year"].astype(str)
)

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_sales["Period"],
    monthly_sales[" Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month and Year")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)
plt.grid(True)

plt.tight_layout()
plt.show()


# Step 18: Analyze Yearly Sales

print("\n--- Total Sales by Year ---")

yearly_sales = df.groupby("Year")[" Sales"].sum()

print(yearly_sales)


# Step 19: Visualize Yearly Sales

yearly_sales.plot(
    kind="bar",
    title="Total Sales by Year",
    xlabel="Year",
    ylabel="Total Sales"
)

plt.tight_layout()
plt.show()