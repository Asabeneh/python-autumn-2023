""" import custom_modules

print(dir(custom_modules))
print(custom_modules.name_of_func())
print(custom_modules.add_two_nums(100, 900))
print(custom_modules.make_square(10))
print(custom_modules.sum_all_nums(50)) """



from customs.custom_modules import name_of_func, add_two_nums, make_square, sum_all_nums

print(name_of_func())
print(add_two_nums(100, 900))
print(make_square(10))
print(sum_all_nums(50))


import os