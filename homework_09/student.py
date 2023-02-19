# Создайте файл student.py. Делайте задание в этом файле.
# Создайте класс Student, с полями full_name, agerage_mark (средняя оценка).
# Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию
# данного студента по следующему алгоритму:
# Если средняя оценка < 6 - вернуть 60 (рублей)
# Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
# Если средняя оценка >= 8 - вернуть 100 (рублей)
# Добавить в класс метод is_excellent, который возвращает bool:
# True, если средняя оценка >= 9
# False, иначе
class Student:
    def __init__(self, full_name, agerage_mark):
        self.full_name = full_name
        self.agerage_mark = agerage_mark
    def get_scholarship(self):
        if self.agerage_mark < 60:
            return 60
        elif 6 <= self.agerage_mark < 8:
            return 80
        elif self.agerage_mark >= 8:
            return 100

    def is_excellent(self):
        return self.agerage_mark >= 9

