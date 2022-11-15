from random import sample
def get_unique_list_numbers(start = -10, stop = 10, size = 15) -> list[int]:
    return sample([i for i in range(start, stop, 1)], size)
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
