# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
#
# Нужно написать функцию RLE, которая на выходе даст строку вида :
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений ;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

# def rle(input_str: str) -> str:
#     if not input_str.isalpha():
#         return "невалидная строка"
#     temp = input_str[0]
#     temp_count = 1
#     t = []
#     for i in range(1, len(input_str)):
#         if temp == input_str[i]:
#             temp_count += 1
#         else:
#             t.append((temp, temp_count))
#             temp = input_str[i]
#             temp_count = 1
#     t.append((temp, temp_count))
#     rez_str = ""
#     for elem in t:
#         if elem[1] > 1:
#             rez_str += elem[0]
#             rez_str += str(elem[1])
#         else:
#             rez_str += elem[0]
#     return rez_str


# print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
# print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBB5286BBBBBBBBBBBBBBBBBBB'))
# print(rle(''))

# 2 вариант решения

def rle(some_str):
    res_list = []
    some_str += ' '
    temp_letter = some_str[0]
    count_letter = 1
    for ind in range(1, len(some_str)):
        if some_str[ind] == temp_letter:
            count_letter += 1
        else:
            if count_letter == 1:
                res_list.append(f'{temp_letter}')
            else:
                res_list.append(f'{temp_letter}{count_letter}')
            count_letter = 1
            temp_letter = some_str[ind]
    print(*res_list, sep='')

rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')

# 3. Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_word(input_l):
    temp_dict = {frozenset(input_l[0]): [input_l[0]]}
    for i in range(1, len(input_l)):
        key = frozenset(input_l[i])
        if key in temp_dict.keys():
            temp_dict[key].append(input_l[i])
        else:
            temp_dict[key] = [input_l[i]]
    return list(temp_dict.values())


print(group_word(input_list))

# Второй вариант решения задачи
def group_letter(input_list):
    word_dict = {}
    for word in input_list:
        if (frozenset(word), len(word)) not in word_dict:
            word_dict[frozenset(word), len(word)] = [word]
        else:
            word_dict[frozenset(word), len(word)].append(word)
    res_list = []
    for value in word_dict.values():
        res_list.append(value)
    return res_list

print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat"]))
