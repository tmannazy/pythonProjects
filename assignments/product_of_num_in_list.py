def product_of_list(lst):
    product_total = 1
    for x in lst:
        product_total *= x
    return product_total


print(product_of_list([1, 2, 3, 4]))
