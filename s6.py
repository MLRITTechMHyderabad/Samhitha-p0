import pandas as pd

df = pd.read_csv("uae_used_cars_10k.csv" )

df.columns = df.columns.str.strip().str.lower()

print("Summary Statistics:\n")
print(df.describe(include='all'))

most_common_models = df['model'].value_counts().head(10)
print("\nTop 10 Most Listed Car Models:")
print(most_common_models)

df['value_ratio'] = df['price_used'] / (df['mileage_km'] + 1)
best_value_cars = df.sort_values(by='value_ratio').head(10)

print("\nCars Offering the Best Resale Value (Price-to-Mileage Ratio):")
print(best_value_cars[['brand', 'model', 'year', 'price_used', 'mileage_km', 'value_ratio']].head(10))

price_mileage_trend = df.groupby('mileage_km')['price_used'].mean().sort_index()

print("\nPrice Trends Based on Mileage:")
print(price_mileage_trend)

price_year_trend = df.groupby('year')['price_used'].mean().sort_index()

print("\nPrice Trends Based on Year:")
print(price_year_trend)
