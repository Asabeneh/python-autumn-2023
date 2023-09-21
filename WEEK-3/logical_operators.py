# Logical operators
# and, or, but
""" 
Kalle is a Python student. (True)
Sonja is a Python Student. (True)


Kalle and Sonja are Python students. True
Sonja is Python student. True.
Kalle and Sonja are not Python students. False
Kalle or Sonja is not a Python student. False
 """
# and
print('-- logical operator and --')
print(4 > 3 and 1 > 0) # True
print(4 > 3 and -1 > 0) # False
print(2 > 3 and -1 > 0) # False

# or
print('-- logicla operator or----')

print(4 > 3 or 1 > 0) # True
print(4 > 3 or 1 < 0) # True
print( 4 < 3 or 1 < 0) # False


# Negation
print('---- Negation operator ---')
print(True)
print(not True)
print (not not True)

print(not 4 > 3 and not 1 > 0)

print('land' not in 'Finland')

print('on' in 'Dragon' and 'on' in 'Python')