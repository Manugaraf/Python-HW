# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

def stepen(a, b):
    if b == 0:
        return 1
    a *= stepen(a, b - 1)
    return a
print(stepen(a, b))