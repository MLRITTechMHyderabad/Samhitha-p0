import pandas as pd

# 1. Load the CSV file
df = pd.read_csv("uae_used_cars_10k.csv")  # Adjust the path if needed

# 2. Print column names to debug and verify
print("Original column names:")
print(df.columns)

# 3. Normalize column names: strip spaces, convert to lowercase, and replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Print normalized column names to verify
print("\nNormalized column names:")
print(df.columns)

# 5. Check if the necessary columns are present in the DataFrame
required_columns = ['make', 'model', 'year', 'price', 'mileage']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"\nError: Missing columns: {missing_columns}")
else:
    # 6. Remove duplicates
    df.drop_duplicates(inplace=True)

    # 7. Drop rows with missing values in critical columns
    df.dropna(subset=required_columns, inplace=True)

    # 8. Convert year, price, and mileage to numeric
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

    # 9. Drop rows with NaNs created by coercion
    df.dropna(subset=['year', 'price', 'mileage'], inplace=True)

    # 10. Filter out unrealistic data
    df = df[(df['year'] >= 1980) & (df['year'] <= 2025)]
    df = df[(df['price'] > 0) & (df['mileage'] > 0)]

    # 11. Rename columns for clarity
    df.rename(columns={
        'make': 'brand',
        'price': 'price_used',
        'mileage': 'mileage_km'
    }, inplace=True)

    # 12. Preview cleaned data
    print("\n✅ Cleaned dataset preview:")
    print(df.head())

    # 13. (Optional) Save cleaned dataset
    df.to_csv("cleaned_uae_used_cars.csv", index=False)

