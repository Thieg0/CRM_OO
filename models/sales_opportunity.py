class SalesOpportunity:
    def __init__(self, id, contact, value, stage):
        self.id = id
        self.contact = contact
        self.value = value
        self.stage = stage
    
    def update_stage(self, new_stage):
        self.stage = new_stage
        print(f'Stage updated to {new_stage}.')

    def __str__(self):
        return f'CPF: {self.id} | Contact: {self.contact} | Value: {self.value} | Stage: {self.stage}'