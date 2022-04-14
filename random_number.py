from random import randint


def random_numbers():
    random_number = randint(0, 99)
    return random_number


def random_index(lst):
    random_index_number = randint(0, len(lst) - 1)
    return random_index_number
