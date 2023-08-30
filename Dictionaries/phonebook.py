phonebook = dict()

contact_info = input()

while not contact_info.isdigit():
    name, phone_number = contact_info.split('-')
    phonebook[name] = phone_number

    contact_info = input()

for i in range(int(contact_info)):
    name = input()
    if name in phonebook.keys():
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')