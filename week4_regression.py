# Step 1: Import the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 2: Load the dataset
df = pd.read_excel("Sample data (1).xlsx")

# Step 3: Select features and target
# Features are the columns used to predict sales.
# Target is the value we want to predict.

features = [
    "Units Sold",
    "Manufacturing Price",
    "Sale Price",
    "Discounts",
    "COGS"
]

X = df[features]
y = df[" Sales"]

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 5: Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict sales
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Regression Model Results")
print("------------------------")
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
print("Mean Absolute Error:", round(mae, 2))
print("R-squared Score:", round(r2, 4))

# Step 8: Compare actual and predicted sales
comparison = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": y_pred.round(2)
})

print("\nActual Sales vs Predicted Sales")
print(comparison.head(10))

# Step 9: Predict sales for a sample input
sample_data = pd.DataFrame({
    "Units Sold": [1000],
    "Manufacturing Price": [10],
    "Sale Price": [20],
    "Discounts": [1000],
    "COGS": [8000]
})

predicted_sales = model.predict(sample_data)

print("\nPredicted Sales for Sample Input:", round(predicted_sales[0], 2))