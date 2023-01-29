# '1.Какой класс? открываем конкретный файл',
# '2. Какой предмет?',
# '3. Показывает весь список учеников и их оценки по предмету',
# '4. Вызвать к доске? если ввести exit то выходит из программы',
# '5. На какую оценку ответ?',
# '6. После выхода сохранить все изменения в текущий файл'


def input_class():
    return input('С каким классом работаем?: ').upper()


def input_subject():
    return input('Какой предмет?: ').lower()


def who_answer():
    return input('Кто будет отвечать?: ')


def what_mark():
    return input('На какую оценку ответил?:  ')


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def output_on_error():
    print('Ошибка. Введите информацию еще раз.')


