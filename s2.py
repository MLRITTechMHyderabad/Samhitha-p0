import pandas as pd

df = pd.read_csv("uae_used_cars_10k.csv")  

print("Original column names:")
print(df.columns)

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("\nNormalized column names:")
print(df.columns)

required_columns = ['make', 'model', 'year', 'price', 'mileage']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f"\nError: Missing columns: {missing_columns}")
else:
    df.drop_duplicates(inplace=True)
    df.dropna(subset=required_columns, inplace=True)
    
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

    df.dropna(subset=['year', 'price', 'mileage'], inplace=True)
    
    df = df[(df['year'] >= 1980) & (df['year'] <= 2025)]
    df = df[(df['price'] > 0) & (df['mileage'] > 0)]

    df.rename(columns={
        'make': 'brand',
        'price': 'price_used',
        'mileage': 'mileage_km'
    }, inplace=True)

    print("\n Cleaned dataset preview:")
    print(df.head())


    df.to_csv("cleaned_uae_used_cars.csv", index=False)

