import pandas as pd

# 1. Load the dataset
df = pd.read_csv("uae_used_cars_10k.csv")

# Normalize column names (strip spaces, convert to lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 2. Check if required columns exist
required_columns = ['make', 'model', 'year', 'price_used']
missing_columns = [col for col in required_columns if col not in df.columns]

# Handle missing columns
if missing_columns:
    print(f" Missing columns: {', '.join(missing_columns)}")
    
    # Check if 'price_usd' column is missing and try to find an alternative column for price
    if 'price' in df.columns:
        #print(" 'price' column found, using it as 'price_used' for calculations.")
        df['price_used'] = df['price']
    else:
        print(" No price column found. Exiting.")
        exit()

else:
    print(" All required columns found.")

# 3. Average price by brand, model, and year
avg_price = df.groupby(['make', 'model', 'year'])['price_used'].mean().reset_index().sort_values(by='price_used', ascending=False)
print("Top 10 car brands, models, and years by average price:")
print(avg_price.head(10))

# 4. Top 10 most common brands
common_brands = df['make'].value_counts().head(10)
print("\nMost common car brands:")
print(common_brands)

# 5. Top 10 most common (brand, model) pairs
common_models = df.groupby(['make', 'model']).size().sort_values(ascending=False).head(10)
print("\nMost common car models:")
print(common_models)
