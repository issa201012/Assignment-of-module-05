import add_contact
import view_all_contact
import  remove_contact

all_contact = []

while True:
    print("Welcome to Contact Management System")
    print("1. Add Contact ")
    print("2. Remove Contact")
    print("3. View All Contacts")
    print("4. Exit")

    menu = input("Select any number: ")

    if menu == "4":
        print("Thanks for using Contact Management System ")
        break
    elif menu == "1":
        all_contact = add_contact.add_contact(all_contact)
    elif menu == "3":
        view_all_contact.view_all_contact(all_contact)
    elif menu == "2":
        all_contact = remove_contact.remove_contact(all_contact)
    else:
        print("Choose a valid number")