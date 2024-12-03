def view_all_contact(all_contact):
    if all_contact != []:
        for contact in all_contact:
            print(f"Name : {contact['name']} | Email : {contact['email']} | Phone number : {contact['number']} | Address : {contact['address']} ")
    else:
        print("No contact found in program")