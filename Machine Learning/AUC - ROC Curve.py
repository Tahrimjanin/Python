import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

n = 10000
y = np.array([0] * n + [1] * n)  

y_prob_1 = np.array(
    np.random.uniform(.25, .5, n // 2).tolist() +  # Class 0
    np.random.uniform(.3, .7, n).tolist() +  # Class 1
    np.random.uniform(.5, .75, n // 2).tolist()  # Class 0
)

y_prob_2 = np.array(
    np.random.uniform(0, .4, n // 2).tolist() +  # Class 0
    np.random.uniform(.3, .7, n).tolist() +  # Class 1
    np.random.uniform(.6, 1, n // 2).tolist()  # Class 1
)

print(f'Model 1 accuracy score: {accuracy_score(y, y_prob_1 > 0.5)}')
print(f'Model 2 accuracy score: {accuracy_score(y, y_prob_2 > 0.5)}')

print(f'Model 1 AUC score: {roc_auc_score(y, y_prob_1)}')
print(f'Model 2 AUC score: {roc_auc_score(y, y_prob_2)}')

def plot_roc_curve(true_y, y_prob):
    fpr, tpr, thresholds = roc_curve(true_y, y_prob)
    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

# Plot for model 1
plot_roc_curve(y, y_prob_1)
plt.title('Model 1 ROC Curve')
plt.show()

# Plot for model 2
plot_roc_curve(y, y_prob_2)
plt.title('Model 2 ROC Curve')
plt.show()
