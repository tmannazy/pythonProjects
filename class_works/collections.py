import collections

c = collections.Counter("hello")
print(c)

print(c.most_common())
print(c.most_common(1))
print(c.most_common(2))

d = collections.Counter("hello world!")
print(d.subtract(d))