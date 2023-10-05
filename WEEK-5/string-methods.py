# String Methods
# String methods allow us to work on string

word = 'Love'
print(word.lower())
print(word.upper())
print(word.swapcase())
print(word.startswith('L'))
print(word.startswith('l'))
print('Finland'.endswith('land'))
print('land' in 'Finland')
print('an' in 'Finland')
print(word.replace('L', 'i'))
print('Finland'.replace('Fin', 'Po'))

sentence = 'I love people, people are awesome that why I LOVE them.'.lower()
sentence = sentence.replace(',', '')
sentence = sentence.replace('.', '')
# cleaning the data
words = sentence.split()
unique_words = set(words)
number_total_words = len(words)
number_unique_words = len(unique_words)


print('Number of words:', len(words))
print('Number of unique words:', len(unique_words))
lexical_variety =  number_unique_words / number_total_words * 100
print(round(lexical_variety, 2))
# Lexical varaity

first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name  + ' ' +  last_name
country = 'Finland'
age = 250
print(f'I am {full_name}.\nI am {age} years old.\nI live in {country}.\nHere are my skills:\n\tHTML\n\tCSS\n\tJavaScript')

print('I don\'t like taking attend')
print('People say, "An apple a day keep the doctor away"')
print('People say, \'An apple a day keep the doctor away\'')

radius = 10
pi = 3.14
area = pi * radius ** 2
print('The radius is %d. The value of pi is %.2f. The area is %.2f '%(radius, pi, area))



first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {0} {1}. I teach {2}. {2} is the most beautiful language and of course it is taught by {0}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3
print('{0} + {1} = {1} + {0} = {2}'.format(a, b, a + b))
print('{0} x {1} = {1} x {0} = {2}'.format(a, b, a * b))
print(f'{a} + {b} = {b} + {a} = {a + b}')
print(f'{a} x {b} = {b} x {a} = {a * b}')

word = 'Python'
print(word[0])
print(word[0:2])
print(word)
print(word[::-1])
print([2, 3,1,4][::-1])

challenge = 'thirty days of python'
print(challenge.lower())
print(challenge.upper())
print(challenge.split())
print(challenge.title())
print(challenge.capitalize())
print(challenge.count('t'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(12)) # 'thirty    days      of        python'

challenge = 'thirtydaysofpython'
print(challenge.find('t'))
print(challenge.rfind('t'))
print(challenge.find('z'))

print(challenge.index('t'))
print(challenge.rindex('t'))

if 'z' in challenge:
    print(challenge.index('z'))
print(challenge.islower())
print(challenge.isupper())
print(challenge.isalnum())
print(challenge.isdigit())
print('123'.isdigit())
print('123'.isnumeric())
num = '10.5'
print(num.isdecimal()) # False

print('xy10'.isidentifier())

skills = ['HTML', 'CSS', 'JavaScript', 'React']
print('-'.join(skills).lower())
print('      I love people')
print('      I love people'.strip())
print('      I love people'.strip('people'))
print('test')
print(' love      I love people'.strip(' love'))


