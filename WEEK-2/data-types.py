'''
Data types:

Numbers(int, float, complex)
String- anything under single, double or triple quote
Booleans: True or False
List: store list of items, they are ordered sequence
Set: does not allow duplicate itmes, no word
Tuple: not mutable, ordered
Dictionary: key value items

'''
# Numbers in Python (int, float, complex)
print(100, type(100))
print(9.81, type(9.81))
print(1 + 4j, type(1 + 4j))

# Strings in Python are created using single, double, triple quote
# it could be a single character of many pages length

print('P')
print('Python')
print('I love Python. There is nothing like such a great programming languages')
print('''It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).''')

# Booleans: True or False
print(True)
print(False)
print('This should be true', 1 > 0)
print('This is false', 0 == 1)
print('python'.upper().isupper())
print('Finalnd'.startswith('F'))

# List: allows us to store different data types
print([1, 2, 3, 4])
print(['Asab', 250,  'Finland', True, 1.72])

print(len(['Asab', 250,  'Finland', True, 1.72]))
print({'Mary','Kalle','Mary','Sonja','Devraj', 'Mary'})

words = 'I love teaching. I love Python. I love people'.split()
print(len(words))
print(len(set(words)))

total_words = len(words)
unique_words = len(set(words))
lexical_variety = unique_words/total_words
print(lexical_variety)

print(set(words))


# Tuple are not modifiable
print(('Asabeneh','Yetayeh', 250, True))

# Dictionary

fin_en_dict = {
    'talo':'house',
    'kirja':'book',
    'tuoli':'chair',
    'auto':'car',
}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
    'is_married':True,
    'height':1.72,
    'weight':73.5,
    'skills':['HTML','CSS','JS','Python'],
    'address':{
        'city':'Espoo',
        'zipcode':'02770',
        'street_name':'Space street'
    }
}
print(fin_en_dict)
print(person)