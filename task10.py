# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# С клавиатуры вводятся число монет и сами монеты построчно.
# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

from random import randint
n = int(input('put number coins: '))
count = 0
for i in range(0, n, 1):
    coin = randint(0,1)
    print(coin)
    if coin < 1:
     count = count + 1
print(f'coins to be flipped: {count}')
