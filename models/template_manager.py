from models.email_template import EmailTemplate

class TemplateManager:
    def __init__(self):
        self.templates = {}

    def create_template(self):
        try:
            name = input('Enter template name: ')
            subject = input('Enter email subject: ')
            print('Enter email content (use {variable_name} for personalization):')
            print('Example: Hello {name}, welcome to {company}!')
            content = input('Content: ')

            template = EmailTemplate(name, subject, content)
            template.validate()
            
            self.templates[name] = template
            print(f'Template "{name}" created successfully!')
            print('Variables detected:', ', '.join(template.variables))
            
        except ValueError as e:
            print(f'Error: {str(e)}')

    def list_templates(self):
        if not self.templates:
            print('No templates found.')
            return

        for template in self.templates.values():
            print('\n' + '-'*50)
            print(template)

    def get_template(self, name):
        return self.templates.get(name)

    def preview_template(self):
        name = input('Enter template name: ')
        template = self.get_template(name)
        
        if not template:
            print('Template not found.')
            return

        print('\nTemplate variables:', ', '.join(template.variables))
        sample_data = {}
        for var in template.variables:
            value = input(f'Enter sample value for {var}: ')
            sample_data[var] = value

        print('\nPreview:')
        print('-'*50)
        print('Subject:', template.subject)
        print('Content:')
        print(template.preview(sample_data))
        print('-'*50)

    def remove_template(self):
        name = input('Enter template name: ')
        if name in self.templates:
            del self.templates[name]
            print(f'Template "{name}" removed successfully!')
        else:
            print('Template not found.')