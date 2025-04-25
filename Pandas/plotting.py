import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.columns = df.columns.str.strip()

print("Column Names after cleaning:")
print(df.columns)
print("First few rows:")
print(df.head())

print("Data types of columns:")
print(df.dtypes)

if 'Duration' in df.columns and 'Calories' in df.columns:
    #convert
    df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')
    df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

    df.dropna(subset=['Duration', 'Calories'], inplace=True)

    # Basic Plot 
    df.plot()
    plt.title("Basic Line Plot")
    plt.show()

    # Scatter Plot
    df.plot(kind='scatter', x='Duration', y='Calories', color='blue')
    plt.title("Scatter Plot: Duration vs Calories")
    plt.show()

    # Scatter Plot
    df.plot(kind='scatter', x='Duration', y='Maxpulse', color='green')
    plt.title("Scatter Plot: Duration vs Maxpulse")
    plt.show()

    # Histogram
    df['Duration'].plot(kind='hist', bins=10, color='purple', edgecolor='black')
    plt.title("Histogram: Duration")
    plt.xlabel("Duration")
    plt.ylabel("Frequency")
    plt.show()

    # Histogram
    df['Calories'].plot(kind='hist', bins=10, color='orange', edgecolor='black')
    plt.title("Histogram: Calories")
    plt.xlabel("Calories")
    plt.ylabel("Frequency")
    plt.show()
else:
    print("The necessary columns 'Duration' or 'Calories' are not found in the data.")
