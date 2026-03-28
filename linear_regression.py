import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Dataset
X = np.array([8, 10, 12, 14, 16]).reshape(-1, 1)
Y = np.array([10, 13, 16, 18, 20])

# 2. Create Model
model = LinearRegression()

# 3. Train Model
model.fit(X, Y)

# 4. Predict values
Y_pred = model.predict(X)

# 5. Calculate Error Metrics
mae = mean_absolute_error(Y, Y_pred)
mse = mean_squared_error(Y, Y_pred)
print("MAE:", mae)
print("MSE:", mse)

# 6. Predict new value
x_new = np.array([[20]])
y_new = model.predict(x_new)
print("Prediction for X=20:", y_new[0])

# 7. Plot Graph
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, Y_pred, color='red', label='Regression Line')

# Mark predicted point
plt.scatter(x_new, y_new, color='green', label='Predicted Point')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.show()