# print([i for i in range(1, 11) if i % 2 == 0])  # print all numbers
import math


# print([i ** 2 if i % 2 == 0 else i for i in range(1, 11)])  # print all odd numbers and print even numbers to square


# x = 'even' if 4 % 2 == 0 else "odd"

# new_lst = [int(input(f"Enter number {i}'s score: ")) for i in range(0, 5)]
# print(sum(new_lst))


# def is_prime(num: int) -> bool:
#     max_divisor = (num // 2) + 1
#     for x in range(2, max_divisor):
#         if num % x == 0:
#             return False
#     return True
#
def optimised_is_prime(num: int) -> bool:
    if num <= 1:
        return False
    sqrt_cal = math.ceil(math.sqrt(num)) + 1
    for x in range(2, sqrt_cal):
        if num == 2:
            return True
        elif num % x == 0:
            return False
    return True


# print(is_prime(111))
# print(optimised_is_prime(9))

# primes = [i for i in range(1, 101) if optimised_is_prime(i)]
#
# print(primes)
# prime = [i if i > 1  % 2 == 0 else i  for i in range(1, 101)]


def cube(num: int) -> int:
    return num ** 3


# cubes = [cube(i) for i in range(1, 11)]
# print(cubes)

# prime_2 = [i for i in range(1, 10_000_000) if optimised_is_prime(i)] # list comprehension
# prime_2 = sum(i for i in range(1, 10_000) if optimised_is_prime(i) # tuple generator
# prime_2 = {i for i in range(1, 10_000) if optimised_is_prime(i)} # set comprehension
prime_2 = {k: v for k, v in enumerate(range(1, 100)) if optimised_is_prime(v)}
# print(prime_2)
# print(type(prime_2))
print(prime_2)
# print(len(prime_2))
