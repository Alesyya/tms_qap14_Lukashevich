#  1
def find_sum_int(a, b):
    """ Данная функция принимает следующие аргументы : a, b
    Выводит сумму всех целых чисел от а до б"""
    sum = 0
    for num in range(a, b + 1):
        sum += num
    return sum


print(find_sum_int(2, 4))


#  2
def find_sum(x, y):
    """#2 находит сумму всех чисел в диапазоне между двумя заданными натуральными числами"""
    total = 0
    if x >= 0 and y >= 0:
        for i in range(x, y):
            total += i
        return total
    else:
        pass


print(find_sum(1, 5))


#  3
def nums(num):
    """ #3 возвращает значение произведения положительных, сумму и количество отрицательных
        из 10 введенных целых значений
    """
    multiply_of_variables = 1
    count_negative_num = 0
    sum_negative_num = 0
    for i in num:
        if i > 0:
            multiply_of_variables *= i
        if i < 0:
            count_negative_num += 1
            sum_negative_num += i
    return multiply_of_variables, count_negative_num, sum_negative_num


num = [int(x) for x in input('Введите числа через пробел: ').split(' ')]

print(nums(num))


#  4
def find_best_swimmer():
    """
     # 4 выводит лучший результат среди 6 участников
    """
    swimmers = {"Бекиш Александр": 21.07,
                "Будник Алексей": 20.34,
                "Гребень Анастасия": 22.12,
                "Давидович Татьяна": 30,
                "Дешук Дмитрий": 24.01,
                "Казак Анна": 28.17}
    return min(swimmers, key=swimmers.get)


print(find_best_swimmer())


#  5
def output_a_unique_number(list_of_numbers):
    """ #5 Возвращает из списка цифру встречающуюся единожды"""
    for i in list_of_numbers:
        if list_of_numbers.count(i) == 1:
            return i


print(output_a_unique_number([1, 5, 2, 9, 2, 9, 1]))
