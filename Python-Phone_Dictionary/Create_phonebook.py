import random

def create_phonebook():
    num = ''
    while not num.isdigit():
        num = input('Выберите количество записей в справочнике: ')
        if not num.isdigit():
            print('Введено некорректное значение! Введите целое число')
            continue

    line = [i for i in range(1, int(num)+1)]

    with open('Surnames&Names/Surnames.txt', 'r', encoding='utf-8') as sur:
        sur_lst = sur.read().split('\n')
    surname = list(random.choices(sur_lst, k=(len(line))))

    with open('Surnames&Names/Names.txt', 'r', encoding='utf-8') as nam:
        nam_lst = nam.read().split('\n')
    name = list(random.choices(nam_lst, k=(len(line))))

    phone = [random.randint(89010000000, 89990000000) for i in range(len(line))]

    print(line)
    print(surname)
    print(name)
    print(phone)
create_phonebook()

