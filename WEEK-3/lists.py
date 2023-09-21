# Lists are order sequence of items
# creating a list [] or list()

empty_lst = []

print(empty_lst)
numbers = [10, 20, 30, 40]
print(len(numbers))
length = len(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])

last_index = len(numbers) - 1
print(last_index)
print(numbers[last_index])
print(numbers[-1])
print(numbers[-2])
print(numbers[:])
print(numbers[0:])
print(numbers[1:3])
print(numbers[-3:-1])

print(-2 in numbers)
print(20 in numbers)
print(numbers.count(10))
numbers[0] = 1
numbers[1] = 2
print(numbers)
numbers.append(50)
numbers.extend([60, 70, 80, 90])
print(numbers)

shopping_cart = ['Meat', 'Yoghurt', 'Coffee', 'Sugar','Honey','Tea']
print(shopping_cart[0])
print(shopping_cart[-1])
print([1, 2, 3] + [4, 5, 6, 7])
shopping_cart[0] = 'Milk'
print(shopping_cart)
# shopping_cart.pop(3)
print(shopping_cart[2:4])
# del shopping_cart[2:4]
# shopping_cart.remove('Honey')
print(shopping_cart)
shopping_cart.insert(2, 'Cheese')
print(shopping_cart)

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
b, o, m, *others = fruits 
print(b,o, m, others)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, _, *others, es = countries
print(others)

nums = [1, 2, 3]

nums2 = nums.copy()

nums2.append(20)

print(nums2)

print(nums)


fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']


operation = input('sort by: ')
if operation == 'asc':
    fruits_copy = fruits.copy()
    fruits_copy.sort()
    print(fruits_copy)
elif operation == 'desc':
    fruits_copy = fruits.copy()
    fruits_copy.sort(reverse=True)
    print(fruits_copy)