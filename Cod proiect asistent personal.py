import re
from datetime import datetime, timedelta

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')

    def validate_contact(self):
        # Validează numărul de telefon și adresa de email
        phone_pattern = r'\d{3}-\d{3}-\d{4}'
        email_pattern = r'[^@]+@[^@]+\.[^@]+'
        valid_phone = re.match(phone_pattern, self.phone) is not None
        valid_email = re.match(email_pattern, self.email) is not None
        if not valid_phone or not valid_email:
            raise ValueError("Invalid phone number or email.")
        return True

class Note:
    def __init__(self, content):
        self.content = content

class ContactsBook:
    def __init__(self):
        self.contacts = []
        self.notes = []

    def add_contact(self, contact):
        if contact.validate_contact():
            self.contacts.append(contact)

    def find_contact(self, search_term):
        # Caută contacte după un termen specific
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]

    def edit_contact(self, name, **kwargs):
        # Editează un contact existent
        for contact in self.contacts:
            if contact.name == name:
                for key, value in kwargs.items():
                    setattr(contact, key, value)
                contact.validate_contact()  # Revalidează contactul după editare

    def delete_contact(self, name):
        # Șterge un contact după nume
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def add_note(self, note):
        self.notes.append(note)

    def find_note(self, search_term):
        # Caută note după un termen specific
        return [note for note in self.notes if search_term.lower() in note.content.lower()]

    def edit_note(self, old_content, new_content):
        # Editează o notă existentă
        for note in self.notes:
            if note.content == old_content:
                note.content = new_content

    def delete_note(self, content):
        # Șterge o notă după conținut
        self.notes = [note for note in self.notes if note.content != content]

    def upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming = today + timedelta(days=days)
        upcoming_birthdays = []
        for contact in self.contacts:
            if contact.birthday.month == upcoming.month and contact.birthday.day == upcoming.day:
                upcoming_birthdays.append(contact)
        return upcoming_birthdays

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Address: {contact.address}, Phone: {contact.phone}, Email: {contact.email}, Birthday: {contact.birthday.strftime('%Y-%m-%d')}")

def main():
    # Crearea obiectului ContactsBook
    my_contacts = ContactsBook()

    # Adăugarea unor contacte de exemplu
    contact1 = Contact("Ana Maria", "Strada Livezii", "123-456-7890", "ana@example.com", "1990-08-10")
    contact2 = Contact("Dan Iom", "Strada Tisa", "987-654-3210", "dan@example.com", "1985-03-15")
    my_contacts.add_contact(contact1)
    my_contacts.add_contact(contact2)

    # Afișarea tuturor contactelor
    print("All Contacts:")
    my_contacts.display_contacts()

    # Afișarea contactelor cu zile de naștere în următoarele 7 zile
    print("\nUpcoming Birthdays (within 7 days):")
    upcoming = my_contacts.upcoming_birthdays(7)
    if upcoming:
        for contact in upcoming:
            print(f"Name: {contact.name}, Birthday: {contact.birthday.strftime('%Y-%m-%d')}")
    else:
        print("No upcoming birthdays within 7 days.")

    # Adăugarea și afișarea notițelor
    note1 = Note("Buy groceries")
    note2 = Note("Call the dentist")
    my_contacts.add_note(note1)
    my_contacts.add_note(note2)

    print("\nNotes:")
    for note in my_contacts.notes:
        print(note.content)

    # Căutarea unui contact
    search_results = my_contacts.find_contact("Ana")
    print("\nSearch Results for 'Ana':")
    for contact in search_results:
        print(f"Found: {contact.name}")

    # Editarea unui contact
    my_contacts.edit_contact("Ana Maria", phone="111-222-3333")
    print("\nContacts after editing Ana's phone number:")
    my_contacts.display_contacts()

    # Ștergerea unui contact
    my_contacts.delete_contact("Dan Iom")
    print("\nContacts after deleting Dan Iom:")
    my_contacts.display_contacts()

    # Editarea unei note
    my_contacts.edit_note("Buy groceries", "Buy groceries and cook dinner")
    print("\nNotes after editing:")
    for note in my_contacts.notes:
        print(note.content)

    # Ștergerea unei note
    my_contacts.delete_note("Call the dentist")
    print("\nNotes after deleting 'Call the dentist':")
    for note in my_contacts.notes:
        print(note.content)

if __name__ == "__main__":
    main()
