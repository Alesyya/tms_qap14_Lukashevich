#  1
def create_school(**kwargs):
    """ #1 Создаёт словарь"""

    school = {}
    for key, value in kwargs.items():
        school[key] = value
    return school


print((
    {'1a': 25, '1b': 21, '2a': 20, '2c': 30, '3a': 23, '4a': 15, '5a': 20, '6b': 28, '7a': 17, '8a': 22},
    {'9b': 12, '10a': 11}))


def change_school(school, school_1):
    """ #2 Данная функция принимает следующие аргументы : school, school_1,
        Выводит информацию по кол-во участников в 1б классе
        #3 В переменную school перезаписываются значения с ключами '2a', '2c', '3a'
        #4 Возвращает значение переменной school, типа dict
    """

    #  2
    print(school['1b'])
    #  3
    school['2a'] = 25
    school['2c'] = 0
    school['3a'] = 12
    print(school)
    school.update(school_1)
    print(school)
    del school['1a']
    #  4
    return school


print(change_school(
    {'1a': 25, '1b': 21, '2a': 20, '2c': 30, '3a': 23, '4a': 15, '5a': 20, '6b': 28, '7a': 17, '8a': 22},
    {'9b': 12, '10a': 11}))

