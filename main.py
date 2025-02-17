from models import ContactManager, SalesPipeline, ActivityTracker, TaskScheduler, TemplateManager, CampaignManager, LeadManager, DashboardManager

def main():
    contact_manager = ContactManager()
    sales_pipeline = SalesPipeline(contact_manager)
    activity_tracker = ActivityTracker(contact_manager)
    task_scheduler = TaskScheduler(contact_manager)
    template_manager = TemplateManager()
    campaign_manager = CampaignManager(contact_manager, template_manager)
    lead_manager = LeadManager()
    dashboard_manager = DashboardManager(contact_manager, sales_pipeline, lead_manager, task_scheduler)

    while True:
        print('\n===== Menu =====')
        print('1 - Manage contacts:')
        print('2 - Manage sales pipeline:')
        print('3 - Manage activities:')
        print('4 - Manage appointments:')
        print('5 - Manage emails:')
        print('6 - Manage leads:')
        print('7 - Manage dashboard:')
        print('0 - Exit:')
        option = input('Enter the option: ')

        if option == '1':
            while True:
                print('\n===== Management of contacts =====')
                print('1 - Add contact:')
                print('2 - List contacts:')
                print('3 - Remove contact:')
                print('4 - Update contact:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    contact_manager.add_contact()
                elif sub_potion == '2':
                    contact_manager.list_contacts()
                elif sub_potion == '3':
                    contact_manager.remove_contact()
                elif sub_potion == '4':
                    contact_manager.update_contact()
                elif sub_potion == '0':
                    break
                else:
                    print('Invalid option.')
        
        elif option == '2':
            while True:
                print('\n===== Management of sales pipeline =====')
                print('1 - Add opportunity:')
                print('2 - List opportunities:')
                print('3 - Update opportunity stage:')
                print('4 - Remove opportunity:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    sales_pipeline.add_opportunity()
                elif sub_potion == '2':
                    sales_pipeline.list_opportunities()
                elif sub_potion == '3':
                    sales_pipeline.update_opportunity_stage()
                elif sub_potion == '4':
                    sales_pipeline.remove_opportunity()
                elif sub_potion == '0':
                    break
                else:
                    print('Invalid option.')

        elif option == '3':
            while True:
                print('\n===== Management of activities =====')
                print('1 - Add activity:')
                print('2 - List activities:')
                print('3 - Find activities by contact:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    activity_tracker.add_activity()
                elif sub_potion == '2':
                    activity_tracker.list_activities()
                elif sub_potion == '3':
                    activity_tracker.find_activities_by_contact()
                elif sub_potion == '0':
                    break
                else:
                    print('Invalid option.')

        elif option == '4':
            while True:
                print('\n===== Appointment management =====')
                print('1 - Add appointment:')
                print('2 - List appointments:')
                print('3 - Update appointment status:')
                print('4 - Remove appointment:')
                print('5 - List appointments by contact:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    task_scheduler.add_appointment()
                elif sub_potion == '2':
                    task_scheduler.list_appointments()
                elif sub_potion == '3':
                    task_scheduler.update_appointment_status()
                elif sub_potion == '4':
                    task_scheduler.remove_appointment()
                elif sub_potion == '5':
                    task_scheduler.list_appointments_by_contact()
                elif sub_potion == '0':
                    break
                else:
                    print('Invalid option.')

        elif option == '5':
            while True:
                print('\n===== Email campaign management =====')
                print('1 - Manage templates:')
                print('2 - Manage campaigns:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    while True:
                        print('\n===== Template management =====')
                        print('1 - Create template:')
                        print('2 - List templates:')
                        print('3 - Preview template:')
                        print('4 - Remove template:')
                        print('0 - Return:')
                        template_option = input('Enter the option: ')

                        if template_option == '1':
                            template_manager.create_template()
                        elif template_option == '2':
                            template_manager.list_templates()
                        elif template_option == '3':
                            template_manager.preview_template()
                        elif template_option == '4':
                            template_manager.remove_template()
                        elif template_option == '0':
                            break
                        else:
                            print('Invalid option.')

                elif sub_potion == '2':
                    while True:
                        print('\n===== Campaign management =====')
                        print('1 - Create campaign:')
                        print('2 - List campaigns:')
                        print('3 - Schedule campaign:')
                        print('4 - Cancel campaign:')
                        print('5 - View campaign statistics:')
                        print('0 - Return:')
                        campaign_option = input('Enter the option: ')

                        if campaign_option == '1':
                            campaign_manager.create_campaign()
                        elif campaign_option == '2':
                            campaign_manager.list_campaigns()
                        elif campaign_option == '3':
                            campaign_manager.schedule_campaign()
                        elif campaign_option == '4':
                            campaign_manager.cancel_campaign()
                        elif campaign_option == '5':
                            campaign_manager.view_campaign_stats()
                        elif campaign_option == '0':
                            break
                        else:
                            print('Invalid option.')

        elif option == '6':
            while True:
                print('\n===== Lead management =====')
                print('1 - Add lead:')
                print('2 - List lead:')
                print('3 - Update lead status:')
                print('4 - Add lead note:')
                print('5 - View lead details:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    lead_manager.add_lead()
                elif sub_potion == '2':
                    lead_manager.list_leads()
                elif sub_potion == '3':
                    lead_manager.update_lead_status()
                elif sub_potion == '4':
                    lead_manager.add_lead_note()
                elif sub_potion == '5':
                    lead_manager.view_lead_details()
                elif sub_potion == '0':
                    break
                else:
                    print('Invalid option')

        elif option == '7':
            while True:
                print('\n===== Dashboard management =====')
                print('1 - Create dashboard:')
                print('2 - List dashboards:')
                print('3 - Customize dashboard:')
                print('0 - Return:')
                sub_potion = input('Enter the option: ')

                if sub_potion == '1':
                    dashboard_manager.create_dashboard()
                elif sub_potion == '2':
                    dashboard_manager.list_dashboards()
                elif sub_potion == '3':
                    dashboard_manager.customize_dashboard()
                elif sub_potion == '0':
                    break
                else:
                    print('Invalid option')

        elif option == '0':
            print('Goodbye!')
            break
        else:
            print('Invalid option.')

if __name__ == '__main__':
    main()
                
