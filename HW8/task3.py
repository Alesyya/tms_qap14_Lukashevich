number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

input_numbers = input().split()
numbers = [int(num) for num in input_numbers]
sorted_numbers = sorted(numbers, key=lambda num: number_names[num])

sorted_names = [number_names[num] for num in sorted_numbers]
output = " ".join(sorted_names)
print(output)