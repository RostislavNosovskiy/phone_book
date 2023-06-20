
phone_book = []
path = '/Users/rostislavnosovskij/Desktop/Les8/projekt/phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        uid, name, phone, comment = contact.strip().split(':')
        phone_book.append({'uid': uid, 'name': name, 'phone': phone, 'comment': comment})
        

def saved_file():
    with open('/Users/rostislavnosovskij/Desktop/Les8/projekt/phones.txt', 'w') as f:
        for contacts in range (len(phone_book)-1):
            uid = phone_book[contacts]['uid']
            name = phone_book[contacts]['name']
            phone = phone_book[contacts]['phone']
            comment = phone_book[contacts]['comment']
            f.write(f"{uid}:{name}:{phone}:{comment}\n ")
        uid = phone_book[len(phone_book)-1]['uid']
        name = phone_book[len(phone_book)-1]['name']
        phone = phone_book[len(phone_book)-1]['phone']
        comment = phone_book[len(phone_book)-1]['comment']
        f.write(f"{uid}:{name}:{phone}:{comment}")
        
    
  
def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('uid')) )
        
    if uid_list == []:
        return{'uid':'1'}
    else:
        return {'uid': str(max(uid_list)+1)}
    

        
        
def add_contact(new: dict):
    new1 = {}
    new1.update(check_id())
    new1.update(new)
    phone_book.append(new1)
    print(phone_book)
          
    
def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    print(result)
    return result

def change(index: int,new: dict[str, str]):
    for key,filed in new.items():
        if filed != '':
            phone_book[index-1][key] = filed
            
def delete(index) :
    for contacts in range(len(phone_book)):
        if phone_book[contacts]['uid'] == index:
            del phone_book[contacts]
            break
        
def delete_name(index) -> str:
    for contacts in range(len(phone_book)):
        name = phone_book[contacts-1]['name']
    return name
        
def delete_conf(str):
    while True:
            return(str)
    
        
    

        