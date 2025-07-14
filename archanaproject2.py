import pandas as pd

# Input file path
input_path = r"C:\Users\archa\OneDrive\Documents\GitHub\Learners-Repo\stock_market_june2025.csv"

# Output paths
cleaned_path = r"C:\Users\archa\OneDrive\Desktop\Project1\cleaned_stock_data.csv"
transformed_path = r"C:\Users\archa\OneDrive\Desktop\Project1\transformed_stock_data.csv"

# Read original CSV
try:
    df = pd.read_csv(input_path)
    print("✅ File loaded successfully.")
except Exception as e:
    print("❌ Error loading file:", e)
    exit()

# 🔹 CLEANING: Drop rows with any missing values
df_cleaned = df.dropna()
print(f"\n✅ Cleaned Data (rows without NA): {df_cleaned.shape[0]} rows")

# 🔹 TRANSFORMING: Add a new column with price difference if columns exist
if 'Open' in df.columns and 'Close' in df.columns:
    df_transformed = df_cleaned.copy()
    df_transformed['Price_Diff'] = df_transformed['Close'] - df_transformed['Open']
    print("✅ Transformed Data: Added 'Price_Diff' column.")
else:
    df_transformed = df_cleaned
    print("⚠️ 'Open' or 'Close' column not found. Skipping transformation.")

# Save to CSV
df_cleaned.to_csv(cleaned_path, index=False)
df_transformed.to_csv(transformed_path, index=False)

print(f"\n📁 Cleaned data saved to: {cleaned_path}")
print(f"📁 Transformed data saved to: {transformed_path}")

print(df)
print(df.tail(10))