#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = int(input("Введите количество элементов в списке: ")) 
import random 
list = [random.randint(1, 50) for i in range(n)]

def proiz_num(ls):
    res = []
    for i in range((len(ls) + 1) // 2):
        res.append(ls[i] * ls[len(ls)-1-i])
    return res

print(list, end=" => ")
print(proiz_num(list))

