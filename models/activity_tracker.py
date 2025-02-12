from models.activity import Activity

class ActivityTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self, cpf, activity_type, description):
        cpf = input('Enter the CPF of the contact: ')
        activity_type = input('Enter the type of activity (call, meeting, email): ')
        description = input('Enter the description of the activity: ')
        
        new_activity = Activity(cpf, activity_type, description)
        self.activities.append(new_activity)
        print('Activity added successfully.')

    def list_activities(self):
        if not self.activities:
            print('No activities registered.')
            return
        for activity in self.activities:
            print(activity)

    def find_activities_by_contact(self, cpf):
        cpf = input('Enter the CPF of the contact: ')
        activities = [act for act in self.activities if act.cpf == cpf]
        if not activities:
            print('No activities found for this contact.')
            return
        else:
            for activity in activities:
                print(activity)
    
