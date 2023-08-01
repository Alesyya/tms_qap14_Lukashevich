# 0 Создать мининум два класса. Один класс будет родитель и несколько наследников
# 1 Реализовать конструкторы для инициализации
# 2 Реализовать вывод данных в основном и дополнительном классе
# 3 Реализовать полиморфизм (перезгрузка и переопределение)
# 4 Реализовать инкапсуляцию методов и свойств

class Books(object):

     def __init__(self, name_of_genre, name_of_book, year_of_issue, author):
        self.name_of_genre = name_of_genre
        self.name_of_book = name_of_book
        self.year_of_issue = year_of_issue
        self._author = author

     def _print_info(self):
         print(f'On the shelf is the book {self.name_of_book}. This book is a {self.name_of_genre} genre and {self.year_of_issue} years of release.')
         print(f'This ganre of books is invented by {self._author}.')

     def print_info(self):
         self._print_info()


class Fantasy(Books):

    def __init__(self, name_of_genre, name_of_book, year_of_issue, author, fantasy_intresting):
        super().__init__(name_of_genre, name_of_book, year_of_issue, author)

        self.fantasy_intresting = fantasy_intresting


    def print(self):
        print(f'This fantasy is so {self.fantasy_intresting} , decide to watching this or not.')


    def read_fantasy(self, read = True):
        if read is False:
            print('You should definitely watch something in this genre')
        else:
            print('Well done, keep reading the following genres.')

    @property
    def author(self):
        return f'The author of the book is {self._author}'

    @author.setter
    def author(self, author):
        self._author = author


book_fantasy1 = Fantasy('Novel', 'Master and Margarita', 1928, 'A.Pushkin', True)
book_fantasy1.print_info()

book_fantasy2 = Fantasy('Fantasy', 'Хроники Нарнии', 1949, 'Джордж Макдональд', True)
book_fantasy2.read_fantasy()
print(book_fantasy2.author)