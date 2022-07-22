# s = {1, 2, 3, 4}
# p = {6, 7, 8, 2, 9}
# o = s | p

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {1, 3}
s4 = {1, 2, 3, 4, 5, 6, 7, 8}
s4.add('d')
s4.add('c')
# s4.discard(0)
# s4.remove(0) # throws error if element not found
# s4.clear()
# print(s4.union(s2)) # print(s4 | s2)
# s1.update(s2)
# s1 |= s2
# print(s1.intersection(s2))
# print(s1 & s2)
# s1.intersection_update(s2)
# s1 &= s2
# print(s1)
# print(s2.difference(s1))
# print(s1.difference(s2))
# print(s2 - s1)
# s2.difference_update(s1)
# s2 -= s2
# print(s2)
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)
# s2.symmetric_difference_update(s1)
# s2 ^= s1
# print(s2)
# print(s3.issubset(s1))
# print(s3 < s1)
# print(s1.issuperset(s3))
# print(s1 > s3)
# print(s1.isdisjoint(s3))

"""
DICTIONARIES
"""
d1 = {'a': 1, 'b': 2, 'c': 4}
# d1.pop('a')
# d1.popitem()
# d1.update({'a': 5, 'b': 8})
# d1 |= {'a': 5, 'b': 8}
# print(d1.items())
# print(list(d1.keys()))
# print(list(d1.values()))
# for key, val in enumerate(d1):
#     print(key)
# for key, val in d1.items():
#     print(val)
#     print(f"{key} -> {val}")

# for key in d1:
#     print(key)

# for k in d1.values():
#     print(k)

# for k in d1.keys():
#     print(k)

# print(r"I \n love\\ \n it \n raw") # printing output RAW

# print(d1.get('g', 7)) # printing something if a key is not in dictionary
# print(d1)
d = dict(a=1, b=2, c=3)
print(d.fromkeys('abcd', 0))
print({}.fromkeys('abcde', list(range(1,8))))
d.setdefault('d', 0)
print(d)
# print(s4)
