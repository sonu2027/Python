# Example of Supervised Learning: Linear Regression
# Let's start with a basic supervised learning example: Linear Regression.

# (A) Linear Regression in Scikit-learn
# Linear Regression is used to model the relationship between a dependent variable (target) and one or more independent variables (predictors).

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data: x - hours studied, y - marks obtained
x = np.array([[1], [2], [3], [4], [5]])  # Hours studied (independent variable) -> this are output
y = np.array([1, 2, 3, 4, 5])           # Marks obtained (dependent variable) -> this are inputg

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Plotting the results
# print dot in graph
plt.scatter(x, y, color='blue', label='Actual data') 
# plot the graph
plt.plot(x, y_pred, color='red', label='Regression line')
# name of x-axis
plt.xlabel('Hours studied')
# name of y-axis
plt.ylabel('Marks obtained')
# display the labels
plt.legend()
# show the graph
plt.show()

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Evaluating the model
# After training a model, you need to evaluate its performance. For regression models, common evaluation metrics are:
# Mean Absolute Error (MAE)
# Mean Squared Error (MSE)
# R-squared (R²)
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'Mean Absolute Error: {mae}')
print(f'R² Score: {r2}')


# Splitting Data into Training and Testing Sets
# It's important to split the data into training and testing sets so that the model can be evaluated on unseen data. Scikit-learn provides a utility function for this:

from sklearn.model_selection import train_test_split

# Example data
X = np.array([[1], [2], [3], [4], [5]])  # Features
y = np.array([1, 2, 3, 4, 5])           # Target

# Split data into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_test_pred = model.predict(X_test)

# Evaluate the model
mse_test = mean_squared_error(y_test, y_test_pred)
print(f'Mean Squared Error on Test Set: {mse_test}')