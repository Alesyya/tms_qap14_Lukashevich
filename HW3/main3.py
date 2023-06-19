# Задание 1.1
name = "John Snow"
age = 29
print(name)

# Задание 1.2
num_int = 5
num_float = 5.5
my_string = "Hello from Alesya"
bool_var = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)
my_set = {11, 12, 13, 14, 15}
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(num_int)
print(num_float)
print(my_string)
print(bool_var)
print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)

# Задание 1.3
znach1 = 17/2 * 3 + 2
znach2 = 2 + 17/2 * 3
znach3 = 19 % 4 + 15 / 2 * 3
znach4 = (15 + 6) - 10 * 4
znach5 = 17 / 2 % 2 * 3**3
print(znach1, ',', znach2, ',', znach3, ',', znach4, ',', znach5)

# Задание 1.4
neighbour_age1 = 45
neighbour_age2 = 55
neighbour_age3 = 22
print(neighbour_age1 + neighbour_age2 + neighbour_age3)
sum_age = (neighbour_age1 + neighbour_age2 + neighbour_age3)/3
print(int(sum_age))

# Задание 1
a = -1.6
b = 2.99
print(int(a), ',', int(b))

# Задание 2
stroka = 'www.my site.com#about'
stroka_change = stroka.replace('#', '/')
print(stroka_change)

# Задание 3
word_half = 'stroka'
word_add = 'ing'
word = word_half + word_add
print(word)

# Задание 4
q = ' Ivanov  Ivan '
print(q[-5:-1], q[1:7])

# Задание 5
d_stroka = ' Я изучаю Python '
print(d_stroka.strip())

# Задание 6
school = {'1a': 25,
          '1b': 21,
          '2a': 20,
          '2c': 30,
          '3a': 23,
          '4a': 15,
          '5a': 20,
          '6b': 28,
          '7a': 17,
          '8a': 22}
for num_pupil, quantity in school.items():
    print(num_pupil, quantity)

# Задание 7
my_family = ['Mother', 'Me', 'Father', 'Brother']
print(my_family[1])

# Задание 8
q = 'employ'
q1 = 'employment'
if q in q1:
    print(True)

# Задание 9
sentence = 'My name is Agent Smith'
print(sentence[1])
print(sentence[3:16:3])