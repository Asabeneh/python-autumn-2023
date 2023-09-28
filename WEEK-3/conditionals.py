# conditionals:
# if else

a = 10
if type(a) == int or type(a) == float:
    if a > 0:
        print(f'{a } is a positive number')
    elif a == 0:
        print(f'{a} is zero')
    else:
        print(f'{a} is a negative number')
else:
    print(f'{a} not a supported value')


# Find today's weather

weather = input('What is the weather today? ').strip().lower()

if weather == 'rainy':
    print("Please take your raincoat")
elif weather == 'sunny':
    print('Go out freely, it is just a shiny day')
elif weather == 'cloudy':
    print('It may rain and it is a good idea to take raincoat')
elif weather == 'foggy':
    print('Be careful when you drive, there might be limited visibility')
else:
    print('No one knows the weather')
