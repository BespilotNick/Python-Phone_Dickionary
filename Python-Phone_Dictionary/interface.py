import Show_dict as shd
import Add_contact as adc
import Change_contact as cngc
import Delete_contact as dec
import Export_dict as expd
import Import_dict as impd

def choose_operation():
    print('Вы находитесь в основном меню, ниже приведены возможные варианты действий:')
    print('1 - Посмотреть телефонную книгу.')
    print('2 - Добавить контакт.')
    print('3 - Редактировать контакт.')
    print('4 - Удалить контакт.')
    print('5 - Импортировать данные из телефонного справочника.')
    print('6 - Экспортировать данные в телефонный справочник.')
    print('7 - Выход.\n')

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
