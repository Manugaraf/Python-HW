# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите кол-во монет: '))
a = 0
for i in range(n):
    side = int(input('Введите сторону 1 или 0: '))
    if side == 1:
        a += 1
print(f'Нужно перевернуть {n - a}')
