
def make_square(n):
    return n ** 2


fn = lambda n: n ** 2

print(fn(2))
print(fn(10))

# x^2 + 2x + y
# 2, 3 => 4 + 4 + 3 => 11

fn = lambda x, y: x ** 2 + 2 * x + y
print(fn(2, 3))

