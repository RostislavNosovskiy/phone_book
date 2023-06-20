from .text import *

def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0< int(choice)<9:
            return int(choice)
        print(input_error)

def print_message(message:str):
    length =  len(message)
    print('\n' + '='*length)
    print(message)
    print('='*length + '\n')

def show_contacts (book: list[dict[str,str]]):
    if book:
        print('\n'+'='*67)
        for contact in book:
            uid = contact.get('uid')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{uid:>3}. {name:<20} {phone:<20} {comment:<20}')
        print('='*67+'\n')
    else:
        length = len(book_error)
        print('\n'+'='*length)
        print(book_error)
        print('='*length+'\n')
        
def input_contact(messege: str) -> dict[str,str]:
    print(messege)
    name = input(new_contact[0])
    phone = input(new_contact[1])
    comment = input(new_contact[2])
    return {'name': name, 'phone': phone, 'comment': comment}

def input_return(messege: str) -> str:
    return input(messege)

def input_delete_contact (messege: str) -> str:
    return input(messege)