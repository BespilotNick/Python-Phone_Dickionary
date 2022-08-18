import interface
import time

def greetings():
    print('Приветствую Вас! Уважаемый пользователь, это телефонный справочник, благодарим Вас за использование нашего'
          ' продукта.\nДалее мы познакомим Вас с возможностями этого справочника.\n')

greetings()
time.sleep(3)
interface.choose_operation()