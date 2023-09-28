# While: 

count = 0
while count < 6: 
    print(count) # 5
    count  = count + 1 # 
    
print(count)

    
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(countries[0])
print(countries[1])
print(countries[4])
print(countries[-1])



i = 0 # initialization

while i < len(countries):
    print(i, countries[i])
    i +=  1



last_index = len(countries) - 1

while last_index >= 0:
    print(countries[last_index])
    last_index -= 1


# Quiz: Number guessing game
# CONGRATULATIONS!!!
# my_number user_number
# checking the my number and the user number
# if my number is equl with user name print the winor with congratula
# if not compare his number and user number and give him a hint



""" counter = 0
while True:
    my_number = 37
    your_number = int(input('What is the number in my mind? '))
    counter += 1
    print(counter)
    if my_number == your_number:
        print(f'=== CONGRATULATIONS!!! ===\n you won the game in {counter} rounds')
        break
    else:
        if your_number > my_number:
            print('The number is less the given number')
        else:
            print('The number is greater than given number') """

            
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

