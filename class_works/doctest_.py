import doctest


# def two_sum(lst_of_num, target):
# lst_ = []
# a = 0
# for x in lst_of_num:
#     a = x
#     if a + x == target:
#         lst_.append(a)
# a = list(zip(lst_of_num, lst_of_num[1:]))
# b = [i for i in a if sum(i) == target]
# print(b)

# return lst_

# for i in range(len(lst_of_num) - 1):
#     for j in range(i + 1, len(lst_of_num)):
#         res = lst_of_num[i] + lst_of_num[j]
#         if res == target:
#             return [i, j]


# lst = [3, 1, 5, -8]
# print(lst, 6)
# twoSum(lst, 6)
# print(twoSum(lst, 6))


# def two_two_sum(lst_of_num: list, target: int) -> list or int:
#     map_ = {}
#     for i in range(len(lst_of_num)):
#         complement = target - lst_of_num[i]
#         if complement in map_:
#             return [map_[complement], i]
#         else:
#             map_[lst_of_num[i]] = i
#     return -1
#
#
# print(two_two_sum(lst, 40))


def add(a, b):
    """
    :param a:
    :param b:
    :return:
    >>> add(3, 5)
    8
    >>> add(3, "Hi")
    Traceback (most recent call lost):
        ...
    TypeError: unsupported
    """
    return a + b


if __name__ == '__main__':
    doctest.testmod()
