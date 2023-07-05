#  1
def find_sum(a, b):
    """ Данная функция принимает следующие аргументы : a, b
    Выводит сумму всех целых чисел от а до б"""
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum


print(find_sum(2, 4))


#  2
def find_sum1(x, y):
    """#2 находит сумму всех чисел в диапазоне между двумя заданными натуральными числами"""
    total = 0
    if x >= 0 and y >= 0:
        for i in range(x, y):
            total += i
        return total
    else:
        pass


print(find_sum1(1, 5))


#  3
def nums(a):
    """ #3 возвращает значение произведения положительных, сумму и количество отрицательных
        из 10 введенных целых значений
    """
    numer = 1
    s = 0
    t = 0
    for i in a:
        if i > 0:
            numer *= i
        if i < 0:
            s += 1
            t += i
    return numer, s, t


a = [int(x) for x in input('Введите числа через пробел: ').split(' ')]


print(nums(a))


#  4
def best_result(**kwargs):
    """ # 4 выводит лучший результат среди 6 участников"""
    best_result1 = min(kwargs.values())
    for key, value in kwargs.items():
        if value == best_result1:
            print(best_result1)
            return key, value


best_result(Бекиш_Александр='21.07',
            Будник_Алексей='20.34',
            Гребень_Анастасия='22.12',
            Давидович_Татьяна='30',
            Дешук_Дмитрий='24.01',
            Казак_Анна='28.17')


#  5
def output_a_unique_number(list_4):
    """ #5 Возвращает из списка цифру встречающуюся единожды"""
    for i in list_4:
        if list_4.count(i) == 1:
            return i


print(output_a_unique_number([1, 5, 2, 9, 2, 9, 1]))
