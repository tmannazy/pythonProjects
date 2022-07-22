from functools import reduce


def sum_num(a: int, b: int) -> int:
    """
    Adds two parameters a, b and return the solution
    :param a: int
    :param b: int
    :return: int
    """
    return a + b


def subtract(a, b):
    return a - b


# Higher-order function
# A function that either returns, take others in and deals with it
def operate(fn, x, y):
    return fn(x, y)


multiply = lambda x, y: x * y

# Regular function
# print(sum_num(3, 6))
# print(operate(sum_num, 2, 4))
# print(operate(subtract, 5, 2))
# print(multiply(3, 4))
# print(operate(lambda a, b: a // b, 18, 9))
# print(multiply.__name__)

# print(sum_num.__name__)
# print(sum_num.__doc__)
# print(sum_num.__annotations__)

# list_of_string = "I love Chukwuemeka Eden Dove".split()
# list_of_num = ["1", "2", "3"]
# print(max(list_of_string, key=len))
# print(max(list_of_string, key=lambda x: x[-1]))
# print(min(list_of_string, key=lambda x: x[-1]))
# print(max(list_of_num, key=ord(l)))

ages = [{"name": "Adedayo", "age": 6}, {"name": "Titi", "age": 16}]

# print(max(ages, key=lambda x: x['age']))
# print(max(ages, key=lambda x: len(x["name"])))
print(sorted(ages, key=lambda x: x['name'], reverse=True))
# print(help(sorted(ages, key=lambda x: x['age'])))
# set_b = {1, 4, 58, 69, 3}
# print(sorted(list(set_b), reverse=True))
# set_b[0]
# print(sum(set_b))

# Slicing from a string
s = slice(1, 27, 3)
str_ = "I totally don't l*** som..."
print(str_[s])  # or str_[1, 27, 3]

# mapping through a list using map method with lambda and list comp
print(list(map(lambda x: x ** 2, [2, 3, 4, 5])))
print([i ** 2 for i in [2, 3, 4, 5]])

# filtering a list using the filter method with lambda and list comp
print(list(filter(lambda x: x < 2, [2, 3, 4, 5])))
print(list(filter(lambda x: x % 2 == 0, [2, 3, 4, 5])))
print(([i for i in [2, 3, 4, 5] if i % 2 == 0]))

# filtering a list using the reduce method with lambda and list comp
print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 10))
print(sum([1, 2, 3, 4], 10))
print(reduce(lambda a, b: a * b, [2, 3, 4, 5]))
print(reduce(lambda x, y: x, y, [1, 2, 3, 4].append(x), {}))
