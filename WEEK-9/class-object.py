# class

'''
from datetime import datetime
    now = datetime.now().strftime("%d %b %Y %H:%M")
    print('this is a dog class')

'''

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def say_woof(self):
        return 'Woof Woof'
        
dog1 = Dog('Puppy', 10, 'Beagle')
print(dog1.name)
print(dog1.age)
print(dog1.breed)
print(dog1.say_woof())

dog2 = Dog('Luna', 14, 'Poodle')
print(dog2.name)
print(dog2.age)
print(dog2.breed)
print(dog2.say_woof())

# let us make a class of a person

class Person:
    def __init__(self, first_name, last_name, age, gender,country, city):
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 
        self.country = country
        self.gender = gender
        self.city = city
    def get_fullname(self):
        return self.first_name + ' ' + self.last_name
    
    def give_pronoun(self):
        pronoun = 'He' if self.gender == 'Male' else 'She'
        return pronoun
    
    def get_person_info(self):
        full_name = self.get_fullname()
        pronoun = self.give_pronoun()
        return f'{pronoun} is {full_name}. {pronoun} is from {self.country}. {pronoun} is {self.age} years old. '
        
p1 = Person('Asab','Yeta', 40, 'Finland', 'Male', 'Espoo')
print(p1.first_name)
print(p1.last_name)
print(p1.get_fullname())


p2 = Person('Donald J.','Trump', 80, 'Male', 'USA','New York')
print(p2.first_name)
print(p2.last_name)
print(p2.get_fullname())
print(p2.age)
print(p2.get_person_info())


p3 = Person('Sana','Mari', 37, 'Finland','Helsinki', 'Female')
print(p3.first_name)
print(p3.last_name)
print(p3.get_fullname())
print(p3.age)
print(p3.get_person_info())

class Student(Person):
    def __init__(self, first_name, last_name, age, gender,country, city, title):
        self.title = title
        super().__init__(first_name, last_name, age, gender, country, city)
        self.skills = []
        self.scores = 0
    def get_person_info(self):
        pronoun = self.give_pronoun()
        print(pronoun)
        return super().get_person_info() + f'{pronoun} is a {self.title}'
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skills (self):
        formatted_skills = ', '.join(self.skills)
        return f'{self.get_fullname()} knows {formatted_skills}.'
    def add_score(self, score):
        self.scores += score
    
    
s1 = Student('John','Doe', 21, 'Male', 'Sweden', 'Stockholm', 'Programmer.')

print(s1.get_person_info())

s1.add_skill('Python')
s1.add_skill('Machine Learning')
s1.add_skill('SQL')

print(s1.get_skills())
s2 = Student('Zarin','Shaikh', 24, 'Female', 'Finland', 'Helsinki','Data Analyst')
print(s2.scores)
s2.add_score(5)
s2.add_score(5)
s2.add_score(5)
print(s2.scores)