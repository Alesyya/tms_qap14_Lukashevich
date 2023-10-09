# Цветочница.
# Определить иерархию и создать несколько цветов.
# Собрать букет с использованием аксессуаров(ленточка + бабочка) с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов стоимости.
# Узнать, есть ли цветок в букете.

class Flowers(object):
    def __init__(self, name, wither_time, price, accessory, accessory_price):
        self.name = name
        self.wither_time = wither_time
        self.price = price
        self.accessory = accessory
        self.accessory_price = accessory_price

    def print(self):
        print(self.name, self.wither_time, self.price)

    def determine_cost_of_the_bouquet(self):
        a = input('Выберите цветы которые хотите в букет: розы, пионы, гипсофилы: ')
        if a == 'розы':
            roses = int(input('Сколько роз нужно: '))
            rose_accessory = input('Выберите аксессуар для роз (лента или бантик): ')
            if rose_accessory == 'лента':
                accessory_price = 2
            elif rose_accessory == 'бантик':
                accessory_price = 3
            else:
                accessory_price = 0
            cost = roses * rose.price + accessory_price * roses
            print(f'Цена за букет из {roses} роз с аксессуаром {rose_accessory} составляет {cost} долларов')
        elif a == 'пионы':
            peonies = int(input('Сколько пионов нужно: '))
            peony_accessory = input('Выберите аксессуар для пионов (бабочка или цветок): ')
            if peony_accessory == 'бабочка':
                accessory_price = 4
            elif peony_accessory == 'цветок':
                accessory_price = 5
            else:
                accessory_price = 0
            cost = peonies * peony.price + accessory_price * peonies
            print(f'Цена за букет из {peonies} пионов с аксессуаром {peony_accessory} составляет {cost} долларов')
        elif a == 'гипсофилы':
            gypsophilas = int(input('Сколько гипсофил нужно: '))
            gypsophila_accessory = input('Выберите аксессуар для гипсофилов: ')
            if gypsophila_accessory == 'блестки':
                accessory_price = 1
            elif gypsophila_accessory == 'лента':
                accessory_price = 2
            else:
                accessory_price = 0
            cost = gypsophilas * gypsophila.price + accessory_price * gypsophilas
            print(
                f'Цена за букет из {gypsophilas} гипсофил с аксессуаром {gypsophila_accessory} составляет {cost} долларов')
        else:
            print('Таких цветов у нас нет')


class Rose(Flowers):
    def __init__(self, name, wither_time, price, accessory, accessory_price):
        super().__init__(name, wither_time, price, accessory, accessory_price)


class Peony(Flowers):
    def __init__(self, name, wither_time, price, accessory, accessory_price):
        super().__init__(name, wither_time, price, accessory, accessory_price)


class Gypsophila(Flowers):
    def __init__(self, name, wither_time, price, accessory, accessory_price):
        super().__init__(name, wither_time, price, accessory, accessory_price)


rose = Rose("Роза", 10, 7, 'лента', 2)
peony = Peony("Пион", 5, 15, 'бабочка', 4)
gypsophila = Gypsophila("Гипсофила", 12, 10, 'блестки', 1)
bouquet = [rose, peony, gypsophila]
total_wither_time = 0
for flower in bouquet:
    total_wither_time += flower.wither_time
average_wither_time = total_wither_time / len(bouquet)
print(f'Среднее время жизни цветов в букете: {average_wither_time} дней')

sorted_bouquet = sorted(bouquet, key=lambda x: x.price)
print('Сортировка цветов по стоимости:')
for flower in sorted_bouquet:
    flower.print()

if rose in bouquet:
    print('Роза есть в букете')
else:
    print('Розы нет в букете')




