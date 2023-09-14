'''
Here we will learn Builtin functions:
print()
len()
input()
type()
str()
int()
float()
round()
min()
max()
sum()
abs()
range()
list()
zip()

'''

# print
print('it takes unlimited number of argument', True, 100, 3.14, 1 + 2j, sep = ', ')

# len: give the number of items or character in a string, list, set, dictionary, tuple
print('The length of word cat is: ', len('cat'))

print('The number of items in the list:', len([1, 2, 3]))

# input: it takes user input

# print(input('What is your name? '))

""" year_born = input('When were you born? ')

print(year_born, type(year_born), type(int(year_born)))

age = 2023 - int(year_born)

print('You were born in ' + year_born + '.' + 'Then you are ' + str(age) + ' years old.')
 """

print('Hello' + ' ' + 'World!' + " .The year is " + str(2023) )

print(int(float('4.52')) - 4)

print(int(9.82))

print(round(9.82))
print(round(3.14))
print(round(37.898569, 1))
print(min(10, 5, -2, 20, 4))
print(max(10, 5, -2, 20, 4))
print(sum([10, 5, -2, 20, 4]))
print(abs(-5))

# it takes three parameters:start, stop, step
# 0     10  20  30 40 ---           100

print(list(range(-100, 101, 2)))
print(list(range(1, 101, 2)))

# 5, 4, 3, 2,1
print(list(range(5, 0, -1)))

print([1, 2,3,4], ['a','b','c'])
print()

countries = ['Finland','Sweden','Norway']
cities = ['Helsinki', 'Stockholm','Oslo']
print(list(zip(countries, cities)))