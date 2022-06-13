if __name__ == '__main__':
    letters = 'hello world'
    # for a_letter in letters:
    #     print(a_letter)

    # for num in range(4, 15, 2):
    #     print(num)

    # for num in range(10, 0, -1):
    #     print(num)

    # for num in range(1, 101):
    #     if num % 3 == 0 and num % 5 == 0:
    #         print("FIZZBUZZ")
    #     elif num % 3 == 0:
    #         print("FIZZ")
    #     elif num % 5 == 0:
    #         print("BUZZ")
    #     else:
    #         print(num)

# for num in range(1, 101):
#     if num % 15 == 0:
#         print("FIZZBUZZ")
#     elif num % 3 == 0:
#         print("FIZZ")
#     elif num % 5 == 0:
#         print("BUZZ")
#     else:
#         print(num)

# for num in range(1, 101):
#     if not num % 15:
#         print("FIZZBUZZ")
#     elif not num % 3:
#         print("FIZZ")
#     elif not num % 5:
#         print("BUZZ")
#     else:
#         print(num)
#
# print("A is: ", ord("A"))
# print("65 is: ", chr(65))

# we = "Hello"
# [start: end: step]
# [start: finish: count_by]
# print(we[0: 3: -1])
# print(we[:-1:2])

# for i in range(11, 1, -1):
#     print("*" * i)

# for i in range(1, 11, -1):
#     print(f'{"*" * i:11}')

# for i in range(1, 11, 2):
#     print(f'{"*" * i:>11}', end="")
#     print(f'{"*" * i:0}')
# print('{:>10s} is {:<10d} years old.'.format("Bill", 25))

# for x in "python":
#     print(x.upper(), end="")
#
# list_of_numbers = [2, 5, 6, 7, 9]
#
# num = 0
# for item in list_of_numbers:
#     num = num + item
# print(num)


# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if 1900 <= year <= 10 ** 5:
#         if not year % 4 and not year % 400 or year % 100:
#             leap = True
#
#     return leap


# word = "Hello"
#     for index, element in enumerate(letters):
#         print(index, element)

print(f"{45:0>10d}")
print(f"{45:0<10d}")
print(f"{'hey':=^10s}")
print(f"{12:0=+10d}")



