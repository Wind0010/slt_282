# принципы ооп
# 4 Наследование,Полиморфизм,Инкапсуляция,Абстракция
# gitignore
# на основе одного класса можно создать другие классы
import random
# from lesson1 import Manga
# naruto=Manga('Naruto','Kishimoto')

# print(naruto)

# cупер класс\родительский класс
class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def reads(self):
        print('я читаю книгу:',self.title)

    def words_author(self):
        print('привет меня зовут:',self.author,' читай с лева на право')

# DRY -


# дочерний класс
class Manga(Book):
    def _init_(self, title, author,png='png'):
        super()._init_(title, author)
        Book._init_(self, title, author)
        self.png = png
    #     обращается к внутренностям родительского класса
    def reads(self):
        print('я читаю мангу:',self.title)
        super().words_author()
        manga = Manga('naruto', 'Kishimoto')
        manga.reads()