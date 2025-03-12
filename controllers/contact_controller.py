from models.contact import Contact
from utils.validators import Validator

class ContactController:
    def __init__(self, view, contact_repository):
        self.view = view
        self.repository = contact_repository
        self.validator = Validator()

    def add_contact(self):
        try:
            contact_data = self.view.get_contact_data()
            cpf = self.validator.validate_cpf(contact_data['cpf'])
            if cpf in self.repository.contacts:
                self.view.show_message('ERROR: A contact with this CPF already exists.')
                return
            
            name = contact_data['name']
            if not name.strip():
                raise ValueError('Name cannot be empty.')
            
            phone = self.validator.validate_phone(contact_data['phone'])
            email = self.validator.validate_email(contact_data['email'])

            contact = Contact(cpf, name, phone, email)
            self.repository.add(contact)
            self.view.show_message(f'Contact added successfully! CPF: {cpf}')

        except ValueError as e:
            self.view.show_message(f'ERROR: {str(e)}')

    def list_contacts(self):
        contacts = self.repository.get_all()
        self.view.show_contacts(contacts)

    def search_contact(self):
        cpf = self.view.get_cpf()
        contact = self.repository.get(cpf)
        if contact:
            self.view.show_contact(contact)
        else:
            self.view.show_message('ERROR: Contact not found.')
        return contact
    
    def remove_contact(self):
        cpf = self.view.get_cpf()
        if self.repository.remove(cpf):
            self.view.show_message('Contact removed successfully.')
        else:
            self.view.show_message('ERROR: Contact not found.')

    def update_contact(self):
        try: 
            cpf = self.view.get_cpf()
            contact = self.repository.get(cpf)
            
            if not contact:
                self.view.show_message('ERROR: Contact not found.')
                return
            
            update_data = self.view.get_update_info(contact)
            name = update_data['name']
            if name and not name.strip():
                raise ValueError('Name cannot be empty.')
            
            phone = update_data['phone']
            if phone:
                phone = self.validator.validate_phone(phone)

            email = update_data['email']
            if email:
                email = self.validator.validate_email(email)

            if contact.update(
                name or contact.name,
                phone or contact.phone,
                email or contact.email
            ):
                self.view.show_message('Contact updated successfully!')
        
        except ValueError as e:
            self.view.show_message(f'Error: {str(e)}')

            
