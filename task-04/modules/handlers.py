def add_contact(args: list[str], contacts: dict[str]) -> str:
    """
    функція-хендлер, яка викликається за "add". Функція перевіряє наявність контакта в словнику.  
    Якщо контакт є у словнику запитає чи хоче користувач замінити існуючий контакт.
    Якщо так викликає change_contact. Якщо ні завершує своє виконання
    Функція вертає строку повідомлення.
    В якості параметрів передаються: список з імьям та словник.
    """    
    try:
        name, phone = args
    except ValueError:
        return 'Contact added failed. Please enter contact name and phone number. Format command [username] [phone]'
    if name in contacts:
        return "Failed added contact. To replace the contact, use change [username] [phone] or enter another name"
    else:
        contacts[name] = phone
        return "Contact added."


def change_contact(args: list[str], contacts: dict[str]) -> str:
    """
    функція-хендлер, яка викликається за "change". Функція заміняє контакт, якщо він є у словнику та вертає строку повідомлення 
    В якості параметрів передаються: список з імьям та словник.
    """
    try:
        name, phone = args
    except ValueError:
        return 'Contact changed failed. Please enter contact name and phone number. Format command [username] [phone]'
    if name in contacts:
        contacts[name] = phone
        return "Changed contacts."
    else:
        return "There is no such contact in your contacts."
    

def show_phone(args: list[str], contacts: dict[str]) -> str:
    """
    функція-хендлер, яка викликається за "phone username" та вертає номер телефону для зазначеного контакту username
    В якості параметрів передаються: список з імьям та словник.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "There is no such contact in your contacts."