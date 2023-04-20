# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint
len_nums = int(input ('Put list lenght: '))

for i in range(len_nums):
    nums = [randint(1,100)]
    print("List: ", *nums)
x = int(input('Enter x: '))

min_pos = nums[0]
for i in nums:
    diff_current = abs(i-x)
    if diff_current < min_pos:
        res = i
        min_pos = diff_current

print(f'Result is {res}')
