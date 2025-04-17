import pandas as pd

# 1. Load the dataset
df = pd.read_csv("uae_used_cars_10k.csv")  # Replace with the actual file path

# 2. Normalize column names: lowercase, remove spaces, use underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 3. Remove duplicate entries
df.drop_duplicates(inplace=True)

# 4. Handle missing or invalid values
# Drop rows with critical missing values
df.dropna(subset=['make', 'model', 'year', 'price', 'mileage'], inplace=True)

# Convert year, price, and mileage to numeric (handle invalid formats)
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

# Drop rows again if conversion made them NaN
df.dropna(subset=['year', 'price', 'mileage'], inplace=True)

# 5. Filter out unrealistic or outlier entries
df = df[(df['year'] >= 1980) & (df['year'] <= 2025)]
df = df[(df['price'] > 0) & (df['mileage'] > 0)]

# 6. Rename columns for clarity (optional)
df.rename(columns={
    'make': 'brand',
    'price': 'price_used',
    'mileage': 'mileage_km'
}, inplace=True)

# 7. Preview cleaned data
print("Cleaned dataset preview:")
print(df.head())

# Optional: Save to new CSV
df.to_csv("cleaned_uae_used_cars.csv", index=False)
