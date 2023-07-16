def num_multiplication(n=5):
    """ #1 возвращает значение произведения всех чисел от 0 до N"""
    i = 0
    mul = 1
    while i < n:
        i += 1
        mul *= i
    return mul


print(num_multiplication())


def calculate_years():
    """ #2 Возвращает значение через сколько лет площадь первых сортов будет
составлять меньше 10% от площади вторых сортов."""
    s1 = 20
    s2 = 40
    year = 0
    while s1 > (s2 * 0.1):
        s1 *= 2
        s2 *= 3
        year += 1
    return year


print(calculate_years())


def count_and_sum_digits(n):
    """ #3 Возвращает количество и сумму цифр числа, используя операции деления нацело и взятия
остатка от деления """
    sum1 = 0
    count = 0
    while n > 0:
        num = n % 10
        sum1 += num
        n = n // 10
        count += 1
    return count, sum1


print(count_and_sum_digits(23))


def family_age():
    """ №4 Возвращает возраст деда и внука, значение через сколько лет дед станет вдвое старше
внука"""
    age_grandson = 2
    age_grandfather = 30
    count2 = 0
    while age_grandfather < 100 and age_grandson < 100:
        age_grandfather += 1
        age_grandson += 1
        count2 += 1
        while age_grandfather == age_grandson * 2:
            print(age_grandson, age_grandfather, count2)
            return age_grandson, age_grandfather, count2


family_age()



