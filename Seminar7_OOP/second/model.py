class Database:
    phone_book = []
    path = ''


    def __init__(self, parth: str='phone_book.txt'):
        self.path = parth

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                if not line.isspace():
                    self.phone_book.append(line.strip().split(';'))


    def get(self):
        return self.phone_book


    def update(self, contact:list):
        self.phone_book.append(contact)


    def search(self, search:str):
        search_results = []
        for line in self.phone_book:
            for field in line:
                if search in field:
                    search_results.append(line)
                    break
        return search_results


    def save(self):
        data = []
        for line in self.phone_book:
            data.append(';'.join(line))
        with open(self.path, 'w', encoding='UTF-8') as file:
            data = file.write('\n'.join(data))

    def change(self, choise_name: str, choise_phone: str, number: int, choise2: str):
        for line in self.phone_book:
            for field in line:
                if (choise_name and choise_phone) in line:
                    line[number-1] = choise2
                    break
        return self.phone_book

    def del_contact (self, choise_name: str, choise_phone: str, number: int):
        for line in self.phone_book:
            for field in line:
                if (choise_name and choise_phone) in line:
                    if number == 4:
                        for del_all in range(len(line)):
                            line.pop(0)
                    else:
                        line.pop(number-1)
                    break

        return self.phone_book


db_phone = Database()