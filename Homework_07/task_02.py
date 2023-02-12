# Пользователь вводит произвольное количество маленьких латинских
# букв через пробел. Напишите функцию remove_vowels, которая принимает
# список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
# Пример:
# Ввод пользователя: a b c d e f
# Результат программы: ['b', 'c', 'd', 'f']
# Используйте функцию filter.
# Список всех гласных английского языка: a, e, i, o, u
alph = list(map(str, input().lower().split()))
gl = ['a', 'e', 'i', 'o', 'u']
def remove_vowels(alph):
   sogl = list(filter(lambda x: x not in gl, alph))
   return sogl
print(remove_vowels(alph))