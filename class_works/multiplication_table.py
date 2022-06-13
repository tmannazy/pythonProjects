import itertools

for num in range(1, 13):
    for inner_num in range(1, 13):
        print('{:4d} * {:>4d}   =   {:>2d}'.format(num, inner_num, num * inner_num))
    print()

# for i, j in itertools.product(range(1, 13), range(1, 13)):
#     print('{:<4d} * {:>4d} {:^} {:>4d}'.format(i, j, "=", i * j))
#     if j == 12:
#         print()

# for i, j in itertools.product(range(1, 13), range(1, 13)):
#     print('{:<0} * {:>1} {:^2} {:>3}'.format(i, j, "=", i * j))
#     if j == 12:
#         print()

for i, j in itertools.product(range(1, 13), range(1, 13)):
    print(f"{i} {'*':>4} {j:>4} {'=':>3} {i * j:>4}", end="\t")
    if j == 12:
        print(end="\t")
