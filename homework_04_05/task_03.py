#Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор, пока ответ не будет корректным.

for n in range(0, 101):
    print(n)
    ans = input('Should we break?')
    if ans == "yes":
        break
    if ans == "no":
        continue
    else:
        print("Don't understand you")