import pandas as pd

def clean_rating_column(df, column_name='rating', strategy='median'):
    try:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        
        if strategy == 'median':
            # Use explicit assignment to avoid chained assignment warning
            median_value = df[column_name].median()
            df[column_name] = df[column_name].fillna(median_value)
        
        df = df[(df[column_name] >= 1) & (df[column_name] <= 5)]
        return df
    except Exception as e:
        print("Error occurred during data cleaning:", e)
        return None

data = {
    'customer_id': [11, 12, 13, 14, 15],
    'product_id': [100, 101, 102, 103, 104],
    'rating': [4, 5, 2, 'na', 3], 
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()

cleaned_df = clean_rating_column(df, column_name='rating', strategy='median')
print("Cleaned DataFrame:")
print(cleaned_df)
