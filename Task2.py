# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input('Введите число: '))
print((n % 10) + (n % 100 // 10) + (n // 100))

# Другое решение
# n = input('Введите число: ')
# print(int(n[0]) + int(n[1]) + int(n[2]))