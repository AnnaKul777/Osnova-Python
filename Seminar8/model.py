import os.path

journal = {}
subject = ''
path = ''


def set_class(class_path:str):
    global path
    path = 'Classes/' + class_path + '.txt'
    control = os.path.exists(path)
    if control == True:
        return path
    else:
        print('Такого класса не существует')
        return False

def set_subdject(our_subject: str, file):
    global subject
    for topic in file:
        if our_subject in topic:
            subject = our_subject
            return True
            break

def open_file1():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    return file

def open_file2(file):
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))


def check_student(file, student):
    for nam in file:
        if student in nam:
            return True
            break


def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks


def get_jornal():
    return journal

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
        for sub in file:
            if sub.split(';')[0] != subject:
                new_file.append(sub.strip())
        item = []
        for student, marks in journal.items():
            item.append(student + ':' + ' '.join(list(map(str, marks))))
        item = subject + ';' + ', '.join(item)
        new_file.append(item)
        with open(path, 'w', encoding='UTF-8') as data:
            data.write('\n'.join(new_file))
