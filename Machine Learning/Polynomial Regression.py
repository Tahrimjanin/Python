import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Polynomial regression model 
mymodel = np.poly1d(np.polyfit(x, y, 3))

# Line for plotting the polynomial regression curve
myline = np.linspace(1, 22, 100)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

#  Polynomial Regression (Good fit)
axes[0].scatter(x, y, color='blue', label='Data points')
axes[0].plot(myline, mymodel(myline), color='red', label='Polynomial regression')
axes[0].set_title("Polynomial Regression - Good Fit")
axes[0].set_xlabel('Hour of the Day')
axes[0].set_ylabel('Speed')
axes[0].legend()

x_bad = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y_bad = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

mymodel_bad = np.poly1d(np.polyfit(x_bad, y_bad, 3))

myline_bad = np.linspace(min(x_bad), max(x_bad), 100)

# Polynomial Regression (Bad fit)
axes[1].scatter(x_bad, y_bad, color='green', label='Data points')
axes[1].plot(myline_bad, mymodel_bad(myline_bad), color='orange', label='Polynomial regression')
axes[1].set_title("Polynomial Regression - Bad Fit")
axes[1].set_xlabel('X values')
axes[1].set_ylabel('Y values')
axes[1].legend()


plt.tight_layout()
plt.show()

r_squared = r2_score(y, mymodel(x))
print(f"R-squared value for good fit: {r_squared}")

predicted_speed = mymodel(17)
print(f"Predicted speed at 17:00: {predicted_speed}")

r_squared_bad = r2_score(y_bad, mymodel_bad(x_bad))
print(f"R-squared value for bad fit: {r_squared_bad}")
