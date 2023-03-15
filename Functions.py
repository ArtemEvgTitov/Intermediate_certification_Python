import json
import Logger as log
from datetime import datetime

import main

BASE_FILE = 'notes.json'
notes = []

def save():
    with open(BASE_FILE, "w", encoding="utf-8") as note:
        note.write(json.dumps(notes, ensure_ascii=False))
    print(f'Заметка успешно сохранена в файле {BASE_FILE}')
    log.text_in_log(f'Заметка успешно сохранена в файле {BASE_FILE}')

def load():
    try:
        global notes
        with open(BASE_FILE, "r", encoding="utf-8") as data:
            notes = json.load(data)
        log.text_in_log('База успешно загружена')
    except:
        log.text_in_log('Ошибка загрузки базы. Вероятно, отсуствует файл')

def print_all():
    load()
    result = ''
    count = 0
    for i in notes:
        count += 1
        for key, value in i.items():
            result += str(key) + ': ' + str(value) + '\n'
        result += '\n'
    log.text_in_log('Вывод всех заметок в терминал')
    print('\n' + f'Всего заметок в базе: {count}' + '\n\n' + result)

def add_note(heading, text):
    try:
        load()
        id = selection_id()
        data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes.append({"ID": id, "Дата создания": data_time, "Дата изменения": data_time, "Заголовок": heading, "Заметка": text)
        log.text_in_log(f'В базу добавлена заметка: \nID:{id}\nЗаголовок: {heading}\nТекст: {text}')
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
    log.text_in_log(f'Осуществлён подбор ID для новой заметки. ID:{id}')
    return id

def search_note(text):
    load()
    result = ''
    search_id = 0
    if text == '1':
        id = input('Введите ID заметки: ')
        log.text_in_log(f'Пользователь искал ID: "{id}"')
        for i in notes:
            if int(id) == i["ID"]:
                search_id = int(i["ID"])
                for key, value in i.items():
                    result += str(key) + ': ' + str(value) + '\n'
                log.text_in_log(f'Произведён поиск по ID. Результат поиска:\n{result}')
    elif text == '2':
        heading = input('Введите текст заголовка: ')
        log.text_in_log(f'Пользователь искал заголовок: "{heading}"')
        for i in notes:
            if heading.lower() in (i["Заголовок"]).lower():
                search_id = int(i["ID"])
                for key, value in i.items():
                    result += str(key) + ': ' + str(value) + '\n'
                log.text_in_log(f'Произведён поиск по заголовку. Результат поиска:\n{result}')
    elif text == '3':
        note = input('Введите текст заметки: ')
        log.text_in_log(f'Пользователь искал текст заметки: "{note}"')
        for i in notes:
            if note.lower() in (i["Заметка"]).lower():
                search_id = int(i["ID"])
                for key, value in i.items():
                    result += str(key) + ': ' + str(value) + '\n'
                log.text_in_log(f'Произведён поиск по ID. Результат поиска:\n{result}')
    else:
        print('Некорректный ввод. Программа будет перезапущена')
        log.text_in_log(f'Некорректный ввод в меню поиска. Пользователь ввёл "{text}"')
        main.start()
    return result, search_id

def options_for_note(text, id, message_level4):
    load()
    if text == '1':
        edit_note(id, input(message_level4))
    elif text == '2':
        delete_note(id)

def edit_note(id, text):
    load()
    temp = []
    for i in notes:
        if int(id) == i['ID']:
            temp.append(i)
    if text == '1':
        heading = input('Введите новый заголовок: ')
        temp["Заголовок"] = heading
    elif text == '2':
        body = input('Введите новый текст заметки')
        temp["Заметка"] = body
    data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp["Дата изменения"] = data_time

def add_edit_note(id):
    delete_note(id)

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
