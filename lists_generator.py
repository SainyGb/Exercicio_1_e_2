def lists_generator():
    lst_1 = [value*0 for value in range(100)]
    lst_2 = lst_1[:]

    return lst_1, lst_2


def list_zero_to_hundred():
    lst = [value for value in range(100)]
    return lst
