import math 
import random  

print(math.sqrt(2))
print(math.pi)
print(math.pow(2, 10)) # 2 ** 10
print(math.floor(3.14))
print(math.ceil(9.81))
print(math.ceil(3.14))
print(math.floor(9.81))

print(dir(random))
print(random.randint(0, 100))
print()
nums = [1, 2,3,4]
random.shuffle(nums)
print(nums)
print(random.choice('aeiou'))

letters = 'abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'

users_id = []
for n in range(11):
    user_id = ''
    for i in range(8):
        letter = random.choice(letters)
        user_id += letter
    users_id.append(user_id)
    
    
print(users_id)
