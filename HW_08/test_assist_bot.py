from address_book import Phone, Record, AddressBook
from assist_bot import (
    add_contact,
    change_contact,
    delete_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
)


def run_tests():
    book = AddressBook()

    # Test 1: Add contacts
    print("Test 1: Adding Contacts")
    add_contact(["Alice Johnson", "1234567890"], book)
    add_contact(["Bob Martin", "2345678901"], book)
    add_contact(["Charlie Brown", "3456789012"], book)
    add_contact(["Daisy Miller", "4567890123"], book)

    print(show_all(book))  # Should show all added contacts

    # Test 2: Show phone numbers
    print("\nTest 2: Show Phone Numbers")
    print(show_phone(["Alice Johnson"], book))  # Should return Alice's phone number
    print(show_phone(["Bob Martin"], book))  # Should return Bob's phone number

    # Test 3: Add birthdays
    print("\nTest 3: Adding Birthdays")
    add_birthday(["Alice Johnson", "15.05.1995"], book)
    add_birthday(["Bob Martin", "20.06.1990"], book)

    print(show_birthday(["Alice Johnson"], book))  # Should show Alice's birthday
    print(show_birthday(["Bob Martin"], book))  # Should show Bob's birthday

    # Test 4: Change a contact's phone number
    print("\nTest 4: Change Phone Number")
    print(change_contact(["Alice Johnson", "1234567890", "9876543210"], book))
    print(show_phone(["Alice Johnson"], book))  # Should show the updated phone number

    # Test 5: Delete a contact
    print("\nTest 5: Delete Contact")
    print(delete_contact(["Charlie Brown"], book))
    print(show_all(book))  # Should show remaining contacts without Charlie

    # Test 6: Show upcoming birthdays
    print("\nTest 6: Upcoming Birthdays")
    print(birthdays([], book))  # Should show upcoming birthdays

# Run the tests
if __name__ == "__main__":
    run_tests()
