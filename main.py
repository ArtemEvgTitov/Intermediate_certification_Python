import Functions as func
import Logger as log

message_hi = '\nПрограмма запущена\n '
message_bay = '\nПрограмма выключена'

message_level1 = 'Вот какие действия Вам доступны:\n' \
                '1 - Показать все заметки\n' \
                '2 - Новая заметка\n' \
                '3 - Найти заметку\n' \
                '4 - Выход\n' \
                'введите цифру с необходимым действием: '

message_level2 = 'По какому параметру произвести поиск:\n' \
                '1 - По ID\n' \
                '2 - По заголовку\n' \
                '3 - По тексту заметки\n' \
                'введите цифру с необходимым действием: '

message_level3 = 'Вот какие действия Вам доступны:\n' \
                '1 - Редактировать заметку\n' \
                '2 - Удалить заметку\n' \
                '3 - Назад\n' \
                'введите цифру с необходимым действием: '

def start():
    print(message_hi)
    answer = input(message_level1)
    if answer == '1':
        log.text_in_log("Пользователь запросил вывод всех заметок в терминал")
        func.print_all()
        start()
    elif answer == "2":
        log.text_in_log("Пользователь запросил создание заметки")
        heading = input("Введите заголовок для заметки: ")
        text = input("Введите текст заметки: ")
        func.add_note(heading, text)
        start()
    elif answer == '3':
        log.text_in_log("Пользователь запросил поиск заметки")
        func.search_note(input(message_level2))
        start()
    elif answer == '4':
        log.text_in_log("Пользователь запросил выключение программы")
        print(message_bay)
        func.stop_programm()
    else:
        print("Некорректный ввод. Программа будет перезапущена")
        log.text_in_log("Некорректный ввод в основном меню программы")
        start()


