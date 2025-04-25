import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

#dataset
data = {
    'Age': [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
    'Experience': [10, 12, 4, 4, 21, 14, 3, 14, 13, 5, 3, 3, 9],
    'Rank': [9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7, 9],
    'Nationality': ['UK', 'USA', 'N', 'USA', 'USA', 'UK', 'N', 'UK', 'N', 'N', 'USA', 'UK', 'UK'],
    'Go': ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'YES', 'YES']
}
df = pd.DataFrame(data)

# categorical data to numeric
nationality_map = {'UK': 0, 'USA': 1, 'N': 2}
go_map = {'NO': 0, 'YES': 1}
df['Nationality'] = df['Nationality'].map(nationality_map)
df['Go'] = df['Go'].map(go_map)

#features and target
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# rain the decision tree model
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(dtree, feature_names=features, class_names=['NO', 'YES'], filled=True)
plt.title("Decision Tree for Comedy Show Attendance")
plt.show()

# Predict new data
prediction_1 = dtree.predict([[40, 10, 7, 1]])
print("Prediction (Rank 7):", "YES" if prediction_1[0] == 1 else "NO")

prediction_2 = dtree.predict([[40, 10, 6, 1]])
print("Prediction (Rank 6):", "YES" if prediction_2[0] == 1 else "NO")
