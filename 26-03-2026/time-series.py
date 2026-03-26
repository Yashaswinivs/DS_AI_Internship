import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url)
df.columns = ["Month", "Passengers"]
df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m")
df.set_index("Month", inplace=True)

# Extract numerical features from datetime
df["MonthsSinceStart"] = (df.index - df.index[0]).days // 30

# Time Series Cross-Validation
tscv = TimeSeriesSplit(n_splits=5)
tscv_mse = []

for train_index, test_index in tscv.split(df):
    train_data, test_data = df.iloc[train_index], df.iloc[test_index]
    
    # Assuming a simple Linear Regression model for illustration
    model = LinearRegression()
    X_train, y_train = train_data[["MonthsSinceStart"]], train_data["Passengers"]
    X_test, y_test = test_data[["MonthsSinceStart"]], test_data["Passengers"]
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    tscv_mse.append(mse)

# Plotting
plt.plot(range(1, len(tscv_mse) + 1), tscv_mse, marker="o")
plt.title("Time Series Cross-Validation")
plt.xlabel("Fold")
plt.ylabel("Mean Squared Error (MSE)")
plt.show()