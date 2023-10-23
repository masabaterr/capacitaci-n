from fredapi import Fred
import pandas as pd

# Inicializa el objeto Fred con tu clave API
fred = Fred(api_key='TU_CLAVE_API')

# Ahora puedes usar el objeto fred para buscar series
gdp_data = fred.search('GDP')

# Convertir los datos obtenidos en un DataFrame de pandas y mostrar las primeras 5 filas con el metodo head.()
gdp_df = pd.DataFrame(gdp_data, columns=['GDP'])
print(gdp_df.head())

# Guardar el DataFrame en un archivo CSV
gdp_df.to_csv('gdp_data.csv', index=False)
