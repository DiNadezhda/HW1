'''Задача №49.
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной'''
# import  functions

def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО:   ')
    tel_number = input('Введите номер телефона:   ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')

def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])
# join соединяет строчки по разделителю

def find_data() -> None:
    '''Осущетсвляет поиск по справочнику'''
    data = input('Введите данные для поиска:   ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска:  ')
    print(search(tel_book, data))

def edit_data():
    '''Вносит изменения в данные '''
    with open("book.txt", "r", encoding="utf-8") as fd:
        all_data = fd.read()
        all_data = all_data.split("\n")
        for elem in list(enumerate(all_data)):
            print(f"{elem[0]} {elem[1]}")
        num_line = int(input("Какую строку хотите изменить?: "))
        all_data[num_line] = edited(all_data[num_line])
        print(all_data[num_line])
        rewrite_file("\n".join(all_data))

def rewrite_file(data: str):
    '''Перезаписывает файл'''
    with open("book.txt", "w", encoding="utf-8") as fd:
        fd.write(data)

def edited(text: str) -> str:
    fio = input("Введите фамилию: ")
    tel = input("Введите телефон: ")
    if len(fio) == 0:
        fio = text.split(" | ")[0]
    if len(tel) == 0:
        tel = text.split(" | ")[1]
    return f"{fio} | {tel}"

def delete_data():
    '''Удаление данных'''
    with open("book.txt", "r", encoding="utf-8") as fd:
        all_data = fd.read()
        all_data = all_data.split("\n")
        for elem in list(enumerate(all_data)):
            print(f"{elem[0]} {elem[1]}")
        num_line = int(input("Какую строку хотите удалить?: "))
        print(f'Удаление строки: {all_data[num_line]}')
        del all_data[num_line]
        rewrite_file("\n".join(all_data))


while True:
    print('1. Вывод данных, 2. Добавление, 3. Поиск, 4. Изменение, 5. Удаление')
    mode = int(input('Выберите нужный пункт:  '))
    if mode  == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode == 4:
        edit_data()
    elif mode == 5:
        delete_data()
    else:
        break

# with open('book.txt', 'w', encoding='utf-8') as f:
#     f.write('фио | номер телефона')
#
#     '''Дозапись в файл'''
# with open('book.txt', 'a', encoding='utf-8') as f:
#     f.write('\nфио1 | номер телефона1')
#
# with open('book.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

