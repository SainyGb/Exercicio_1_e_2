from switch_random_number import change_random_number
from lists_generator import lists_generator, list_zero_to_hundred
from random_number import random_index


def check_equal_lists_random():
    lsts_of_changed_numbers = change_random_number(lists_generator())
    lsts_of_index = list_zero_to_hundred()
    count = 0

    while lsts_of_index:
        random_idx = lsts_of_index.pop(random_index(lsts_of_index))
        count += 1
        # print(lsts_of_index.pop(random_index(lsts_of_index)))
        if lsts_of_changed_numbers[0][random_idx] != lsts_of_changed_numbers[1][random_idx]:
            # print("They're not equal")
            # print(f"count: {count}")
            return count

    else:
        # print('--------------------------------------THEY ARE EQUAL--------------------------------------')
        # print(count)
        return count
