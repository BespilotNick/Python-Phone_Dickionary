
import phone_dict_module as pdm


def main_menu():
    """
    Основное меню программы. Позволяет пользователю выбрать действие, которое нужно выполнить.
    После выполнения любого действия, возвращает пользователя в главное меню.
    """
    while True:  # Определяем цикл для возврата в меню
        print('Вы находитесь в основном меню, ниже приведены возможные варианты действий:')
        print('1 - Посмотреть телефонную книгу.')
        print('2 - Добавить контакт.')
        print('3 - Редактировать контакт.')
        print('4 - Удалить контакт.')
        print('5 - Импортировать данные.')
        print('6 - Экспортировать данные.')
        print('7 - Выход.\n')

        usernum = input('Выберите действие или введите "m" для возврата в меню: ')
        if usernum == 'm':
            continue

        actions = '1234567'
        if usernum not in actions:
            print('Введено некорректное значение, попробуйте снова.')
            continue

        if usernum == '1':
            pdm.show_dict()
        elif usernum == '2':
            pdm.add_contact()
        elif usernum == '3':
            pdm.change_contact()
        elif usernum == '4':
            pdm.delete_contact()
        elif usernum == '5':
            pdm.import_dict()
        elif usernum == '6':
            pdm.export_dict()
        else:
            print('Всего доброго) Возвращайтесь ещё.')
            break    # Выход из цикла завершает работу программы
