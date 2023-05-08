# Задача 34:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# **Вывод:** Парам пам-пам

input_str = "пара-ра-рам рам-пам-папам па-ра-па-да"
input_str2 = "парааа-ра-рама рам-пам-папам па-ра-па-да"

def is_rithm(my_str: str) -> str:
    phrases = my_str.split()
    result = []
    for words in phrases:
        result.append(words.split("-"))

    counts = []
    for word in result:
        count = 0
        for i in word:
            count += len(list(filter(lambda x: x in "ауоыиэяюёе", i)))
        counts.append(count)

    if len(set(counts)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


print(is_rithm(input_str))
print(is_rithm(input_str2))

# 2 вариант решения
def rythm(phrase: str) -> str:
    '''Возвращает "Парам пам-пам", если с ритмом всё в порядке
    и "Пам парам", если нет'''
    phrase = phrase.lower().split()
    vovels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
    if len(set(map(
                lambda word: len([letter for letter in word if letter in vovels]),
                phrase))) == 1:
        return 'Парам пам-пам'
    return 'Пам парам'

lirics = input('Введите стих:  ')
print(rythm(lirics))

# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation: callable, num_rows: int = 6, num_columns: int = 6) -> list:
    result = []
    line = []
    for column in range(1, num_columns + 1):
        for row in range(1, num_rows + 1):
            line.append(operation(column, row))
        print(line)
        result.append(line)
        line = []
    return result

print_operation_table(lambda x, y: x * y, 6, 6)

# 2 вариант решения
def print_operation_table(oper: callable,
                          num_rows: int = 6,
                          num_columns: int = 6) -> None:
    '''Выводит таблицу для чисел с заданной опцией oper,
    числом столбцов num_columns и строк num_rows'''
    table = [list(range(i, i + num_columns)) for i in range(1, num_rows + 1)]
    # show_table(table)
    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] = oper(table[i][0], table[0][j])
    show_table(table)

oper = lambda x, y: x * y
n = 4
m = 5
print_operation_table(oper, n, m)
