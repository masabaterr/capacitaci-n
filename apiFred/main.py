from fredapi import Fred
import pandas as pd

# Replace with your own API key from FRED
api_key = '04008132ab90f5b3d89035751921cadd'

# Initialize the Fred object with your API key
fred = Fred(api_key=api_key)

# Fetch the GDP data
gdp_series_id = 'PAYEMS'  # This is the series ID for GDP
gdp_data = fred.get_series(gdp_series_id)

# Convert the data into a pandas DataFrame
gdp_df = pd.DataFrame(gdp_data, columns=['PAYEMS'])

# Filter the DataFrame for the year 2023
gdp_2023_df = gdp_df[gdp_df.index.year == 2023]

# Display the DataFrame
print(gdp_2023_df)

# Save the DataFrame to a CSV file
gdp_2023_df.to_csv('gdp_2023_data.csv', index=True)




