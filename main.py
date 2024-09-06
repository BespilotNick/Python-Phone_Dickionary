
import time
import interface

def greetings():
    print('Приветствую Вас! Уважаемый пользователь, это телефонный справочник, благодарим Вас за использование нашего'
          ' продукта.\nДалее мы познакомим Вас с возможностями этого справочника.\n')

greetings()

time.sleep(2)

interface.main_menu()