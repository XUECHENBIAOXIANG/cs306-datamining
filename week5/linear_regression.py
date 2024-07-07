import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load data from csv file
data = pd.read_csv('CCPP.csv')



# 2. Drop rows with missing values
data = data.dropna()

# 3. Get explanatory variables and dependent variable
X = data.iloc[:, :-1].values  # Explanatory variables (features)
Y = data.iloc[:, -1].values   # Dependent variable (target)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=False)


plt.figure(figsize=(12, 8))
plt.scatter(X_train[:, 0], Y_train, color='blue', label='Training Data')
plt.xlabel('Temperature (T)')
plt.ylabel('Net Hourly Electrical Energy Output (PE)')
plt.title('Training Data Visualization')
plt.legend()
plt.show()

# 6. Build a linear regression model
LR_Model = LinearRegression()

# 7. Data fitting
LR_Model.fit(X_train, Y_train)
print('Intercept:', LR_Model.intercept_)
print('Coefficients:', LR_Model.coef_)

# 8. Make predictions on test data
Y_pred = LR_Model.predict(X_test)

# 9. Evaluate the model
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(Y_test, Y_pred)
rmse = mean_squared_error(Y_test, Y_pred, squared=False)
r2 = r2_score(Y_test, Y_pred)

print('Mean Squared Error:', mse)
print('R-squared:', r2)

