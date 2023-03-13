import json
from datetime import datetime

BASE_FILE = 'notes.json'
notes = []

def save():
    with open(BASE_FILE, "w", encoding="utf-8") as note:
        note.write(json.dumps(notes, ensure_ascii=False))
    print(f"Заметка успешно сохранена в файле {BASE_FILE}")

def load():
    global notes
    with open(BASE_FILE, "r", encoding="utf-8") as data:
        notes = json.load(data)

def add_note(text):
    load()
    data_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"data_time": data_time, "note": text})
    save()