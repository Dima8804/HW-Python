# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
array = []
period = int(input('period: '))
x = int(input('num2: '))
count = 0
for i in range(period):
    num = randint(1,9)
    if x == num:
        count += 1
    array.append(num)
print(array) 
print(count)





