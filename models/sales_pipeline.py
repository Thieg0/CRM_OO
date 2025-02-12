from models.sales_opportunity import SalesOpportunity

class SalesPipeline:
    def __init__(self, contact_manager):
        self.opportunities = {}
        self.contact_manager = contact_manager

    def add_opportunity(self):
        contact = self.contact_manager.search_contact()

        if not contact:
            print('Contact not found. Add the contact first.')
            return
        
        id = len(self.opportunities) + 1
        value = float(input('Enter the value of the deal (R$): '))
        stage = input('Enter the stage of the deal (Prospection, Negotiation, Closed): ')

        opportunity = SalesOpportunity(id, contact, value, stage)
        self.opportunities[id] = opportunity
        print(f'Opportunity added successfully! ID: {id}')

        def list_opportunities(self):
            if not self.opportunities:
                print('No opportunities found.')
                return

            for opportunity in self.opportunities.values():
                print(opportunity)

        def update_opportunity_stage(self):
            id = int(input('Enter the ID of the opportunity: '))
            if id in self.opportunities:
                new_stage = input('Enter the new stage of the deal (Prospection, Negotiation, Closed): ')
                self.opportunities[id].update_stage(stage)
                print('Opportunity updated successfully!')
            else:
                print('Opportunity not found.')

        def remove_opportunity(self):
            id = int(input('Enter the ID of the opportunity: '))
            if id in self.opportunities:
                del self.opportunities[id]
                print('Opportunity removed successfully!')
            else:
                print('Opportunity not found.')

