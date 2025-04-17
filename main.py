import pandas as pd

try:
    df = pd.read_csv("uae_used_cars_10k.csv")
    print(" File loaded successfully.")
except FileNotFoundError:
    print(" Error: File not found.")
    df = None  
except pd.errors.ParserError:
    print(" Error: Could not parse the file.")
    df = None 


if df is not None:

    print("Columns in the dataset:")
    print(df.columns)  

   
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    print("\nNormalized column names:")
    print(df.columns)  

    
    if 'year' in df.columns:  
        df.drop_duplicates(inplace=True)
        df.dropna(subset=['make', 'model', 'year', 'price', 'mileage'], inplace=True)
      
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

     
        df = df[(df['year'] <= 2025) & (df['year'] >= 1980)]
        df = df[(df['mileage'] > 0) & (df['price'] > 0)]

        
        df.rename(columns={
            'make': 'brand',
            'price': 'price_used',
            'mileage': 'mileage_km'
        }, inplace=True)

        print("Cleaned dataset preview:")
        print(df.head())
    else:
        print(" Error: 'year' column not found.")
else:
    print(" No data to clean, as file loading failed.")
