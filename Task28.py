# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя

# *Пример:*

# 2 22

#     4


def sum(a,b):
    if b == 0:
        return a
    return sum(a+1,b-1)

c = int(input("put number 1: "))
d = int(input("put number 2: "))

result = sum(c,d)
print(result)