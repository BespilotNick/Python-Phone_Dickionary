
def checking(param):
    pass

def choose_contact():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.read()

    print(book)

    print('Параметры для выбора контакта: '
          '1 - Порядковый номер. '
          '2 - Фамилия. '
          '3 - Имя. '
          '4 - Номер телефона. '
          '5 - Комментарий.')

    usernum = input('Выберите параметр: ')
    params = '12345'
    while usernum not in params:
        usernum = input('Введено некорректное значение, выберите параметр из списка: ')
        continue
    param = int(usernum)

    if param == 1:
        index = int(input('Введите порядковый номер контакта: '))
        contact = [row for row in book if list(row)[0] == index]
        print(contact)
        return contact
    elif param == 2:
        surname = input('Введите фамилию контакта: ')
        contact = [row for row in book if row[1] == surname]
        return contact
    elif param == 3:
        name = input('Введите имя контакта: ')
        contact = [row for row in book if row[2] == name]
        return contact
    elif param == 4:
        phonenum = input('Введите номер телефона: ')
        contact = [row for row in book if row[3] == phonenum]
        return contact
    elif param == 5:
        comment = input('Введите комментарий: ')
        contact = [row for row in book if row[4] == comment]
        return contact
    else:
        return (f"Contact not found")



choose_contact()