# set is a collection of unique items
# no order and cannot be accessed by indexing
# mutable

lst = [1, 2, 2, 3, 4,4, 5]
print('List here: ', lst)
print(len(lst))

s = {1, 2, 2, 3, 4, 4, 5}
print('Set here: ', s)
print(len(s))

empty_set = set(lst) #  {}
print(len(s))

fruits = {'banana', 'orange', 'mango', 'lemon'}
for fruit in fruits:
    print(fruit)
    
print('mango' in fruits)
    
print('avocado' in fruits)
fruits.add('apple')
fruits.add('avocado')
print(fruits)
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

print(fruits)
fruits.remove('apple')
print(fruits)
fruits.clear()
print(fruits)

A = {1, 2, 3, 4, 5}
B = {2, 3, 5, 6, 7}

# A U B = {1, 2, 3, 4,5,6,7}
# A n B = {2, 3, 5}
# A \ B = {1, 4}
# B \ A = {6, 7}
# A delta B = (AUB)\(AnB) = {1, 4, 6, 7}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.isdisjoint(B))
print(A.issubset(B))