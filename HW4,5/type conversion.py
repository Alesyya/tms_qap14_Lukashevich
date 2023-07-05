#  1
def string_to_array(str_1, srt_2):
    """ # 1 переводит строку в массив"""
    print(list(str_1.split(maxsplit=1)))
    print(list(srt_2.split(maxsplit=6)))
    return str_1, srt_2


string_to_array('Robin Singh', 'I love arrays they are my favorite')


#  2
def transformation(list_1, city, country, a):
    """ #2 Функция transformation принимает четыре аргумента: list_1, city, country и a.
     Функция выводит отформатированную строку с помощью функции print и возвращает переменную name"""
    name = ' '.join(map(str, list_1))  # преобразование списка в строку
    print(a.format(name=name, city=city, country=country))
    return name


transformation(['Ivan', 'Ivanou'], 'Minsk', 'Belarus', 'Привет, {name}! Добро пожаловать в {city} {country}')


#  3
def func(list_2):
    """ #3 Внутри функции происходит преобразование списка list_2 в строку с помощью метода join,
    Затем функция возвращает полученную строку"""
    a = ' '.join(list_2)
    return a


print(func(["I", "love", "arrays", "they", "are", "my", "favorite"]))


#  4
def change_list(list_3):
    """ #4 возвращает список в котором 10 элементов, на 3-ей позиции новое значение,
удален элемент из списка под индексом 6"""
    list_3.insert(2, 33)
    del list_3[6]
    return list_3


print(change_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


#  5
def merge_dicts(a, b, ab):
    """ #5 объединение словарей по ключам"""
    for key in set(a) | set(b):
        ab[key] = [a.get(key), b.get(key)]
        if ab[key][0] is None:
            ab[key][0] = None
        if ab[key][1] is None:
            ab[key][1] = None
    return ab


print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'c': 3, 'd': 4, 'e': 5}, {}))


#  6*
def output_a_unique_number(list_4, a1):
    """ #6 Возвращает значение уникального числа из массива в переменной a1"""
    for i in list_4:
        if list_4.count(i) == 1:
            a1.append(i)
    print(*a1)
    return a1


output_a_unique_number([1, 5, 2, 9, 2, 9, 1], [])
