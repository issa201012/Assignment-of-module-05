from save_all_contact import save_all_contact


def add_contact(all_contact):
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

    all_contact.append(contact)
    save_all_contact(all_contact)

    print("Contact Added Successfully")
    return all_contact
