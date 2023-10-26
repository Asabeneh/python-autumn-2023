def name_of_func ():
    print('I am a function')
      
name_of_func()

def add_two_nums(a, b):
    return a + b


print(add_two_nums(1, 9))
print(add_two_nums(99, 1))
print(add_two_nums(-10, 20))

def make_square(n):
    return n ** 2


def sum_all_nums(n):
    lst = list(range(n + 1))
    return sum(lst)

print(sum_all_nums(100))
    