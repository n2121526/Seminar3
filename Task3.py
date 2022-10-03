# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def  diff_max_min(list):
    min = list[0] % 1
    max = list[0] % 1
    k = []
    for i in range(len(list)):
        k.append(round(list[i] % 1, 2))
        if k[i] < min and k[i] != 0:
            min = k[i]
        if k[i] > max:
            max = k[i]
    return max, min

num = [1.1, 1.2, 3.1, 5, 10.01]
max, min = diff_max_min(num)
print(num)
print(round((max-min), 2))