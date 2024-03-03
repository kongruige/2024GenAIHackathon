# Implementing a simple linear regression package

import numpy as np

# Model Training
def train_linear_regression_model(features, target):
    coefficients = np.linalg.inv(features.T.dot(features)).dot(features.T).dot(target)
    return coefficients

# Prediction
def predict_linear_regression(features, coefficients):
    predictions = features.dot(coefficients)
    return predictions

# Evaluation
def evaluate_linear_regression_model(predictions, actual_values):
    mse = np.mean((predictions - actual_values) ** 2)
    return mse

# Test the functions
# Generate sample data
np.random.seed(0)
features = np.random.rand(100, 3)
coefficients = np.array([2, 3, 4])
target = features.dot(coefficients) + np.random.normal(0, 0.1, 100)

# Train the model
model_coefficients = train_linear_regression_model(features, target)

# Make predictions
predicted_values = predict_linear_regression(features, model_coefficients)

# Evaluate the model
mse = evaluate_linear_regression_model(predicted_values, target)

print("Model Coefficients:", model_coefficients)
print("Mean Squared Error:", mse)