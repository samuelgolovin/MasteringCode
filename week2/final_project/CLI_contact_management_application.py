# This CLI application will manage contacts, allow add/search/edit/delete
# functionality, using a dictionary for data storage

# example dictionary with key and value
# contacts = {"John Doe": "(555)-555-5555", "Joey Smith": "(555)-555-5556"}

# possible future additions could include a file where the contacts can be saved to and read from 
# for a more permanent contact management application

class Contacts:
    def __init__(self):
        self.name_to_number = {}
        self.number_to_name = {}

    def add_contact(self, name, number):
        self.name_to_number[name] = number
        self.number_to_name[number] = name

    def delete_name(self, name):
        del self.number_to_name[self.name_to_number[name]]
        del self.name_to_number[name]

    def delete_number(self, number):
        del self.name_to_number[self.number_to_name[number]]
        del self.number_to_name[number]
        
    def edit_contact(self, old_name, old_number, new_name, new_number):
        self.delete_name(old_name)
        self.add_contact(new_name, new_number) 

    def search_by_name(self, name):
        if name in self.name_to_number:
            print("(" + name + ", " + self.name_to_number[name] + ")")
            return True
        else:
            print(name + " not found. Try again.")
            return False

    def search_by_number(self, number):
        if number in self.number_to_name:
            print("(" + number + ", " + self.number_to_name[number] + ")")
            return True
        else:
            print(number + " not found. Try again.")
            return False
            
    def show_all_names(self):
        print()
        for name in self.name_to_number:
            print("{'" + name + "': '" + self.name_to_number[name] + "'}")

    def show_all_numbers(self):
        print()
        for number in self.number_to_name:
            print("{'" + number + "': '" + self.number_to_name[number] + "'}")

contact_info = Contacts()

print("This CLI application keeps track of your contacts.")

while 1:
    input_value = input("\n 'A' to add a contact\n 'D' to delete a contact\n 'E' to edit a contact\n \
'S' to search for a contact\n 'V' to view all contacts\n 'Q' to quit\n :")

    if input_value == "a" or input_value == "A":
        adding_contact = True
        while adding_contact:
            contact_name = input("Name of new contact or 'C' to cancel: ")
            if contact_name in contact_info.name_to_number or contact_name in contact_info.number_to_name:
                print("Name already exists as a contact. Try again.")
                continue
            elif contact_name == "c" or contact_name == "C":
                break
            else:
                while 1:
                    contact_number = input("Number of new contact or 'C' to cancel: ")
                    if contact_number in contact_info.number_to_name or contact_number in contact_info.name_to_number:
                        print("Number already exists in contacts. Try again.")
                    elif contact_number == "c" or contact_number == "C":
                        adding_contact = False
                        break
                    else:
                        contact_info.add_contact(contact_name, contact_number)
                        adding_contact = False
                        break
    elif input_value == "d" or input_value == "D":
        if len(contact_info.name_to_number) > 0:
            deleting_contact = True
            while deleting_contact:
                type_of_delete = input("Would you like to delete contact by 'A': name or 'B': number ('C' to cancel)?\n: ")
                if type_of_delete == "a" or type_of_delete == "A":
                    while 1:
                        name_to_delete = input("Name of contact to delete or 'C' to cancel: ")
                        if name_to_delete in contact_info.name_to_number:
                            contact_info.delete_name(name_to_delete)
                            print("Contact " + name_to_delete + " deleted.")
                            deleting_contact = False
                            break
                        elif name_to_delete == "c" or name_to_delete == "C":
                            deleting_contact = False
                            break
                        else:
                            print("Name not found in contacts. Try again.")
                            continue
                elif type_of_delete == "b" or type_of_delete == "B":
                    while 1:
                        number_to_delete = input("Number of contact to delete or 'C' to cancel: ")
                        if number_to_delete in contact_info.number_to_name:
                            contact_info.delete_number(number_to_delete)
                            print("Contact with the number " + number_to_delete + " deleted.")
                            deleting_contact = False
                            break
                        elif number_to_delete == "c" or number_to_delete == "C":
                            deleting_contact = False
                            break
                        else:
                            print("Name not found in contacts. Try again.")
                            continue
                elif type_of_delete == "c" or type_of_delete == "C":
                    break
                else:
                    print("Invalid input. Try again.")
        else:
            print("\nAdd a concact to delete.")
                
    elif input_value == "e" or input_value == "E":
        if len(contact_info.name_to_number) > 0:
            while 1:
                print("Enter the Name and Number of contact to edit.")
                while 1:
                    old_name = input("Name: ")
                    if old_name in contact_info.name_to_number:
                        break
                    else:
                        print("'" + old_name + "' not found in contacts. Try again.")
                while 1:
                    old_number = input("Number: ")
                    if old_number in contact_info.number_to_name:
                        break
                    else:
                        print("'" + old_number + "' not found in contacts. Try again.")

                new_name = input("Enter the NEW Name and Number of contact to edit\nName: ")
                new_number = input("Number: ")
                contact_info.edit_contact(old_name, old_number, new_name, new_number)
                break
        else:
            print("\nAdd a concact to edit.")
        
    elif input_value == "s" or input_value == "S":
        if len(contact_info.name_to_number) > 0:
            while 1:
                search_type = input("Search by '1' Name or '2' Number or 'C' to cancel: ")
                if search_type == '1':
                    while 1:
                        name = input("Name to search: ")
                        if contact_info.search_by_name(name):
                            break
                elif search_type == '2':
                    while 1:
                        number = input("Number to search: ")
                        if contact_info.search_by_number(number):
                            break
                elif search_type == 'c' or search_type == 'C':
                    break
                else:
                    print("Invalid input. Try again.")
        else:
            print("\nAdd a concact to search.")

    elif input_value == "v" or input_value == "V":
        if len(contact_info.name_to_number) > 0:
            while 1:
                type_of_view = input("View by '1' Names or '2' Numbers or 'C' to cancel: ")
                if type_of_view == '1':
                    contact_info.show_all_names()
                elif type_of_view == '2':
                    contact_info.show_all_numbers()
                elif type_of_view == 'c' or type_of_view == 'C':
                    break
                else:
                    print("Invalid input. Try again.")
        else:
            print("\nAdd a concact to view.")
                
    elif input_value == "q" or input_value == "Q":
        print("Have a good day!")
        break
    else:
        print("Invalid input. Try again.")

