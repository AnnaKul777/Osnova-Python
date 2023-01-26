import view
import model

def start():
    user_choise = 0
    while user_choise != 8:
        user_choice = view.main_menu()

        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                choose_name = view.change_contact_once()
                choose_phone = view.change_contact_second()
                result = view.change_contact_success()
                result_once = view.change_contact_new(result)
                model.change_contact_one(choose_name, choose_phone, result, result_once)
                view.save_success()
            case 6:
                name = view.delete_contact()
                model.del_contact(name)
                view.del_success()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
