# Higher order function
# a function that takes another function as a parameter or return another function

""" def callback():
    return 'you will be called latar'
    

def do_something(fn):
    value = fn()
    return value

print(do_something(callback)) """


def area(l, w):
    return l * w

print(area(4, 5))

def volume(fn, w, l, h):
    return fn(w, l) * h

print(volume(area, 4, 5, 10))


def do_math(a, b):
    def add_nums():
        return a  + b
    def multiply():
        return a  * b
    return {
        'add_nums':add_nums,
        'multiply':multiply
    }

print(do_math(1, 9)['add_nums']())
print(do_math(9, 9)['multiply']())


    
    