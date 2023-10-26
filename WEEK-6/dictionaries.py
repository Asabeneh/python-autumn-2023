from pprint import pprint

dct = dict() # {}
print(dct)
print(len(dct))

person = {
    'first_name':'Asabeneh',
     'last_name':'Yetayeh',
     'is_married':True,
     'age':250,
     'skills': ['JS','Python','Node'],
     'country':'Finland'
}

print(person['first_name'])
print(person.get('country'))

if 'country' in person:
    print(person['country'])
    
if 'nationality' in person:
    print(person['nationality'])
else:
    person['nationality'] = 'Ethiopian'
    
    
print(person)
print(person['skills'])
person['skills'].append('ML')

print(person)
person['age'] = 40
print(person)

person.pop('age')
person.pop('nationality')
print(person)


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }


keys = person.keys()
print(list(keys))

values = person.values()
print(list(values))

print(person.items())

items = person.items()

for item in items:
    # key, value = item
    print(item[0], item[1])



# create create_frequency_table(), it takes a text
# return a frequency table in a descending order

txt= 'and the love and the love and love and love and the he love you and they love you too he is in love with you and he love you'

def word_count(txt, n = None):
    unique_words = ['and', 'the', 'love', 'you', 'he', 'they', 'too', 'is', 'with', 'in']
    dct = {}
    for word in unique_words:
        count = txt.count(word)
        dct[word] = count
    items = dct.items()
    sorted_items = sorted(items, key = lambda x : x[1], reverse=True)
    if n != None:
        return sorted_items[:n]
    else:
        return sorted_items
    # for item in sorted_items[:3]:
    #     print(f'The word {item[0]} appears {item[1]} in the shakespears book')



pprint(word_count(txt, 7))

