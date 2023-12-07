# Project 2
# Name: Justin Agosto
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv
import datetime as dt


# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.

print("Welcome to the Contact List Program")

# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:
def import_csv(filename):
    """
    Imports the contacts from the CSV file.

    Args:
        filename (str): The name of the CSV file.

    Returns:
        dict: The dictionary of contacts.
    """
    contacts = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name = row[0]
                phone = row[1]
                email = row[2]
                birthday = datetime.strptime(row[3], "%m/%d/%Y")
                contacts[name] = {"Phone": phone, "Email": email, "Birthday": birthday}
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")
    return contacts


def add_contact(contacts, name, phone, email, birthday):
    """
    Adds a contact to the dictionary.

    Args:
        contacts (dict): The dictionary of contacts.
        name (str): The name of the contact.
        phone (str): The phone number of the contact.
        email (str): The email address of the contact.
        birthday (str): The birthday of the contact in the format mm/dd/yyyy.

    Returns:
        bool: True if the contact was added, False if it already exists.

    """
    if name in contacts:
        print("Contact already exists.")
        return False
    contacts[name] = {"Phone": phone, "Email": email, "Birthday": datetime.strptime(birthday, "%m/%d/%Y")}
    return True


def view_contacts(contacts):
    """
    Displays the contacts in a table format.

    Args:
        contacts (dict): The dictionary of contacts.
    """
    if not contacts:
        print("No contacts found.")
        return

    print("{:<20} {:<15} {:<25} {:<15}".format("Name", "Phone", "Email", "Birthday"))
    print("-" * 75)
    sorted_contacts = sorted(contacts.items(), key=lambda x: x[0])
    for name, info in sorted_contacts:
        phone = info["Phone"]
        email = info["Email"]
        birthday = info["Birthday"].strftime("%m/%d/%Y")
        print("{:<20} {:<15} {:<25} {:<15}".format(name, phone, email, birthday))


def delete_contact(contacts, name):
    """
    Deletes a contact from the dictionary.

    Args:
        contacts (dict): The dictionary of contacts.
        name (str): The name of the contact to delete.

    Returns:
        bool: True if the contact was deleted, False if it does not exist.
    """
    if name not in contacts:
        print("Contact does not exist.")
        return False
    del contacts[name]
    return True


def next_birthday(contacts):
    """
    Displays the next birthday.

    Args:
        contacts (dict): The dictionary of contacts.
    """
    if not contacts:
        print("No contacts found.")
        return

    today = datetime.now()
    upcoming_birthdays = []
    for name, info in contacts.items():
        birthday = info["Birthday"]
        birthday = birthday.replace(year=today.year)  # Replace year with current year
        if 0 <= (birthday - today).days <= 30:  # Check if within next 30 days
            upcoming_birthdays.append((name, birthday))

    if not upcoming_birthdays:
        print("No birthdays in the next 30 days.")
    else:
        upcoming_birthdays.sort(key=lambda x: x[1])  # Sort by next birthday
        name, birthday = upcoming_birthdays[0]
        birthday_str = birthday.strftime("%m/%d/%Y")
        print("Next birthday: {} on {}".format(name, birthday_str))


def save_csv(contacts, filename):
    """
    Saves the contacts to a CSV file.

    Args:
        contacts (dict): The dictionary of contacts.
        filename (str): The name of the CSV file.

    Returns:
        bool: True if the contacts were saved, False if not.
    """
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Birthday"])
            for name, info in contacts.items():
                phone = info["Phone"]
                email = info["Email"]
                birthday = info["Birthday"].strftime("%m/%d/%Y")
                writer.writerow([name, phone, email, birthday])
        return True
    except IOError:
        print("Error saving contacts.")
        return False


def main():
    """
    Runs the Contact List Program.
    """
    contacts = {}  
    while True:
        print("\nMENU:")
        print("1. Import contacts from CSV")
        print("2. Add contact")
        print("3. View contacts")
        print("4. Delete contact")
        print("5. Next birthday")
        print("0. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":  # Import contacts from CSV
            filename = input("Enter the name of the CSV file: ")
            contacts = import_csv(filename)
        elif choice == "2":  # Add contact
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            birthday = input("Enter birthday (mm/dd/yyyy): ")
            added = add_contact(contacts, name, phone, email, birthday)
            if added:
                print("Contact added.")
        elif choice == "3":  # View contacts
            view_contacts(contacts)
        elif choice == "4":  # Delete contact
            name = input("Enter the name of the contact to delete: ")
            deleted = delete_contact(contacts, name)
            if deleted:
                print("Contact deleted.")
        elif choice == "5":  # Next birthday
            next_birthday(contacts)
        elif choice == "0":  # Quit
            filename = input("Enter a name to save the contacts to CSV file: ")
            saved = save_csv(contacts, filename)
            if saved:
                print("Contacts saved to CSV file.")
            print("Goodbye!")
            break
        


if __name__ == "__main__":
    main()


# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.


# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]


# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.


# delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.

# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.

# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.

# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.




    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?
def count_names_starting_with_a(contacts):
    count_a_names = sum(1 for name in contacts.values() if name.startswith("A"))
    print("Number of names starting with 'A':", count_a_names)

if __name__ == "__main__":
    main()
    # Number of names starting with a: 5

    # How many emails are yahoo emails?
def count_yahoo_emails(contacts):
    count_yahoo_emails = sum(1 for info in contacts.values() if info["Email"].endswith("@yahoo.com"))
print("Number of Yahoo emails:", count_yahoo_emails)
# Number of Yahoo emails: 5

    # How many .org emails are there?
def count_org_emails(contacts):
   count_org_emails = sum(1 for info in contacts.values() if info["Email"].endswith(".org"))
print("Number of .org emails:", count_org_emails)
# Number of .org emails: 2
    # How many contacts have a birthday in January?
def count_january_birthdays(contacts):
    count_january_birthdays = sum(1 for info in contacts.values() if info["Birthday"].month == 1)
print("Number of contacts with a birthday in January:", count_january_birthdays)
# Number of contacts with a birthday in January: 2


if __name__ == "__main__":
    main()
