import pandas as pd


df = pd.read_csv("uae_used_cars_10k.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

required_columns = ['make', 'model', 'year', 'price_used']
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    print(f" Missing columns: {', '.join(missing_columns)}")
    
    if 'price' in df.columns:
        df['price_used'] = df['price']
    else:
        print(" No price column found. Exiting.")
        exit()

else:
    print(" All required columns found.")

avg_price = df.groupby(['make', 'model', 'year'])['price_used'].mean().reset_index().sort_values(by='price_used', ascending=False)
print("Top 10 car brands, models, and years by average price:")
print(avg_price.head(10))

common_brands = df['make'].value_counts().head(10)
print("\nMost common car brands:")
print(common_brands)


common_models = df.groupby(['make', 'model']).size().sort_values(ascending=False).head(10)
print("\nMost common car models:")
print(common_models)
