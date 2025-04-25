import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

X = pd.DataFrame([[2300, 1.3]], columns=["Weight", "Volume"])

df = pd.read_csv("data-1.csv")

# Separate features and target variable
X = df[['Weight', 'Volume']]
y = df['CO2']

# Scale the features
scale = StandardScaler()
scaledX = scale.fit_transform(X)

# Train the regression model
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

# Predict CO2 for a car with 2300 kg weight and 1.3 liter volume
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])

# Output the prediction
print("Predicted CO2 emission:", predictedCO2[0])
