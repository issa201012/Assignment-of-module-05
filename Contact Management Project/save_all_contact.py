def save_all_contact(all_contact):
    with open("all_contact.csv", "w") as fp:
        for contact in all_contact:
            line = f"{contact['name']}, {contact['email']}, {contact['number']}, {contact['address']}\n"
            fp.write(line)