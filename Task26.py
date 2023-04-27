# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def degr(a,b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * degr(a,b-1)
    
c = int(input("put number: "))
d = int(input("put degree: "))

result = degr(c,d)
print(f"{result}")


