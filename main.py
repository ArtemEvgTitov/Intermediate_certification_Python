import Functions as func

message_hi = 'Программа запущена\n '
message_bay = 'Программа выключена'

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
        func.print_all()
        start()
    elif answer == "2":
        heading = input("Введите заголовок для заметки: ")
        text = input("Введите текст заметки: ")
        func.add_note(heading, text)
        start()
    elif answer == '3':
        func.search_note(input(message_level2))
        start()
    elif answer == '4':
        func.stop_programm()
    else:
        print("Некорректный ввод")
        start()


