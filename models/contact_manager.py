from models.contact import Contact
from models.validators import Validator

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.validator = Validator()
        
    def add_contact(self):
        try:
            cpf = input('Enter the CPF: ')
            cpf = self.validator.validate_cpf(cpf)
            
            if cpf in self.contacts:
                print('Error: A contact with this CPF already exists.')
                return

            name = input('Enter the name: ')
            if not name.split():
                raise ValueError('Name cannot be empty.')
            
            phone = input('Enter the phone: ')
            phone = self.validator.validate_phone(phone)
            
            email = input('Enter the email: ')
            email = self.validator.validate_email(email)
        
            contact = Contact(cpf, name, phone, email)
            self.contacts[cpf] = contact
            print(f'Contact added successfully! CPF: {cpf}')

        except ValueError as e:
            print(f'Error: {str(e)}')

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
        try: 
            cpf = input('Enter the CPF: ')
            contact = self.contacts.get(cpf)
            if contact:
                print('Leave the field blank if you do not want to update it.')
                
                name = input(f'Current name ({contact.name}): ') 
                if name and not name.strip():
                    raise ValueError('Name cannot be empty.')
                
                phone = input(f'Current phone ({contact.phone}): ') 
                if phone:
                    phone = self.validator.validate_phone(phone)
                    
                email = input(f'Current email ({contact.email}): ') 
                if email:
                    email = self.validator.validate_email(email)

                contact.update_contact(
                    name or contact.name,
                    phone or contact.phone,
                    email or contact.email
                )
            else:
                print('Contact not found.')

        except ValueError as e:
            print(f'Error: {str(e)}')