from models.contact import Contact

class contactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        cpf = input('Enter the CPF: ')
        if cpf in self.contacts:
            print('Error: A contact with this CPF already exists.')
            return

        name = input('Enter the name: ')
        phone = input('Enter the phone: ')
        email = input('Enter the email: ')
        
        contact = Contact(cpf, name, phone, email)
        self.contacts[cpf] = contact
        print(f'Contact added successfully! CPF: {cpf}')

    def list_contacts(self):
        if not self.contacts:
            print('No contacts found.')
            return

        for contact in self.contacts.values():
            print(contact)

    def search_contact(self):
        cpf = input('Enter the CPF: ')
        return self.contacts.get(cpf)
        
    def remove_contact(self):
        cpf = input('Enter the CPF: ')
        if cpf in self.contacts:
            del self.contacts[cpf]
            print('Contact removed successfully!')
        else:
            print('Contact not found.')

    def update_contact(self):
        cpf = input('Enter the CPF: ')
        contact = self.contacts.get(cpf)
        if contact:
            print('Leave the field blank if you do not want to update it.')
            name = input(f'Current name ({contact.name}): ') or contact.name
            phone = input(f'Current phone ({contact.phone}): ') or contact.phone
            email = input(f'Current email ({contact.email}): ') or contact.email
            contact.update_contact(name, phone, email)
        else:
            print('Contact not found.')