#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Введите целое число: "))

def transformation(num):
    res = ""
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res

print(f'{number} -> {transformation(number)}')

