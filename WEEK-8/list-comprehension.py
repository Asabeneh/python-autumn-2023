# list comprehension is memory efficent, performant

from countries import countries
from countries_data import data
nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

""" new_nums = []
for n in nums:
    new_nums.append(n ** 2)
    
print(new_nums) """

""" new_nums = list(map(lambda n : n ** 2, nums))
print(new_nums) """

new_nums = [ n * 2  for n in nums]
print(new_nums)
countries_code = [c.upper()[:3] for c in countries]
print(countries_code)
populations = [c['population'] for c in data]
print(populations)

""" list_lst = [[1, 2,3],[4,5,6],[7, 8,9]]
new_lst = []
for item in list_lst:
    new_lst.extend(item)
    
print(new_lst) """


list_lst = [[1, 2,3],[4,5,6],[7, 8,9]]
flattened_lst = [i for item in list_lst for i in item]
print(flattened_lst)


