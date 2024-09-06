
import csv
import json


def add_contact():
    """
    Добавляет новый контакт в телефонную книгу. Позволяет отменить добавление и вернуться в меню.
    """
    while True:
        surname = input('Введите фамилию (или "m" для возврата в меню): ')
        if surname == 'm':
            return  # Возврат в основное меню
        name = input('Введите имя (или "m" для возврата в меню): ')
        if name == 'm':
            return
        phone = input('Введите номер телефона (или "m" для возврата в меню): ')
        if phone == 'm':
            return
        comment = input('Введите комментарий (или "m" для возврата в меню): ')
        if comment == 'm':
            return

        # После ввода данных контакт добавляется
        with open('Phonebook.txt', 'a', encoding='utf-8') as data:
            new_id = sum(1 for line in open('Phonebook.txt')) + 1
            new_contact = f'{new_id};{surname};{name};{phone};{comment}\n'
            data.write(new_contact)
        print('Контакт успешно добавлен!')
        break  # Выход из функции добавления


def show_dict():
    """
    Выводит на экран содержимое телефонной книги. Позволяет вернуться в меню.
    """
    while True:
        with open('Phonebook.txt', 'r', encoding='utf-8') as data:
            book = data.readlines()

        if not book:
            print('Телефонная книга пуста.')
        else:
            print('Телефонная книга:')
            for contact in book:
                print(contact.strip())

        user_input = input('Введите "m" для возврата в меню: ')
        if user_input == 'm':
            return  # Возврат в меню


def choose_contact():
    """
    Позволяет пользователю выбрать контакт по одному из параметров (номер, фамилия, имя, телефон, комментарий).
    Возвращает выбранный контакт в виде списка.
    """
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.readlines()

    print('Параметры для выбора контакта: '
          '1 - Порядковый номер. '
          '2 - Фамилия. '
          '3 - Имя. '
          '4 - Номер телефона. '
          '5 - Комментарий.')
    print('Введите "m" для возврата в меню.')

    usernum = input('Выберите параметр: ')
    if usernum == 'm':
        return  # Возврат в меню

    params = '12345'
    while usernum not in params:
        usernum = input('Введено некорректное значение, выберите параметр из списка: ')

    param = int(usernum)

    if param == 1:
        index = int(input('Введите порядковый номер контакта: '))
        for row in book:
            contact_data = row.split(';')
            if int(contact_data[0]) == index:
                return contact_data
    elif param == 2:
        surname = input('Введите фамилию контакта: ')
        return [row for row in book if surname in row]
    elif param == 3:
        name = input('Введите имя контакта: ')
        return [row for row in book if name in row]
    elif param == 4:
        phonenum = input('Введите номер телефона: ')
        return [row for row in book if phonenum in row]
    elif param == 5:
        comment = input('Введите комментарий: ')
        return [row for row in book if comment in row]


def change_contact():
    """
    Позволяет пользователю изменить информацию о существующем контакте.
    Пользователь выбирает контакт и вводит новые данные.
    """
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.readlines()

    contact = choose_contact()

    if contact:
        index = book.index(';'.join(contact))
        print(f'Редактируем контакт: {";".join(contact)}')

        surname = input('Введите новую фамилию или оставьте пустым для пропуска: ')
        name = input('Введите новое имя или оставьте пустым для пропуска: ')
        phone = input('Введите новый номер телефона или оставьте пустым для пропуска: ')
        comment = input('Введите новый комментарий или оставьте пустым для пропуска: ')

        old_data = contact
        new_data = [
            old_data[0],
            surname or old_data[1],
            name or old_data[2],
            phone or old_data[3],
            comment or old_data[4].strip(),
        ]

        book[index] = ';'.join(new_data) + '\n'

        with open('Phonebook.txt', 'w', encoding='utf-8') as data:
            data.writelines(book)

        print('Контакт успешно изменён!')

    user_input = input('Введите "m" для возврата в меню: ')
    if user_input == 'm':
        return  # Возврат в меню


def delete_contact():
    """
    Удаляет контакт из телефонной книги. Пользователь выбирает контакт, затем подтверждает удаление.
    """
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.readlines()

    contact = choose_contact()

    if not contact:
        print('Контакт не найден.')
        return

    print(f'Вы выбрали для удаления контакт: {";".join(contact)}')
    confirm = input('Вы уверены, что хотите удалить этот контакт? (y/n): ').lower()

    if confirm == 'y':
        book.remove(';'.join(contact) + '\n')

        with open('Phonebook.txt', 'w', encoding='utf-8') as data:
            data.writelines(book)

        print('Контакт успешно удалён.')
    else:
        print('Удаление отменено.')

    user_input = input('Введите "m" для возврата в меню: ')
    if user_input == 'm':
        return  # Возврат в меню


def export_dict():
    """
    Предлагает вариант экспорта телефонной книги в различных форматах: 
    CSV, JSON или TXT.
    """
    while True:
        print('Выберите формат для экспорта телефонной книги:')
        print('1 - Экспорт в CSV.')
        print('2 - Экспорт в JSON.')
        print('3 - Экспорт в TXT.')
        print('0 - Вернуться в основное меню.')

        usernum = input('Выберите действие: ')
        options = '0123'
        while usernum not in options:
            usernum = input('Введено некорректное значение, выберите действие из списка: ')

        if usernum == '1':
            export_to_csv()
        elif usernum == '2':
            export_to_json()
        elif usernum == '3':
            export_to_txt()
        elif usernum == '0':
            print('Возврат в основное меню...')
            break  # Возврат в основное меню



def import_dict():
    """
    Предлагает вариант импорта телефонной книги из различных форматов: 
    CSV, JSON или TXT.
    """
    while True:
        print('Выберите формат для импорта телефонной книги:')
        print('1 - Импорт из CSV.')
        print('2 - Импорт из JSON.')
        print('3 - Импорт из TXT.')
        print('0 - Вернуться в основное меню.')

        usernum = input('Выберите действие: ')
        options = '0123'
        while usernum not in options:
            usernum = input('Введено некорректное значение, выберите действие из списка: ')

        if usernum == '1':
            import_from_csv()
        elif usernum == '2':
            import_from_json()
        elif usernum == '3':
            import_from_txt()
        elif usernum == '0':
            print('Возврат в основное меню...')
            break  # Возврат в основное меню


def export_to_csv():
    """
    Экспортирует телефонную книгу в формат CSV.
    """
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = [line.strip().split(';') for line in data]

    with open('Phonebook.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(book)
    print('Экспорт в CSV завершён.')


def export_to_json():
    """
    Экспортирует телефонную книгу в формат JSON.
    """
    phonebook = []
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            contact_data = line.strip().split(';')
            phonebook.append({
                "id": contact_data[0],
                "surname": contact_data[1],
                "name": contact_data[2],
                "phone": contact_data[3],
                "comment": contact_data[4]
            })

    with open('Phonebook.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(phonebook, jsonfile, indent=4, ensure_ascii=False)
    print('Экспорт в JSON завершён.')


def export_to_txt():
    """
    Экспортирует телефонную книгу в текстовый файл.
    """
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.readlines()

    with open('Phonebook_export.txt', 'w', encoding='utf-8') as txtfile:
        for contact in book:
            txtfile.write(contact)
    print('Экспорт в TXT завершён.')


def import_from_csv():
    """
    Импортирует данные из CSV-файла в телефонную книгу (TXT).
    """
    try:
        with open('Phonebook.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            phonebook = [row for row in reader]

        with open('Phonebook.txt', 'w', encoding='utf-8') as data:
            for row in phonebook:
                data.write(';'.join(row) + '\n')

        print('Импорт из CSV завершён.')
    except FileNotFoundError:
        print('Файл не найден. Убедитесь, что файл Phonebook.csv существует.')

def import_from_json():
    """
    Импорт данных из JSON файла и добавление в телефонную книгу.
    Если файл не найден, выводится сообщение об ошибке.
    """
    try:
        with open('Phonebook.json', 'r', encoding='utf-8') as j_file:
            phonebook = json.load(j_file)

        with open('Phonebook.txt', 'a', encoding='utf-8') as t_file:
            for contact in phonebook:
                # Добавляем каждый контакт в текстовый файл
                t_file.write(';'.join(contact) + '\n')

        print('Импорт из JSON завершён.')
    except FileNotFoundError:
        print('Файл Phonebook.json не найден.')
    except json.JSONDecodeError:
        print('Ошибка чтения JSON файла.')

def import_from_txt():
    """
    Импорт данных из другого текстового файла в основную телефонную книгу.
    Если файл не найден, выводится сообщение об ошибке.
    """
    try:
        with open('Phonebook_import.txt', 'r', encoding='utf-8') as import_file:
            imported_contacts = import_file.readlines()

        with open('Phonebook.txt', 'a', encoding='utf-8') as phonebook_file:
            phonebook_file.writelines(imported_contacts)

        print('Импорт из TXT завершён.')
    except FileNotFoundError:
        print('Файл Phonebook_import.txt не найден.')
