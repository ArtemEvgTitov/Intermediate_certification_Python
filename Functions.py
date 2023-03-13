import json
from datetime import datetime

BASE_FILE = 'notes.json'
notes = []

def save():
    with open(BASE_FILE, "w", encoding="utf-8") as note:
        note.write(json.dumps(notes, ensure_ascii=False))
    print(f"Заметка успешно сохранена в файле {BASE_FILE}")

def load():
    try:
        global notes
        with open(BASE_FILE, "r", encoding="utf-8") as data:
            notes = json.load(data)
    except:
        pass

def print_all():
    load()
    print(show_notes(notes))

def show_notes(notes):
    result = ''
    for i in notes:
        for key, value in i.items():
            result += str(key) + ': ' + str(value) + '\n'
        result += '\n'
    return result

def add_note(heading, text):
    load()
    id = search_id()
    data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"ID": id, "Дата создания": data_time, "Заголовок": heading, "Заметка": text})
    save()

def search_id():
    load()
    id = 0
    temp = []
    ID = False
    for i in notes:
        temp.append(i["ID"])
    while ID == False:
        if id in temp:
            id += 1
        else:
            ID = True
    return id

def search_note(text):
    load()
    if text == '1':
        id = input('Введите ID заметки: ')
        for i in notes:
            if int(id) == i["ID"]:
                result = ''
                for key, value in i.items():
                    result += str(key) + ': ' + str(value) + '\n'
                print(result)
    elif text == '2':
        heading = input('Введите текст заголовка: ')
        pass
    elif text == '3':
        pass

def stop_programm():
    pass
