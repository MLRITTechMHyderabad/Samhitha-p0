import pandas as pd
df = pd.read_csv("uae_used_cars_10k.csv")
df.columns = df.columns.str.strip().str.lower()

avg_price_by_brand = df.groupby('Brand')['price_used'].mean().sort_values(ascending=False)
avg_price_by_model = df.groupby('Model')['price_used'].mean().sort_values(ascending=False)
avg_price_by_year = df.groupby('Year')['price_used'].mean().sort_index()

most_common_makes = df['Brand'].value_counts().head(10)
most_common_models = df['Model'].value_counts().head(10)

price_mileage_trend = df.groupby('mileage_km')['price_used'].mean().sort_index()
price_year_trend = df.groupby('Year')['price_used'].mean().sort_index()


transmission_dist = df['transmission'].value_counts()
fuel_type_dist = df['fuel_type'].value_counts()


df['value_ratio'] = df['price_used'] / (df['mileage_km'] + 1)


best_value_cars = df.sort_values(by='value_ratio').head(10)
print(best_value_cars[['brand', 'model', 'year', 'price_used', 'mileage_km', 'value_ratio']])
