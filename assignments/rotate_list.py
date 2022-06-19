def rotate_list(lst, rotation_num):
    new_lst = []
    for x in range(rotation_num):
        if len(new_lst) == 0:
            if type(lst[0]) is not list:
                el = [lst[0]]
                new_lst = lst[1:] + el
        else:
            if type(new_lst[0]) is not list:
                new_el = [new_lst[0]]
                new_lst = new_lst[1:] + new_el

    return new_lst


print(rotate_list([1, 2, 3, 4, 5], 3))
