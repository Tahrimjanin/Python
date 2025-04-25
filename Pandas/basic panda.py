import pandas as pd #pandas use for big data manipulation and analysis

df = pd.read_csv('data.csv')

print(df.to_string())

#Pandas Series
# Create a simple Pandas Series from a list
a = [1, 7, 2]
myvar = pd.Series(a)
print("\n Simple Series:")
print(myvar)

# Accessing the first value of the Series
print("\nFirst value of the Series:", myvar[0])

# custom labels series
myvar_with_labels = pd.Series(a, index=["x", "y", "z"])
print("\nSeries with custom labels:")
print(myvar_with_labels)

# Create label
print("\nValue of label 'y':", myvar_with_labels["y"])

#Value Objects as Series
#Create a Pandas Series from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar_dict = pd.Series(calories)
print("\nSeries from dictionary:")
print(myvar_dict)

# Create a Series using only specific data from the dictionary
myvar_filtered = pd.Series(calories, index=["day1", "day2"])
print("\nFiltered Series:")
print(myvar_filtered)

# Create a DataFrame from two Series
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print("\nDataFrame from Series:")
print(df)

# Using loc to access rows in the DataFrame
print("\nRow 0 of the DataFrame:")
print(df.loc[0])

# Using loc to access multiple rows
print("\nRows 0 and 1 of the DataFrame:")
print(df.loc[[0, 1]])

# Create a DataFrame with named indexes
df_named = pd.DataFrame(data, index=["day1", "day2", "day3"])
print("\nDataFrame with named indexes:")
print(df_named)

# Access a row by its named index
print("\nRow with index 'day2':")
print(df_named.loc["day2"])

# Get the first 10 rows of the DataFrame
print("\nFirst 10 rows of the DataFrame:")
print(df.head(10))

# Get the last 5 rows of the DataFrame
print("\nLast 5 rows of the DataFrame:")
print(df.tail())

# Get information about the DataFrame
print("\nInformation about the DataFrame:")
print(df.info())

# Example of handling null values:
print("\nHandling null values:")
print(df.isnull().sum())  # Count null values in each column

# If necessary, drop rows with missing values in any column:
df_cleaned = df.dropna()  # Drop rows with null values
print("\nDataFrame after dropping rows with null values:")
print(df_cleaned)
