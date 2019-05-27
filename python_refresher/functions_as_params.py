def methodception(another):
    return another()


def add_two():
    return 1 + 1


x = methodception(add_two)
print(x)  # 2

y = methodception(lambda: 1 + 1)
print(y)  # 2

##

my_list = [1, 2, 3, 4, 5, 6]
# How to extract only evens?
# 1
new_list = [item for item in my_list if item % 2 == 0]
print(new_list)

# 2. filter built-in function + lambda
new_list = list(filter(lambda item: item % 2 == 0, my_list))
print(new_list)

# 3. filter + regular foo
def is_even(num):
    return num % 2 == 0

new_list = list(filter(is_even, new_list))
print(new_list)
##

(lambda x: x * 3)(5)

# this is equals to:

def foo(x):
    return x * 3

foo(5)