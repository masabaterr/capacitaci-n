from fredapi import Fred

fred = Fred(api_key='TU_CLAVE_API')
gdp_growth = fred.get_series('GDP', transformation='pct_change')
print(gdp_growth)







