import json

def export_to_txt(data):
    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write('')
        for row in data:
            data.write(str(row) + '\n')


def expor_to_json():
    pass