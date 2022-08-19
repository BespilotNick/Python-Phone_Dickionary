import random
from ipython_genutils.py3compat import xrange
import Export_dict as expd

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

    with open('Surnames&Names/Comments.txt', 'r', encoding='utf-8') as com:
        com_lst = com.read().split('\n')
    comments = list(random.choices(com_lst, k=(len(line))))

    phonebook = [[] for x in xrange(len(line))]

    # Тут можно было через zip, но кортежи неизмняемы, а нам нужно будет редактировать контакты.
    # Хотя в модуле редактирования можно было бы написать функцию конвертации нужного кортежа в список и затем изменить, но...

    for i in range(len(line)):
        phonebook[i].append(line[i])
        phonebook[i].append(surname[i])
        phonebook[i].append(name[i])
        phonebook[i].append(phone[i])
        phonebook[i].append(comments[i])

    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write('')
        for row in phonebook:
            data.write(str(row) + '\n')

create_phonebook()

