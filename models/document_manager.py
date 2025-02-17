from .document import Document

class DocumentManager:
    def __init__(self):
        self.documents = {}
        self.current_id = 1
        self.categories = ["proposal", "contract", "marketing", "other"]

    def upload_document(self):
        try:
            print("\n=== Upload Document ===")
            name = input("Enter document name: ")
            
            print("\nSelect category:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i} - {category.title()}")
            category_index = int(input("Enter category number: ")) - 1
            
            if not (0 <= category_index < len(self.categories)):
                print("Invalid category.")
                return
            
            category = self.categories[category_index]
            
            print("\nDocument content (type 'END' on a new line when finished):")
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)
            content = '\n'.join(content_lines)
            
            related_to = input("\nRelated to (CPF/ID or leave empty): ").strip() or None
            
            document = Document(name, category, content, related_to)
            document.id = self.current_id
            self.documents[self.current_id] = document
            self.current_id += 1
            
            print(f"\nDocument uploaded successfully! ID: {document.id}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")

    def list_documents(self):
        if not self.documents:
            print("No documents found.")
            return

        for doc in self.documents.values():
            print("\n" + "-"*50)
            print(doc)

    def search_documents(self):
        print("\n=== Search Documents ===")
        print("1 - Search by name")
        print("2 - Search by category")
        print("3 - Search by related to")
        option = input("Enter option: ")

        if option == "1":
            name = input("Enter document name: ").lower()
            results = [doc for doc in self.documents.values() if name in doc.name.lower()]
        elif option == "2":
            category = input("Enter category: ").lower()
            results = [doc for doc in self.documents.values() if category == doc.category.lower()]
        elif option == "3":
            related_to = input("Enter CPF/ID: ")
            results = [doc for doc in self.documents.values() if related_to == doc.related_to]
        else:
            print("Invalid option.")
            return

        if not results:
            print("No documents found.")
            return

        for doc in results:
            print("\n" + "-"*50)
            print(doc)

    def view_document(self):
        try:
            doc_id = int(input("Enter document ID: "))
            document = self.documents.get(doc_id)
            
            if not document:
                print("Document not found.")
                return
                
            print("\n=== Document Details ===")
            print(f"ID: {document.id}")
            print(f"Name: {document.name}")
            print(f"Category: {document.category}")
            print(f"Version: {document.version}")
            print(f"Upload Date: {document.upload_date.strftime('%d/%m/%Y %H:%M')}")
            if document.related_to:
                print(f"Related to: {document.related_to}")
            print("\nContent:")
            print("-"*50)
            print(document.content)
        except ValueError:
            print("Please enter a valid document ID.")

    def update_document(self):
        try:
            doc_id = int(input("Enter document ID: "))
            document = self.documents.get(doc_id)
            
            if not document:
                print("Document not found.")
                return

            print("\nCurrent content:")
            print(document.content)
            
            print("\nNew content (type 'END' on a new line when finished):")
            content_lines = []
            while True:
                line = input()
                if line == 'END':
                    break
                content_lines.append(line)
            
            # Create new version
            new_doc = Document(
                document.name,
                document.category,
                '\n'.join(content_lines),
                document.related_to
            )
            new_doc.version = document.version + 1
            new_doc.id = self.current_id
            
            self.documents[self.current_id] = new_doc
            self.current_id += 1
            
            print(f"Document updated successfully! New version ID: {new_doc.id}")
        except ValueError:
            print("Please enter a valid document ID.")