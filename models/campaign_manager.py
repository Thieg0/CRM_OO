from datetime import datetime
from models.email_campaign import EmailCampaign

class CampaignManager:
    def __init__(self, contact_manager, template_manager):
        self.campaigns = {}
        self.contact_manager = contact_manager
        self.template_manager = template_manager

    def create_campaign(self):
        try:
            # Get campaign name
            name = input('Enter campaign name: ')
            if name in self.campaigns:
                print('A campaign with this name already exists.')
                return
            
            # Select template
            self.template_manager.list_templates()
            template_name = input('\nEnter template name to use: ')
            template = self.template_manager.get_template(template_name)
            if not template:
                print('Template not found.')
                return

            # Select target contacts
            print('\nSelect target contacts:')
            self.contact_manager.list_contacts()
            target_contacts = []
            
            while True:
                cpf = input('\nEnter contact CPF (or leave empty to finish): ')
                if not cpf:
                    break
                    
                contact = self.contact_manager.search_contact()
                if contact:
                    target_contacts.append(contact)
                else:
                    print('Contact not found.')

            if not target_contacts:
                print('You must select at least one contact.')
                return

            # Create campaign
            campaign = EmailCampaign(name, template, target_contacts)
            self.campaigns[name] = campaign
            print(f'\nCampaign "{name}" created successfully!')

        except ValueError as e:
            print(f'Error: {str(e)}')

    def list_campaigns(self):
        if not self.campaigns:
            print('No campaigns found.')
            return

        for campaign in self.campaigns.values():
            print('\n' + '-'*50)
            print(campaign)

    def schedule_campaign(self):
        try:
            name = input('Enter campaign name: ')
            campaign = self.campaigns.get(name)
            
            if not campaign:
                print('Campaign not found.')
                return

            if campaign.status != "Draft":
                print('Only draft campaigns can be scheduled.')
                return

            while True:
                try:
                    date_str = input('Enter schedule date (YYYY-MM-DD): ')
                    time_str = input('Enter schedule time (HH:MM): ')
                    schedule_date = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
                    
                    if schedule_date <= datetime.now():
                        print('Schedule date must be in the future.')
                        continue
                    break
                except ValueError:
                    print('Invalid date/time format. Please try again.')

            campaign.schedule(schedule_date)
            print(f'Campaign "{name}" scheduled successfully for {date_str} {time_str}')

        except ValueError as e:
            print(f'Error: {str(e)}')

    def cancel_campaign(self):
        name = input('Enter campaign name: ')
        campaign = self.campaigns.get(name)
        
        if not campaign:
            print('Campaign not found.')
            return

        try:
            campaign.cancel()
            print(f'Campaign "{name}" cancelled successfully.')
        except ValueError as e:
            print(f'Error: {str(e)}')

    def view_campaign_stats(self):
        name = input('Enter campaign name: ')
        campaign = self.campaigns.get(name)
        
        if not campaign:
            print('Campaign not found.')
            return

        print('\nCampaign Statistics:')
        print('-'*50)
        print(f'Name: {campaign.name}')
        print(f'Status: {campaign.status}')
        print(f'Total recipients: {campaign.stats["total"]}')
        print(f'Sent: {campaign.stats["sent"]}')
        print(f'Opened: {campaign.stats["opened"]}')
        print(f'Clicked: {campaign.stats["clicked"]}')