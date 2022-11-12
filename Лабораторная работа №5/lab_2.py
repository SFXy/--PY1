from random import shuffle
def get_unique_list_numbers() -> list[int]:
    list_ = [i for i in range(left_lim, right_lim + 1)]
    shuffle(list_)
    return list_[:list_len]  # TODO написать функцию для получения списка уникальных целых чисел

left_lim = -10
right_lim = 10
list_len = 15
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
