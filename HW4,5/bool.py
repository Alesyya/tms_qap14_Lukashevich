#  1
a = 20
b = 10


def construct_bool_statements(a, b):
    """ #2,#3 Данная функция принимает следующие аргументы : a,b.
        Возвращает значения четырех сложных логических выражения созданных с помощью оператора and, or типа bool.
    """

    #  2
    print(a + b != 0 and b == 0)
    print(a - b < a + b and b < 0)
    print(a**2 != 401 and b > 0)
    print(a and b != str)
    #  3
    print(a != 3 or b != 3)
    print(a * b == 200 or a * b != 202)
    print(a + 5 > 60 or b + 100 < 101)
    print(a / b > 20 or a * b > 199)
    return "bool statements constracture"


construct_bool_statements(1, 5)


def construct_bool_string(bool_1, bool_2):
    """ #4 Данная функция принимает следующие аргументы : bool_1, bool_2,
        возвращает знаение типа bool
    """

    #  4
    print(bool_1[1] and bool_2[1] == "v")
    print(bool_1[4] and bool_2[1] == "y")
    print(bool_1 == "Alesya" or bool_2 == "Python")
    return bool_1, bool_2


construct_bool_string("Alesya", "Python")

