# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count)/
# Замерьте время работы двух алгоритмов и сравните. Подумайте, почему оно отличается.

# 5
# 1 2 3 4 5
# 3
# -> 1

# РЕШЕНИЕ №16
# input_list = []
# n = int(input('Введите количество элементов в массиве: '))
# for _ in range(n):
#     input_list.append(int(input('Введите целое число: ')))
# print(input_list)
# x = int(input('Введите число X: '))
#
# import time
#
# start = time.perf_counter()
# count = 0
# for i in range(n):
#     if input_list[i] == x:
#         count += 1
# print(f'Число {x} встречается {count} раз')
# end = time.perf_counter()
# first_time = end - start
#
# # Метод count() возвращает количество раз, когда указанный элемент появляется в списке.
# start = time.perf_counter()
# count = input_list.count(x)
# print(f'Число {x} встречается {count} раз')
# end = time.perf_counter()
# second_time = end - start
#
# print(f'Метод count() работает в {first_time / second_time} раз быстрее моего способа')

# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# РЕШЕНИЕ №18
# input_list = []
# n = int(input('Введите количество элементов в массиве: '))
# for _ in range(n):
#     input_list.append(int(input('Введите целое число: ')))
# print(input_list)
# x = int(input('Введите число X: '))
#
# next_number = input_list[0]
# for i in input_list:
#     if abs(i - x) < abs(next_number - x):
#         next_number = i
#
# print(f'Ближайшее число к {x} в списке {input_list} является {next_number}')


# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
#
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
#
# Ввод:
# ноутбук
# Вывод:
# 12

import re

word = input('Введите слово: ')
scrabble_rules = {'[A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т]': '1',
                  '[D, G, Д, К, Л, М, П, У]': '2', '[B, C, M, P, Б, Г, Ё, Ь, Я]': '3',
                  '[F, H, V, W, Y, Й, Ы]': '4', 'K, Ж, З, Х, Ц, Ч': '5', '[J, X, Ш, Э, Ю]': '8',
                  '[Q, Z, Ф, Щ, Ъ]': '10'}

for i in scrabble_rules:
    word = re.sub(i, scrabble_rules[i], word)
print(sum(map(int, word)))

