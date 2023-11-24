import requests
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
import json

# get request

response = requests.get(url)
data = response.json()

# function programming, list comphres, regular loop

""" for cat in data:
    print('------')
    print(cat['origin'], cat['name'], cat['life_span']) """
    

ages = []
for cat in data:
    lowest, highest = cat['life_span'].split(' - ')
    average = (int(lowest) + int(highest)) / 2
    ages.append(average)

average_life_span_cats = round(sum(ages) / len(ages), 2)
print(average_life_span_cats)


