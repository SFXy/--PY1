def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower().split()
    str_ = "".join(str_)

    for let_ in str_:
         if let_ in dict_ and let_.isalpha():
             dict_[let_] += 1
         elif let_.isalpha():
            dict_[let_] = 1

    return dict_

def get_count_char1(dict_):
    total_sum = sum(dict_.values())
    for let_, num_ in dict_.items():
        dict_[let_] = round((num_ / total_sum) * 100, 3)

    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_count_char1(get_count_char(main_str)))