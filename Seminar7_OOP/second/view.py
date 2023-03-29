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
        print(f'\t {i+1}.{commands[i]}')
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
    print('Телефонная книга телефонная книга сохранена (контакт(ы) добален(ы)/изменены)')

def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def new_contact_change1():
    line = input ('Укажите какую информацию вы хотите изменить, где 1 - это ФИО, 2 - это номер телефона, 3 - это комментарий ')
    if 0 >= int(line) > 3:
        print('Некорректный ввод. Введено больше Введите заново простое число от 1 до 3')
        return new_contact_change1()
    try:
        line = int(line)
        return line
    except:
        print('Некорректный ввод. Введите заново простое число от 1 до 3')
        return new_contact_change1()



def delete_contact():
    line = input ('Укажите какую информацию вы хотите удалить, где 1 - это ФИО, 2 - это номер телефона, 3 - это комментарий, 4 - это весь конакт полностью:  ')
    if 1 > int(line) > 4:
        print('Некорректный ввод. Введено больше Введите заново простое число от 1 до 4')
        return delete_contact()
    try:
        line = int(line)
        return line
    except:
        print('Некорректный ввод. Введите заново простое число от 1 до 4')
        return delete_contact()





def seek1():
    name = input('Для поиска: введите имя и фамилию контакта, в отношении которого необходимо произвести изменения: ')
    return name

def seek2():
    phone = input('Для уточнения поиска: введите номер телефона контакта, в отношении которого необходимо произвести изменения: ')
    return phone


def new_contact_change2(line):
    if line == 1:
        name = input('Введите имя и фамилию контакта: ')
        return name
    if line == 2:
        phone = input('Введите номер телефона: ')
        return phone
    if line == 3:
        comment = input('Введите комментарий: ')
        return comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def save_success_change():
    print('Изменения внесеты и добавлены в телефонную книгу')