countries = input().split(', ')
capitals = input().split(', ')

countries_capitals_dict = {country: capital for (country, capital) in zip(countries, capitals)}

for country, capital in countries_capitals_dict.items():
    print(f'{country} -> {capital}')
