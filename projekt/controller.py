from view import  menu, show_contacts, print_message, input_contact, input_return, input_delete_contact 
import model
from view import text


def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successeful) 
            case 2:
                show_contacts(model.phone_book)
                model.saved_file()
                print_message(text.save)
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index)-1].get('name')
                print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))
            case 7:
                index = input_return(text.delete_index)
                result = input_delete_contact(text.del_confirm)
                name = model.delete_name(index)
                if model.delete_conf(result) =='да':
                    model.delete(index)
                    print_message(text.contact_delete(name))
                
                
                
            case 8:
                break