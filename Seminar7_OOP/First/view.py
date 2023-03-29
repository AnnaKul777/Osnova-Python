def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']

    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t {i + 1}.{commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input


def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            if len(item) == 3:
                print(f'{item[0]} {item[1]} ({item[2]})')
            if len(item) == 2:
                print(f'{item[0]} {item[1]}')
            if len(item) == 1:
                print(f'{item[0]}')
    else:
        print('Телефонная книга пуста или не загруженна')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Внесены изменения.')

def del_success():
    print('Контакт удален.')


def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def change_contact_once():
    name = input('Введите имя и фамилию контакта: ')
    return name

def change_contact_second():
    phone = input('Введите номер телефона: ')
    return phone

def change_contact_success():
    element_contact = input('Введите данные которые вы хотите изменить, где 1. ФИО, 2. Номер телефона, 3. Коментарии: ')
    if 1 > int(element_contact) > 3:
        print('Некорректный ввод. Введено больше. Введите заново простое число от 1 до 3')
        return change_contact_success()
    try:
        element_contact = int(element_contact)
        return element_contact
    except:
        print('Некорректный ввод. Введите заново простое число от 1 до 3')
        return change_contact_success()

def change_contact_new(num):
    if num == 1:
        name = input('Введите имя и фамилию контакта: ')
        return name
    if num == 2:
        phone = input('Введите номер телефона: ')
        return phone
    if num == 3:
        comment = input('Введите комментарий: ')
        return comment

def delete_contact():
    name = input('Введите имя и фамилию контакта: ')
    return name


def find_contact():
    search = input('Введите искомое значение: ')
    return