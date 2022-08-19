import json

def import():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        book = data.read()


