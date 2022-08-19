import json

def export_to_txt(text):
    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write('')
        for row in text:
            data.write(str(row) + '\n')


def export_to_json():
    with open('Phonebook.txt', 'w', encoding='utf-8') as t_book:
        t_book.read()

    with open('Phonebook.json', 'w') as j_book:
        json.dump(t_book, j_book)
