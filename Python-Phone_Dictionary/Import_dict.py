import json

def import_data():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.read()


