def get_prime_num(start, end):
    lst_of_prime = []
    for x in range(start, end + 1):
        if x > 1:
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                lst_of_prime.append(x)

    return lst_of_prime


print(get_prime_num(1, 100))


