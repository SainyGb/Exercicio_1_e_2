from random_number import random_numbers
from lists_generator import lists_generator


def change_random_number(truple_of_2_lists):
    truple_of_2_lists[0][random_numbers()] = 1
    #truple_of_2_lists[1][random_numbers()] = 1

    return truple_of_2_lists
