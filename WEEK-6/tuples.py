# immutable
empty_tp = tuple() # ()
empty_tp_2 = ()
print(empty_tp)
print(type(()))

item = (1, )
print(type(item))
print(len(item))

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[0])
print(fruits[-1])
for fruit in fruits:
    print(fruit)
    
print('orange' in fruits)
print(fruits[1:])

print(list(fruits))
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

tp = (1, 2, 2, 2, 3, 4)
print(tp.count(2))
print('mongoose'.count('o'))