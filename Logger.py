from datetime import datetime as dt


def text_in_log(text):
    # Логирование
    path = 'log_notes.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {text}\n')
    f.close()
