#  1 Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку.(task1.txt)
with open('task1.txt', 'r') as f:
    q1 = f.read()


def extract_numbers_from_file():
    numbers = list(map(int, q1))
    if len(numbers) < 3:
        print('error')
    else:
        print(numbers[:2], numbers[-2:])


print(extract_numbers_from_file())

#  2 Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные.(task2_sourse, even, odd)
with open('task2_sours', 'r') as sours_file:
    nums = sours_file.read()


def sourse_add_even():
    all_numbers = list(map(int, nums))
    for i in all_numbers:
        if i % 2 == 0:
            with open('even.txt', 'a') as even_nums:
                even_nums.write(str(i))
        if i % 2 != 0:
            with open('odd.txt', 'a') as odd_nums:
                odd_nums.write(str(i))


sourse_add_even()

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.(task3_float)
with open("task3_float.txt", "r") as float_file:
    all_nums = list(map(float, float_file.readline().split(' ')))


def float_to_int():
    nums_float_sqr = []
    for i in all_nums:
        nums_to_list = i ** 2
        nums_float_sqr.append(nums_to_list)

        with open("task3_float.txt", "w") as file:
            file.write(' '.join(map(str, nums_float_sqr)))


float_to_int()


#  4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа. (task4_bin, task4_bin2)
def swap_files(file1, file2):
    with open(file1, 'wb') as bin_file:
        num = [5, 10, 15, 20, 25]
        arr = bytearray(num)
        bin_file.write(arr)

    with open(file2, 'wb') as bin2_file:
        num = [1, 44, 88]
        arr = bytearray(num)
        bin2_file.write(arr)

    with open(file1, "rb") as bin_file, open(file2, "rb") as bin2_file:
        text_from_file1 = bin_file.read()
        text_from_file2 = bin2_file.read()

    with open(file1, "wb") as bin_file, open(file2, "wb") as bin2_file:
        bin_file.write(text_from_file2)
        bin2_file.write(text_from_file1)


swap_files('task4_bin.bin', "task4_bin2.bin")