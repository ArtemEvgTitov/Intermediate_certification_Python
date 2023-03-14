import json
import Logger as log
from datetime import datetime

BASE_FILE = 'notes.json'
notes = []

def save():
    with open(BASE_FILE, "w", encoding="utf-8") as note:
        note.write(json.dumps(notes, ensure_ascii=False))
    print(f"Заметка успешно сохранена в файле {BASE_FILE}")
    log.text_in_log(f"Заметка успешно сохранена в файле {BASE_FILE}")

def load():
    try:
        global notes
        with open(BASE_FILE, "r", encoding="utf-8") as data:
            notes = json.load(data)
        log.text_in_log("База успешно загружена")
    except:
        log.text_in_log("Ошибка загрузки базы. Вероятно, отсуствует файл")

def print_all():
    load()
    result = ''
    for i in notes:
        for key, value in i.items():
            result += str(key) + ': ' + str(value) + '\n'
        result += '\n'
    log.text_in_log("Вывод всех заметок в терминал")
    print(result)

def add_note(heading, text):
    try:
        load()
        id = selection_id()
        data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes.append({"ID": id, "Дата создания": data_time, "Заголовок": heading, "Заметка": text})
        log.text_in_log(f"В базу добавлена заметка: \nID:{id}\nЗаголовок: {heading}\nТекст: {text}")
        save()
    except:
        pass


def selection_id():
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
                log.text_in_log(f"Произведён поиск по ID. Результат поиска:\n{result}")
                print(result)
                delete_note(id)
    elif text == '2':
        heading = input('Введите текст заголовка: ')
        pass
    elif text == '3':
        note = input('Введите текст заметки: ')
        pass

def delete_note(id):
    load()
    temp = []
    for i in notes:
        if int(id) != i['ID']:
            temp.append(i)
    with open(BASE_FILE, "w", encoding="utf-8") as note:
        note.write(json.dumps(temp, ensure_ascii=False))
    print(f"База перезаписана в файле {BASE_FILE}")
    log.text_in_log(f"База перезаписана в файле {BASE_FILE}")

def stop_programm():
    log.text_in_log("======== EXIT PROGRAMM ========")
