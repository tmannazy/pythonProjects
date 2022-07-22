# import operator
# from functools import reduce
#
# # lst = [1, 2, 3, 4, 5, 8]
# # print(any(True if i >= 7 else False for i in lst))  # all uses generator expression
#
# lst_1 = [1, 2, 3, 4]
# lst_2 = [9, 8, 7, 6]
# # print(list(zip(lst_1, lst_2, lst, strict=True)))
# # print(list(zip(lst_1, lst_2, lst, strict=True)))
# # print(zip(lst_1, lst_2, lst))
#
# students = [
#     {"name": "Abu", "score": [90, 60, 40]},
#     {"name": "Ali", "score": [70, 45, 80]},
#     {"name": "Asake", "score": [99, 78, 88]}
# ]
# # print(list(max(students, key=lambda sum_: sum(sum_['score']))))
# # print(list(max(students, key=lambda sum_: sum(sum_['score']))))
#
# # list_of_dict = [{"name": "Asake", "gender": "F"}, {"name": "Boyo", "gender": "M"}]
# # mapped_list_of_dict = list(map(lambda x: ("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"], list_of_dict))
# # print(mapped_list_of_dict)
# # filter_list_of_dict = list(filter(lambda x: x["gender"] == "M", list_of_dict))
# #
# # print([("Mr. " if x["gender"] == "M" else "Mrs. ") + x["name"] for x in list_of_dict])
# # print([x for x in list_of_dict if x['gender'] == "M"])
# # print(filter_list_of_dict)
# # lst_str = ["life", "is", "not", "balance"]
# sum_reduce = reduce(lambda acc, val: acc + val, lst)
# sum_reduce2 = reduce(operator.sub, lst)
# print(sum_reduce)
# print(sum_reduce2)
#
# fruits = ["pear", "cucumber", "water melon", "banana"]
# print(reduce(lambda x, y: x if len(x) > len(y) else y, fruits))
# print()
#
# """
# LEGB - SCOPING
# L: Local
# E: Enclosing
# G: Global
# B: Builtins
# """
# let = 7
#
#
# def main_one():
#     global let
#     let += 7
#     var = 8
#     print(let)
#
#     def main_two():
#         print(var)
#
#     main_two()
#
#
# print(let)
# main_one()
#
#
# def sub(a, b):
#     return b - a


# print(sub(b=10, a=15))


# def appender(lst=None):
#     if lst is None:
#         lst = []
#     lst.append("You")
#
#
# print(appender())

# def sub(a: int = 0, b: int = 0) -> int:
#     """
#     Calculate the difference between two values
#     """
#     return b - a
#
#
# print(sub.__annotations__['a'])
# print(sub.__annotations__)
# print(sub.__doc__)

# def avg(*numbers):
#     from statistics import mean
# help(mean)
# return sum(numbers) / len(numbers)
# return mean(numbers)
#
# print(avg(1,2,3,4))
# print(avg(1,2,3))
# print(avg(*[1,2,3,4]))

# def add(a=0, b=0, c=0):
#     return a + b + c
#
# d = dict(b=6, c=5, a=7)
# print(d)
# print(add(**d))

# def add(a, *args, b=0, **kwargs):
#     print(a)
#     print(args)
#     print(b)
#     print(kwargs)
#
#
# add(5, 6, 7, 8, b=9, c=0, f=8, y=4)

def add(a, b, /, *, c):
    print(a, b, c)


add(6, 9, c=8)
