# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.
# Пример:
# Ввод: 13 -> 1, 2, 4, 8

n = int(input("put number: "))
count = 1

while count < n:
   
   print(count)
   count = count * 2
   
