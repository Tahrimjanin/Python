import numpy
from sklearn import linear_model
import matplotlib.pyplot as plt

X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#train logistic regression model
logr = linear_model.LogisticRegression()
logr.fit(X, y)

#Predict if tumor is cancerous for a given size
size_to_predict = numpy.array([3.46]).reshape(-1,1)
predicted = logr.predict(size_to_predict)
print("Prediction (0 = not cancerous, 1 = cancerous):", predicted[0])

log_odds = logr.coef_
odds = numpy.exp(log_odds)
print("Odds of being cancerous per 1mm increase in tumor size:", odds[0][0])

# Function to convert log-odds
def logit2prob(logr, X):
    log_odds = logr.coef_ * X + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds / (1 + odds)
    return probability
probabilities = logit2prob(logr, X)
print("Probabilities of being cancerous for each tumor size:")
for size, prob in zip(X.flatten(), probabilities.flatten()):
    print(f"Tumor size {size:.2f} cm -> Probability: {prob:.2f}")

# Optional: Visualization
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X, probabilities, color='red', label='Logistic Regression Curve')
plt.xlabel("Tumor Size (cm)")
plt.ylabel("Probability of Cancer")
plt.title("Logistic Regression Prediction")
plt.legend()
plt.grid(True)
plt.show()
