import pandas as pd

# 🔹 Step 1: Try loading the dataset
try:
    df = pd.read_csv("uae_used_cars_10k.csv")
    print("✅ File loaded successfully.")
except FileNotFoundError:
    print("❌ Error: File not found.")
    df = None  # Assign None if file loading fails
except pd.errors.ParserError:
    print("❌ Error: Could not parse the file.")
    df = None  # Assign None if parsing fails

# Proceed only if the file was loaded successfully
if df is not None:
    # Print column names to check if 'year' exists
    print("Columns in the dataset:")
    print(df.columns)  # Verify column names

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Print normalized column names
    print("\nNormalized column names:")
    print(df.columns)  # Verify the normalization

    # 🔹 Step 2: Clean the data
    if 'year' in df.columns:  # Ensure 'year' exists before proceeding
        df.drop_duplicates(inplace=True)
        df.dropna(subset=['make', 'model', 'year', 'price', 'mileage'], inplace=True)

        # Convert columns to numeric
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

        # Filter out unrealistic data
        df = df[(df['year'] <= 2025) & (df['year'] >= 1980)]
        df = df[(df['mileage'] > 0) & (df['price'] > 0)]

        # Rename columns for clarity
        df.rename(columns={
            'make': 'brand',
            'price': 'price_used',
            'mileage': 'mileage_km'
        }, inplace=True)

        # Preview the cleaned data
        print("✅ Cleaned dataset preview:")
        print(df.head())
    else:
        print("❌ Error: 'year' column not found.")
else:
    print("❌ No data to clean, as file loading failed.")
