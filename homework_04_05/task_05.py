# Пользователь вводит произвольное число.
# Посчитайте сумму цифр этого числа используя операторы % и //
# Пример для числа 12.
# Ответ должен быть получен примерно так:
# answer = 12 % 10  # 2
# answer += 12 // 10  # 1
# print(answer)  # 3
num = int(input())
summ = 0
while num > 0:
    ost = num % 10
    summ += ost
    num = num // 10
print(summ)