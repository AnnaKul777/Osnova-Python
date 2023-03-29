from model import db_phone as db
import view
import model

def start():
    user_choise = 0
    while user_choise != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = db.get()
                view.show_contacts(phone_book)
            case 2:
                db.open()
                view.load_success()
            case 3:
                db.save()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                db.update(new)
                view.save_success()
            case 5:
                choise_name = view.seek1()
                choise_phone = view.seek2()
                choise_number = view.new_contact_change1()
                choise2 = view.new_contact_change2(choise_number)
                db.change(choise_name, choise_phone, choise_number, choise2)
                view.save_success()
            case 6:
                choise_name = view.seek1()
                choise_phone = view.seek2()
                choise_number = view.delete_contact()
                db.del_contact(choise_name, choise_phone, choise_number)
                view.save_success()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)