import Show_dict as shd
import Add_contact as adc
import Change_contact as chc
import Delete_contact as dec
import Export_dict as expd
import Import_dict as impd

def choose_operation():
    print('Вы находитесь в основном меню, ниже приведены возможные варианты действий:'
          '1 - Посмотреть телефонную книгу.'
          '2 - Добавить контакт.'
          '3 - Редактировать контакт.'
          '4 - Удалить контакт.'
          '5 - Импортировать телефонный справочник.'
          '6 - Экспортировать телефонный справочник.'
          '7 - Выход.')
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
        chc.change_contact()
    elif usernum == 4:
        dec.delete_contact()
    elif usernum == 5:
        impd.import_dict()
    elif usernum == 6:
        expd.export_dict()
    else:
        exit()
