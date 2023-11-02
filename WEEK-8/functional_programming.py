# map, filter, reduce
# ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland'] => ['FIN', 'SWE', 'NOR','DEN','ICE'] => [7, 6, 6, 7]

""" countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
country_codes = []
for country in countries:
    code = country.upper()[:3]
    country_codes.append(code)
    
print(country_codes) """
    
""" countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
def fn(country):
    code = country.upper()[:3]
    return code
country_codes = map(fn, countries)
print(list(country_codes)) """
from countries import countries
from countries_data import data
from pprint import pprint
nordics = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
def get_countries_code (data):
    country_codes = map(lambda country: [country, country.upper()[:3]], data)
    return list(country_codes)


nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

squared_numbers = map(lambda x : x ** 2, nums)
print(list(squared_numbers))
print(get_countries_code(nordics))
print(get_countries_code(countries))

populations = list(map(lambda country: country['population'], data))
world_population = sum(populations)
print(world_population)
print('The world population is {:,}'.format(world_population))

# filter and reduce
# pprint(data)

countries_with_land = list(filter(lambda country: 'land' in country, countries))
print(countries_with_land)

countries_with_low_population =  list(filter(lambda country:country['population'] < 1000, data))
pprint(countries_with_low_population)

pprint(list(map(lambda c: [c['name'], c['population']], countries_with_low_population)))

# reduce => 
from functools import reduce
nums = [1, 2, 3, 4]

""" total = 0 
for num in nums:
     total = total + num
print(total) """

total = reduce(lambda acc, cur : acc + cur, nums)
print(total)

world_population = reduce(lambda acc, cur: acc + cur['population'], data, 0)
print(world_population)

sorted_countries = sorted(data, key=lambda c:c['population'], reverse=True)
ten_most_populated_countries = sorted_countries[:10]
pprint(sorted_countries[:10])
print(len(sorted_countries[:10]))






