import json
import os

CONTACT_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts):
        print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    if not results:
        print("No matching contacts found.")
        return
    for idx, contact in enumerate(results):
        print(f"{idx + 1}. {contact['name']} - {contact['phone']}")

def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("Enter new details or press Enter to keep the current value:")
            contacts[index]['name'] = input(f"Name ({contacts[index]['name']}): ") or contacts[index]['name']
            contacts[index]['phone'] = input(f"Phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
            contacts[index]['email'] = input(f"Email ({contacts[index]['email']}): ") or contacts[index]['email']
            contacts[index]['address'] = input(f"Address ({contacts[index]['address']}): ") or contacts[index]['address']
            save_contacts(contacts)
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
