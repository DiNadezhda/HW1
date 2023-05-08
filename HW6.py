# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arith_pr(first, diff, count):
    res = []
    for i in range(1,count):
        res.append(first + (i - 1) * diff)
    return res

a1 = int(input("Введите первый элемент массива: "))
d = int(input("Введите разность элементов массива: "))
count_elem = int(input("Введите количество элементов в массиве: "))

print(arith_pr(a1, d, count_elem))

# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def filter_mass(i_min, i_max, input_mass):
    res_index = []
    for i in range(len(input_mass)):
        if input_mass[i] > i_min and input_mass[i]< i_max:
            res_index.append(i)
    return res_index

input_min = int(input("Введите минимальный элемент массива: "))
input_max = int(input("Введите максимальный элемент массива: "))
n = int(input("Введите длину массива:"))
mass = []
for i in range(n):
    mass.append(int(input(f"Введите {i+1} элемент массива:")))

print(filter_mass(input_min, input_max, mass))