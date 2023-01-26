phone_book = []
path = 'phone_book.txt'

def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))


def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact:list):
    global phone_book
    phone_book.append(contact)

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def change_contact_one(choose_name: str, choose_phone: str, number: int, choose_new: str):
    global phone_book
    for line in phone_book:
        for field in line:
            if (choose_name and choose_phone) in line:
                line[number - 1] = choose_new
                break
    return phone_book

def del_contact(name: str):
    global phone_book
    for line in phone_book:
        if name in line:
            phone_book.remove(line)
            break
    return phone_book

def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results

