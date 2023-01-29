import view
import model

def start():
    find_class = view.input_class()
    print(find_class)
    check = model.set_class(find_class)
    if check == False:
        return start()
    file = model.open_file1()
    test = model.set_subdject(view.input_subject(), file)
    while test != True:
        view.output_on_error()
        test = model.set_subdject(view.input_subject(), file)
    model.open_file2(file)
    student = ''
    while True:
        journal = model.get_jornal()
        view.list_of_child(journal)
        student = view.who_answer()
        num = model.check_student(file, student)
        while num != True:
            view.output_on_error()
            student = view.who_answer()
            num = model.check_student(file, student)
        if student == 'exit':
            break
        mark = int(view.what_mark())
        right_mark = [1, 2, 3, 4, 5]
        while mark not in right_mark:
            view.output_on_error()
            mark = int(view.what_mark())
        model.student_mark(student, mark)
    model.save_file()