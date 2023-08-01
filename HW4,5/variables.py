# Работа с переменными
def variables_task(var_int, var_float):
    """ Данная функция принимает следующие аргументы : var_int, var_float, var_str
        #2 значение var_int увеличили в 3.5 раза,результат связали с big_int
        #3 значение var_float уменьшили на единицу и результат связали с той же переменной
        #4 разделили var_int на var_float, а затем big_int на var_float
        #5 изменили значение переменной var_str на "NoNoYesYesYes
        #6 вывели значение всех переменных
    """
    #  2
    big_int = var_int * 3
    print(big_int)
    #  3
    var_float = var_float - 1
    print(var_float)
    #  4
    print(var_int/var_float)
    print(big_int/var_float)
    #  5
    var_str = "NoYes"
    print(var_str[0:2]*2 + var_str[2:6]*3)
    return big_int, var_int, var_str, var_float


variables_task(10, 8.4)

