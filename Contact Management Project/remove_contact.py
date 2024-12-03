from save_all_contact import save_all_contact


def remove_contact(all_contact):
    print('Which item you want remove give here details...')
    name = input("Enter Your Name : ")
    email = input("Enter Email Address : ")
    number = int(input("Enter Your Phone Number : "))
    address = input('Enter Your Address : ')

    contact = {
        "name": name,
        "email": email,
        "number": number,
        "address": address,
    }

    if contact in all_contact:

        all_contact.remove(contact)

        save_all_contact(all_contact)

        print("Contact Remove Successfully")
        return all_contact
    else:
        print("This Contact can't find")
