# 3 task
nums = [2.4, 9.6]


def float_to_int(nums):
    if not all(isinstance(i, float) for i in nums):
        raise TypeError("only float numbers")
    nums_float_sqr = []
    for i in nums:
        nums_to_list = i ** 2
        nums_float_sqr.append(nums_to_list)
    return nums_float_sqr


nums = float_to_int(nums)


with open('task3_float.txt', 'w') as file:
    file.write('\n'.join(str(x) for x in nums) + '\n')


# 4 task
def swap_files(file1, file2):
    with open(file1, 'wb') as bin_file:
        num = [5, 10]
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