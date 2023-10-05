# function:is a block of code that does a certain task
# It would be great if a function solve only one problem
# functin may or may not take a parameter
# a function may or may not return a value
# how do we create a function

def do_something ():
    print('I am actually doing something. I am proud function')
    
do_something()

def print_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name
    
print(print_full_name('Asab','Yeta'))
print(print_full_name('Donlad','Trump'))
print(print_full_name('John','Doe'))

def add_two_nums(a, b):
    return a + b

print(add_two_nums(1, 9))
print(add_two_nums(91, 9))


def make_square(n):
    return n ** 2

print(make_square(2))

def generate_list(start, end, step):
    return list(range(start, end + 1, step))


print(generate_list(50, 100, 5))
print(generate_list(25, 75, 3))
print(generate_list(0, 100, 1))

# 100
""" def sum_all_nums(n):
    total = 0
    for i in  range(n+1):
       total = total + i
    return total
print(sum_all_nums(10)) """

def sum_all_nums(n):
    return sum(range(n + 1))

print(sum_all_nums(10))
       