import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("uae_used_cars_10k.csv")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# 1. Average price by brand, model, and year
avg_price_by_brand = df.groupby('Brand')['price_used'].mean().sort_values(ascending=False)
avg_price_by_model = df.groupby('Model')['price_used'].mean().sort_values(ascending=False)
avg_price_by_year = df.groupby('Year')['price_used'].mean().sort_index()

# 2. Most common car makes and models
most_common_makes = df['Brand'].value_counts().head(10)
most_common_models = df['Model'].value_counts().head(10)

# 3. Price trends based on mileage and year
price_mileage_trend = df.groupby('mileage_km')['price_used'].mean().sort_index()
price_year_trend = df.groupby('Year')['price_used'].mean().sort_index()

# 4. Distribution of transmission and fuel type
transmission_dist = df['transmission'].value_counts()
fuel_type_dist = df['fuel_type'].value_counts()

# 5. Best value cars based on price-to-mileage ratio
df['value_ratio'] = df['price_used'] / (df['mileage_km'] + 1)

# Display the best value cars
best_value_cars = df.sort_values(by='value_ratio').head(10)
print(best_value_cars[['brand', 'model', 'year', 'price_used', 'mileage_km', 'value_ratio']])