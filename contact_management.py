# Initialize empty data structures
contacts = []
contacts_dict = {}
favorite_contacts = set()

# Main menu loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. List Contacts")
    print("4. Add to Favorites")
    print("5. List Favorite Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact = (name, phone, email)
        contacts.append(contact)
        contacts_dict[name] = {'Phone': phone, 'Email': email}
        print(f"Contact '{name}' added successfully!")

    elif choice == '2':
        search_name = input("Enter the name to search: ")
        if search_name in contacts_dict:
            print(f"Name: {search_name}")
            print(f"Phone: {contacts_dict[search_name]['Phone']}")
            print(f"Email: {contacts_dict[search_name]['Email']}")
        else:
            print(f"Contact '{search_name}' not found.")

    elif choice == '3':
         print("All Contacts:")
         for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")

    
    elif choice == '4':
        name = input("Enter the name to add to favorites: ")
        favorite_contacts.add(name)
        print(f"Contact '{name}' added to favorites!")

    elif choice == '5':
        print("\nFavorite Contacts:")
        for name in favorite_contacts:
            print(f"Name: {name}, Phone: {contacts_dict[name]['Phone']}, Email: {contacts_dict[name]['Email']}")

    elif choice == '6':
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


