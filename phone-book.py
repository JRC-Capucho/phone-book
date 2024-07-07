class Contact:
    def __init__(self, name, phone, email, favorite):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite

    def get(self) -> dict:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "favorite": self.favorite,
        }


def list_contacts():
    index = 0
    print("\n\tIndex, contact\n")
    for contact in lists:
        print("\t", index, contact, "\n")
        index += 1


def add_contact():
    name = input("\nName: ")
    phone = input("\nPhone: ")
    email = input("\nEmail: ")
    favorite = input("\nFavorite? Y/n\n")

    favorite = favorite.lower() == "y"

    contact = Contact(name, phone, email, favorite)

    lists.append(contact.get())


def edit_contact():
    list_contacts()
    choose = int(input("\nChoose a contact: "))
    contact = lists[choose]

    print(contact)

    name = input("\nName: ")
    phone = input("\nPhone: ")
    email = input("\nEmail: ")
    favorite = input("\nFavorite? Y/n\n")

    contact["name"] = name or contact["name"]
    contact["phone"] = phone or contact["phone"]
    contact["email"] = email or contact["email"]
    contact["favorite"] = favorite.lower() == "y" or contact["favorite"]


def delete_contact():
    list_contacts()

    choose = int(input("\nChoose a contact: "))

    lists.pop(choose)


def list_favorites():
    for contact in lists:
        if contact["favorite"]:
            print(contact)


def favorite_contact():
    list_contacts()

    choose = int(input("\nChoose a contact: "))

    contact = lists[choose]

    contact["favorite"] = True


lists = []

while True:
    print("\n\tPhone list\n")
    print("1. List all contacts\t")
    print("2. Add new contact\t")
    print("3. Edit edit contact\t")
    print("4. Favorite contact\t")
    print("5. List Favorite contacts\t")
    print("6. Delete contact\t")
    print("7. Exit\t")

    number = input("\nChoose a number: ")

    if number == "1":
        list_contacts()

    if number == "2":
        add_contact()

    if number == "3":
        edit_contact()

    if number == "4":
        favorite_contact()

    if number == "5":
        list_favorites()

    if number == "6":
        delete_contact()

    if number == "7":
        break
