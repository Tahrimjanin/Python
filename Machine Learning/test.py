import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

# Fit a 4th-degree polynomial regression model
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

# Line to plot the polynomial regression
myline = np.linspace(0, 6, 100)

plt.figure(figsize=(14, 10))

# 1. Original Data
plt.subplot(2, 2, 1)
plt.scatter(x, y)
plt.title("Original Data")
plt.xlabel("Minutes in Shop")
plt.ylabel("Amount Spent")

# 2. Training Set
plt.subplot(2, 2, 2)
plt.scatter(train_x, train_y, color="blue")
plt.plot(myline, mymodel(myline), color='red')
plt.title("Training Set with Model")
plt.xlabel("Minutes in Shop")
plt.ylabel("Amount Spent")

# 3. Testing Set
plt.subplot(2, 2, 3)
plt.scatter(test_x, test_y, color="green")
plt.plot(myline, mymodel(myline), color='red')
plt.title("Testing Set with Model")
plt.xlabel("Minutes in Shop")
plt.ylabel("Amount Spent")

# 4. Prediction Example
predicted_value = mymodel(5)
plt.subplot(2, 2, 4)
plt.scatter(x, y, alpha=0.3)
plt.plot(myline, mymodel(myline), color='red')
plt.scatter(5, predicted_value, color='black', s=100, label=f'Predicted: {predicted_value:.2f}')
plt.legend()
plt.title("Prediction for 5 Minutes")
plt.xlabel("Minutes in Shop")
plt.ylabel("Amount Spent")

plt.tight_layout()
plt.show()

train_r2 = r2_score(train_y, mymodel(train_x))
test_r2 = r2_score(test_y, mymodel(test_x))

print("Training R2 Score:", round(train_r2, 3))
print("Testing R2 Score:", round(test_r2, 3))
print("Prediction for 5 minutes:", round(predicted_value, 2))
