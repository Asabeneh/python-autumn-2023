# 

""" try:
    print(10/0)
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
except NameError:
    print('Name error') """
    
    
try:
    print(100 + 10)
except Exception as e:
    print("The error is ", e)
else:
    print('this will be printed out if the try block works')
finally:
    print('I will be executed not matter what')


