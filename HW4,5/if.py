#  1
def num_positive(num):
    """ Данная функция принимает аргумент num,
    №1 выводит следующее: если число положительное то прибавляется 1, если нет то не изменяется.
    """
    if num > 0:
        print(num + 1)
    else:
        print(num)
    return num


num_positive(5)


#  2
def num_quantity(a, b, c, q):
    """ Данная функция принимает значения аргументов: a, b, c, q
    №2 выводит количество положительных чисел
    """
    if a > 0:
        q += 1
    if b > 0:
        q += 1
    if c > 0:
        q += 1
    print('Количество положительных чисел: ', q)
    return q


num_quantity(2, - 3, 1, 0)


#  3
def check_leap_year():
    """#3 Определяет является ли год висококсный"""
    year = int(input('Введите год:'))
    if (year % 4 == 0 and year % 400 == 0):
        print('Високосный - 366 дней')
    else:
        print('365 дней в году')
    return year


check_leap_year()


#  4
def weeks(name_of_week):
    """ #4 выводит значение строку — название дня недели,
соответствующее введенному числу """
    if name_of_week == 1:
        print('Понедельник')
    if name_of_week == 2:
        print('Вторник')
    if name_of_week == 3:
        print('Среда')
    if name_of_week == 4:
        print('Четверг')
    if name_of_week == 5:
        print('Пятница')
    if name_of_week == 6:
        print('Суббота')
    if name_of_week == 7:
        print('Воскресенье')
    return name_of_week


weeks(3)


#  5
def find_weight(unit_of_mass, y):
    """#5 Возвращает значение массы тела в кг"""
    if unit_of_mass == 1:
        z = y
    if unit_of_mass == 2:
        z = y / 1000000
    if unit_of_mass == 3:
        z = y / 1000
    if unit_of_mass == 4:
        z = y * 1000
    if unit_of_mass == 5:
        z = y * 100
    return z


print(find_weight(5, 2.5))


