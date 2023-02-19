# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# * Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count
from student import Student
students = [Student('Zanna', 9),
            Student('Anya', 8),
            Student('Ivan', 3),
            Student('Matvei', 4)]
def calc_sum_scholarship():
    summ = students[0].get_scholarship()
    for i in students[1:]:
        summ += i.get_scholarship()
        return summ

def get_excellent_student_count():
    count = 0
    for i in students:
        if i.is_excellent():
            count += 1
    return count

print(calc_sum_scholarship(), "Рублеу")
print(get_excellent_student_count())