import Show_dict as shd
import Add_contact as adc
import Change_contact as cngc
import Delete_contact as dec
import Export_dict as expd
import Import_dict as impd
import time

def choose_operation():
    print('Вы находитесь в основном меню, ниже приведены возможные варианты действий:')
    time.sleep(0.75)
    print('1 - Посмотреть телефонную книгу.')
    time.sleep(0.5)
    print('2 - Добавить контакт.')
    time.sleep(0.5)
    print('3 - Редактировать контакт.')
    time.sleep(0.5)
    print('4 - Удалить контакт.')
    time.sleep(0.5)
    print('5 - Импортировать данные из телефонного справочника.')
    time.sleep(0.5)
    print('6 - Экспортировать данные в телефонный справочник.')
    time.sleep(0.5)
    print('7 - Выход.\n')
    time.sleep(1)

    usernum = input('Выберите действие: ')
    actions = '1234567'
    while usernum not in actions:
        usernum = input('Введено некорректное значение, выберите действие из списка: ')
        continue

    if usernum == 1:
        shd.show_dict()
    elif usernum == 2:
        adc.add_contact()
    elif usernum == 3:
        cngc.change_contact()
    elif usernum == 4:
        dec.delete_contact()
    elif usernum == 5:
        impd.import_dict()
    elif usernum == 6:
        expd.export_dict()
    else:
        print('Всего доброго) Возвращайтесь ещё.')
        exit()
