from models.appointment import Appointment
from datetime import datetime

class TaskScheduler:
    def __init__(self, contact_manager):
        self.appointments = []
        self.contact_manager = contact_manager

    def add_appointment(self):
        contact = self.contact_manager.search_contact()
        if not contact:
            print('Contact not found. Please add the contact first.')
            return
        
        title = input('Enter the title of the appointment: ')

        while True:
            try:
                date_str = input('Enter the date of the appointment (YYYY-MM-DD): ')
                time_str = input('Enter the time of the appointment (HH:MM): ')
                date_time = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
                if date_time < datetime.now():
                    print('The appointment must be scheduled for a future date.')
                    continue
                break
            except ValueError:
                print('Invalid date and time format. Please try again.')

        description = input('Enter a description for the appointment: ')

        appointment = Appointment(contact, title, date_time, description)
        self.appointments.append(appointment)
        print('Appointment scheduled successfully.')

    def list_appointments(self):
        if not self.appointments:
            print('No appointments found.')
            return
        
        # Order appointments by date 
        sorted_appointments = sorted(self.appointments, key=lambda x: x.date_time)
        for appointment in sorted_appointments:
            print(appointment)

    def update_appointment_status(self):
        self.list_appointments()
        if not self.appointments:
            return
        
        try:
            index = int(input('Enter the number of the appointment to update (1, 2, 3...): ')) - 1
            if 0 <= index < len(self.appointments):
                print('Available status: Scheduled, Completed, Canceled')
                new_status = input('Enter new status: ')
                if self.appointments[index].update_status(new_status):
                    print('Appointment status updated successfully.')
                else:
                    print('Invalid status.')

            else:
                print('Invalid appointment number.')
        except ValueError:
            print('Please enter a valid number.')

    def remove_appointment(self):
        self.list_appointments()
        if not self.appointments:
            return
        
        try:
            index = int(input('Enter the number of the appointment to remove (1, 2, 3...): ')) - 1
            if 0 <= index < len(self.appointments):
                removed = self.appointments.pop(index)
                print(f'Appointment "{removed.title}" removed successfully!')
            else:
                print('Invalid appointment number.')
        except ValueError:
            print('Please enter a valid number.')       

    def list_appointments_by_contact(self):
        contact = self.contact_manager.search_contact()
        if not contact:
            print('Contact not found. Please add the contact first.')
            return
        
        appointments = [apt for apt in self.appointments if apt.contact.cpf == contact.cpf]
        if not appointments:
            print('No appointments found for this contact.')
            return
        
        for appointment in sorted(appointments, key=lambda x: x.date_time):
            print(appointment)