import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("uae_used_cars_10k.csv" )
# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# 1. Summary statistics and key metrics
print("Summary Statistics:\n")
print(df.describe(include='all'))

# 2. Top 10 most listed car models
most_common_models = df['model'].value_counts().head(10)
print("\nTop 10 Most Listed Car Models:")
print(most_common_models)

# 3. Cars offering the best resale value
# Create a value ratio: price divided by mileage (adding 1 to avoid division by zero)
df['value_ratio'] = df['price_used'] / (df['mileage_km'] + 1)
best_value_cars = df.sort_values(by='value_ratio').head(10)

print("\nCars Offering the Best Resale Value (Price-to-Mileage Ratio):")
print(best_value_cars[['brand', 'model', 'year', 'price_used', 'mileage_km', 'value_ratio']].head(10))

# 4. Market trends based on mileage and year
# Price trends based on mileage
price_mileage_trend = df.groupby('mileage_km')['price_used'].mean().sort_index()

print("\nPrice Trends Based on Mileage:")
print(price_mileage_trend)

# Price trends based on year
price_year_trend = df.groupby('year')['price_used'].mean().sort_index()

print("\nPrice Trends Based on Year:")
print(price_year_trend)