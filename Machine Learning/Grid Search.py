from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X = iris['data']
y = iris['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

default_model = LogisticRegression(max_iter=10000)
default_model.fit(X_train, y_train)
default_score = default_model.score(X_test, y_test)
print("Default C=1 Accuracy:", default_score)

C_values = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
scores = []

for c in C_values:
    model = LogisticRegression(C=c, max_iter=10000)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    scores.append(score)
    print(f"C={c} -> Accuracy={score}")

best_index = scores.index(max(scores))
best_C = C_values[best_index]
print(f"\nBest C value: {best_C} with Accuracy: {scores[best_index]}")
