# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person.
# Добавьте в него некоторое количество вымышленных друзей с разными именами,
# возрастом и полом.
# Выведите информацию о каждом друге на экран.
# * Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# * Выведите на экран информацию о всех друзьях мужского пола (можно использовать
# функцию filter, либо генератор списков).
# * Заверните код из пунктов 5 и 6 в функции get_oldest_pearson
# и filter_male_person соответственно.
from person import Person

my_friends = [Person('Galya Kuchugurova', 36, 'F'),
              Person('Evgen Purgen', 24, 'M'),
              Person('Boris Britva', 28, 'M'),
              Person('Kama Pulya', 38, 'M'),
              Person('Masha Kulachkova', 23, 'F')]

my_friends[0].print_person_info()
my_friends[1].print_person_info()
my_friends[2].print_person_info()
my_friends[3].print_person_info()
my_friends[4].print_person_info()

def get_oldest_pearson():
    old = my_friends[0]
    for i in my_friends[1:]:
        if i.age > old.age:
            old = i

    old.print_person_info()

def filter_male_person():
    male = list(filter(lambda personal: personal.gender == 'M', my_friends))
    for i in male:
        i.print_person_info()


get_oldest_pearson()
filter_male_person()

