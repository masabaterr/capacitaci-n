from fredapi import Fred

fred = Fred(api_key='04008132ab90f5b3d89035751921cadd')
gdp_growth = fred.get_series('GDP', transformation='pct_change')
print(gdp_growth)







