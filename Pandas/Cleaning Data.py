import pandas as pd

# Step 1: Read CSV and clean column names
df = pd.read_csv('data.csv')

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Step 2: Check the column names to ensure correct ones are being used
print("Column names:", df.columns)

# Step 3: Clean the 'Date' column (remove single quotes and convert to datetime)
# Remove single quotes around the Date values
df['Date'] = df['Date'].astype(str).str.replace("'", "")

# Check if Date column exists after cleaning
if 'Date' in df.columns:
    # Convert the 'Date' column to datetime, invalid dates will be set as NaT
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
else:
    print("Error: 'Date' column not found in the data.")

# Step 4: Handle missing values in 'Calories'
df['Calories'].fillna(df['Calories'].mean(), inplace=True)

# Step 5: Drop rows where 'Date' is NaT (invalid dates) or any NaN values
df.dropna(subset=['Date'], inplace=True)

# Step 6: Handle wrong data (e.g., 'Duration' too high)
# Set 'Duration' values above 180 to the median
df.loc[df['Duration'] > 180, 'Duration'] = df['Duration'].median()

# Step 7: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Final: Print the cleaned data
print(df.to_string())

# Optional: Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
