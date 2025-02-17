from datetime import datetime
from models.lead import Lead

class LeadManager:
    def __init__(self):
        self.leads = {}
        self.current_id = 1

    def add_lead(self):
        try:
            print("\n=== Add New Lead ===")
            name = input("Enter lead name: ")
            email = input("Enter lead email: ")
            phone = input("Enter lead phone: ")
            
            print("\nSelect lead source:")
            print("1 - Website")
            print("2 - Social Media")
            print("3 - Referral")
            print("4 - Other")
            source_option = input("Enter option: ")
            
            sources = {
                "1": "Website",
                "2": "Social Media",
                "3": "Referral",
                "4": "Other"
            }
            
            source = sources.get(source_option, "Other")
            
            lead = Lead(name, email, phone, source)
            lead.id = self.current_id
            self.leads[self.current_id] = lead
            self.current_id += 1
            
            print(f"\nLead added successfully! ID: {lead.id}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")

    def list_leads(self):
        if not self.leads:
            print("No leads found.")
            return
            
        for lead in self.leads.values():
            print("\n" + "-"*50)
            print(lead)
            if lead.last_interaction:
                print(f"Last interaction: {lead.last_interaction.strftime('%d/%m/%Y %H:%M')}")

    def update_lead_status(self):
        lead_id = int(input("Enter lead ID: "))
        lead = self.leads.get(lead_id)
        
        if not lead:
            print("Lead not found.")
            return
            
        print("\nCurrent status:", lead.status)
        print("\nSelect new status:")
        print("1 - New")
        print("2 - Qualified")
        print("3 - Negotiating")
        print("4 - Converted")
        print("5 - Lost")
        
        status_map = {
            "1": "New",
            "2": "Qualified",
            "3": "Negotiating",
            "4": "Converted",
            "5": "Lost"
        }
        
        option = input("Enter option: ")
        new_status = status_map.get(option)
        
        if new_status and lead.update_status(new_status):
            print("Status updated successfully!")
        else:
            print("Invalid status.")

    def add_lead_note(self):
        lead_id = int(input("Enter lead ID: "))
        lead = self.leads.get(lead_id)
        
        if not lead:
            print("Lead not found.")
            return
            
        note = input("Enter note: ")
        lead.add_note(note)
        print("Note added successfully!")

    def view_lead_details(self):
        lead_id = int(input("Enter lead ID: "))
        lead = self.leads.get(lead_id)
        
        if not lead:
            print("Lead not found.")
            return
            
        print("\n=== Lead Details ===")
        print(f"ID: {lead.id}")
        print(f"Name: {lead.name}")
        print(f"Email: {lead.email}")
        print(f"Phone: {lead.phone}")
        print(f"Source: {lead.source}")
        print(f"Status: {lead.status}")
        print(f"Score: {lead.score}")
        print(f"Created: {lead.created_at.strftime('%d/%m/%Y %H:%M')}")
        
        if lead.notes:
            print("\nNotes:")
            for note in lead.notes:
                print(f"[{note['timestamp'].strftime('%d/%m/%Y %H:%M')}] {note['content']}")