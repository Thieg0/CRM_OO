from datetime import datetime
from models.dashboard import Dashboard
from models.dashboard_widget import DashboardWidget


class DashboardManager:
    def __init__(self, contact_manager, sales_pipeline, lead_manager, task_scheduler):
        self.dashboards = {}
        self.contact_manager = contact_manager
        self.sales_pipeline = sales_pipeline
        self.lead_manager = lead_manager
        self.task_scheduler = task_scheduler
        self._create_default_widgets()

    def _create_default_widgets(self):
        self.available_widgets = {
            "total_contacts": DashboardWidget(
                "Total Contacts",
                "counter",
                lambda: len(self.contact_manager.contacts)
            ),
            "active_opportunities": DashboardWidget(
                "Active Opportunities",
                "chart",
                self._get_opportunities_by_stage
            ),
            "recent_leads": DashboardWidget(
                "Recent Leads",
                "list",
                self._get_recent_leads
            ),
            "upcoming_appointments": DashboardWidget(
                "Upcoming Appointments",
                "list",
                self._get_upcoming_appointments
            )
        }

    def create_dashboard(self):
        name = input("Enter dashboard name: ")
        if name in self.dashboards:
            print("A dashboard with this name already exists.")
            return

        dashboard = Dashboard(name)
        self.dashboards[name] = dashboard
        print(f"Dashboard '{name}' created successfully!")

    def list_dashboards(self):
        if not self.dashboards:
            print("No dashboards found.")
            return

        for dashboard in self.dashboards.values():
            print("\n" + "-"*50)
            print(dashboard)
            if dashboard.widgets:
                print("Widgets:")
                for widget in dashboard.widgets:
                    print(f"  {widget.position}. {widget}")

    def customize_dashboard(self):
        name = input("Enter dashboard name: ")
        dashboard = self.dashboards.get(name)
        
        if not dashboard:
            print("Dashboard not found.")
            return

        while True:
            print("\n=== Customize Dashboard ===")
            print("1 - Add widget")
            print("2 - Remove widget")
            print("3 - View dashboard")
            print("0 - Return")
            option = input("Enter option: ")

            if option == "1":
                self._add_widget_to_dashboard(dashboard)
            elif option == "2":
                self._remove_widget_from_dashboard(dashboard)
            elif option == "3":
                self._view_dashboard(dashboard)
            elif option == "0":
                break

    def _add_widget_to_dashboard(self, dashboard):
        print("\nAvailable widgets:")
        for i, (key, widget) in enumerate(self.available_widgets.items(), 1):
            print(f"{i}. {widget}")

        try:
            widget_num = int(input("\nSelect widget number: "))
            if 1 <= widget_num <= len(self.available_widgets):
                widget = list(self.available_widgets.values())[widget_num - 1]
                dashboard.add_widget(widget)
                print("Widget added successfully!")
            else:
                print("Invalid widget number.")
        except ValueError:
            print("Please enter a valid number.")

    def _remove_widget_from_dashboard(self, dashboard):
        if not dashboard.widgets:
            print("No widgets to remove.")
            return

        print("\nCurrent widgets:")
        for widget in dashboard.widgets:
            print(f"{widget.position}. {widget}")

        try:
            position = int(input("\nEnter widget position to remove: "))
            dashboard.remove_widget(position)
            print("Widget removed successfully!")
        except ValueError:
            print("Please enter a valid number.")

    def _view_dashboard(self, dashboard):
        print(f"\n=== {dashboard.name} ===")
        for widget in dashboard.widgets:
            print("\n" + "-"*30)
            print(f"{widget.title}:")
            data = widget.update_data()
            
            if widget.widget_type == "counter":
                print(data)
            elif widget.widget_type == "list":
                for item in data:
                    print(f"- {item}")
            elif widget.widget_type == "chart":
                for label, value in data.items():
                    print(f"{label}: {value}")

    def _get_opportunities_by_stage(self):
        stages = {}
        for opp in self.sales_pipeline.opportunities.values():
            stages[opp.stage] = stages.get(opp.stage, 0) + 1
        return stages

    def _get_recent_leads(self):
        return [str(lead) for lead in list(self.lead_manager.leads.values())[-5:]]

    def _get_upcoming_appointments(self):
        appointments = sorted(
            [apt for apt in self.task_scheduler.appointments if apt.date_time > datetime.now()],
            key=lambda x: x.date_time
        )
        return [str(apt) for apt in appointments[:5]]