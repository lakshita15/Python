import json

# Initialize the dictionary outside the loop to keep contacts across multiple operations
contact_dictionary = {}

# Load contacts from file at the start
try:
    with open('contacts.json', 'r') as file:
        contact_dictionary = json.load(file)
    print("Contacts loaded from 'contacts.json'")
except FileNotFoundError:
    print("No file named 'contacts.json' found. Starting with an empty contact list.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Search Contact by Name")
    print("6. Save Contacts to File")
    print("7. Load Contacts from File")
    print("8. Sort Contacts by Name")
    print("9. Search Contact by Email")
    print("10. Export Contacts to File")
    print("11. Exit")
    
    operation = input("Enter your choice (1-11): ")
    
    if operation == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact_dictionary[name] = {'phone': phone, 'email': email}
        print(f"Contact '{name}' added successfully.")
        
    elif operation == '2':
        print("\nContacts List:")
        #Loop through both keys and values, by using the items() method:
        for name, info in contact_dictionary.items(): 

            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
            
    elif operation == '3':
        name = input("Enter contact name to delete: ")
        if name in contact_dictionary:
            del contact_dictionary[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")
            
    elif operation == '4':
        name = input("Enter the contact name to update: ")
        if name in contact_dictionary:
            update_choice = input("What do you want to update? (1. Phone Number, 2. Contact Name, 3. Email): ")
            if update_choice == '1':
                new_phone = input(f"Enter new phone number for '{name}': ")
                contact_dictionary[name]['phone'] = new_phone
                print(f"Phone number for contact '{name}' updated successfully.")
            elif update_choice == '2':
                new_name = input(f"Enter new name for the contact: ")
                contact_dictionary[new_name] = contact_dictionary.pop(name)
                print(f"Contact name updated from '{name}' to '{new_name}'.")
            elif update_choice == '3':
                new_email = input(f"Enter new email for '{name}': ")
                contact_dictionary[name]['email'] = new_email
                print(f"Email for contact '{name}' updated successfully.")
            else:
                print("Invalid choice. Please try again.")
        else:
            print(f"Contact '{name}' not found.")
            
    elif operation == '5':
        name = input("Enter contact name to search: ")
        if name in contact_dictionary:
            info = contact_dictionary[name]
            print(f"Contact found: Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print(f"Contact '{name}' not found.")
            
    elif operation == '6':
        with open('contacts.json', 'w') as file:
            json.dump(contact_dictionary, file)
        print("Contacts saved to 'contacts.json'")
        
    elif operation == '7':
        try:
            with open('contacts.json', 'r') as file:
                contact_dictionary = json.load(file)
            print("Contacts loaded from 'contacts.json'")
        except FileNotFoundError:
            print("No file named 'contacts.json' found.")
        
    elif operation == '8':
        #created a copy of that list
        sorted_contacts = dict(sorted(contact_dictionary.items()))
        print("\nSorted Contacts List:")
        #Loop through both keys and values, by using the items() method:
        for name, info in sorted_contacts.items():
            print(f"Name: {name}, Phone: {info.get('phone')}, Email: {info.get('email')}")
        
    elif operation == '9':
        email = input("Enter email to search: ")
        found = False
        for name, info in contact_dictionary.items(): #search in values of the keys
            if info.get('email') == email:
                print(f"Contact found: Name: {name}, Phone: {info.get('phone')}, Email: {info.get('email')}")
                found = True
                break
        if not found:
            print(f"No contact found with email {email}")
        
    elif operation == '10':
        with open('exported_contacts.txt', 'w') as file:
            for name, info in contact_dictionary.items():
                file.write(f"Name: {name}, Phone: {info.get('phone')}, Email: {info.get('email')}\n")
        print("Contacts exported to 'exported_contacts.txt'")
        
    elif operation == '11':
        with open('contacts.json', 'w') as file:
            json.dump(contact_dictionary, file)
        print("Contacts saved to 'contacts.json'. Exiting Contact Management System.")
        break
        
    else:
        print("Invalid choice. Please try again.")
