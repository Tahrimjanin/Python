import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data-1.csv")
df.columns = df.columns.str.strip()
print("Available columns:", df.columns.tolist())

#features (X) and target (y)

X = df[['Weight', 'Volume']]
y = df['CO2']

model = LinearRegression()
model.fit(X, y)

predicted_CO2 = model.predict([[2300, 1300]])
print(f"\nPredicted CO2 for Weight=2300 and Volume=1300: {predicted_CO2[0]}")
