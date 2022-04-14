from switch_random_number import change_random_number
from lists_generator import lists_generator, list_zero_to_hundred


def equal_sequences():
    lsts_of_changed_numbers = change_random_number(lists_generator())

    if len(lsts_of_changed_numbers[0]) == len(lsts_of_changed_numbers[1]):
        counter = 0

        for i in range(len(lsts_of_changed_numbers[0])):
            counter += 1
            if lsts_of_changed_numbers[0][i] != lsts_of_changed_numbers[1][i]:
                return counter
        else:
            return counter

    else:
        return counter
