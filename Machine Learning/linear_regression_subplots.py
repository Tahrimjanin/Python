import matplotlib.pyplot as plt
from scipy import stats

# Good Fit Example
x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope1, intercept1, r1, p1, std_err1 = stats.linregress(x1, y1)

def predict_good(x):
    return slope1 * x + intercept1

model1 = list(map(predict_good, x1))
predicted_speed = predict_good(10)

# Bad Fit Example
x2 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y2 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope2, intercept2, r2, p2, std_err2 = stats.linregress(x2, y2)

def predict_bad(x):
    return slope2 * x + intercept2

model2 = list(map(predict_bad, x2))

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Good Fit Plot
axs[0].scatter(x1, y1, color='blue', label='Data Points')
axs[0].plot(x1, model1, color='red', label='Regression Line')
axs[0].set_title(f"Good Fit\nr = {r1:.2f} | Predicted speed (age 10) = {predicted_speed:.2f}")
axs[0].set_xlabel('Age')
axs[0].set_ylabel('Speed')
axs[0].legend()

# Bad Fit Plot
axs[1].scatter(x2, y2, color='orange', label='Data Points')
axs[1].plot(x2, model2, color='green', label='Regression Line')
axs[1].set_title(f"Bad Fit\nr = {r2:.2f}")
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')
axs[1].legend()

plt.tight_layout()
plt.show()

# Also print r values and prediction in console
print("Good Fit r-value:", r1)
print("Predicted speed for 10-year-old car:", predicted_speed)
print("Bad Fit r-value:", r2)
