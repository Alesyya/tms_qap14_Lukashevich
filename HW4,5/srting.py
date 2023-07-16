#  1
def extract_from_string(str_1):
    """ Данная функция принимает следующие аргументы : str_1, str_2
        #1 Извлекает из строки первый символ, затем последний, третий с начала и третий с
        конца и измеряет длинну строки
    """
    #  1
    print(str_1[0])
    print(str_1[-1])
    print(str_1[2:-2])
    print(len(str_1))
    return str_1


extract_from_string('My name is Alesya')


def string_slices(str_2):
    """ #2 Данная функция принимает аргумент : str_2,
    Возвращает значения срезов строки, типа str.
    """

    #  2
    slice1 = str_2[0:8]
    slice2 = str_2[7:11]
    slice3 = str_2[::3]
    slice4 = str_2[::-1]
    return slice1, slice2, slice3, slice4


print(', '.join(string_slices('automated testing')))


#  3(именованное)
def print_name(str_3, name):
    """ #3 Данная функция принимает следующие аргументы : str_3, name
        Возвращает вместо 2ого “name” любое имя, возращает результат типа str.
    """

    print(str_3.format(name=name))
    return str_3


print_name('my name is {name}', 'Alesya')


#  4
def print_test_tring(test_tring):
    """ #4 Выводит место буквы w, кол-во букв l, начинается ли строка с подстроки: “Hello”,
        заканчивается ли строка подстрокой: “qwe”, возращает результат типа str.
    """

    q1 = test_tring.find('w')
    q2 = test_tring.count('l')
    q3 = test_tring.startswith('Hello')
    q4 = test_tring.endswith('qwe')
    return q1, q2, q3, q4


print(', '.join(map(str, print_test_tring('Hello world!'))))