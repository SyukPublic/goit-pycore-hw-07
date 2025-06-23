# -*- coding: utf-8 -*-"

"""
Tests for AddressBook and Record classes
"""

from tasks.address_book import AddressBook, Record


def main():
    try:

        print("#" * 20, "  Test 1  ", "#" * 20)

        # Create an address book
        book = AddressBook()

        # Create a record for John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")
        john_record.add_phone("(111) 222 33-44")
        john_record.add_email("john@test.com")
        # Add John's record to the address book
        book.add_record(john_record)

        # Create a record for Jane
        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")
        jane_record.add_email("jane@test.com")
        # Add Jane's record to the address book
        book.add_record(jane_record)

        # Print all records in the address book
        for name, record in book.items():
            print(record)

    except Exception as e:
        print(e)

    try:

        print("#" * 20, "  Test 2  ", "#" * 20)

        # Find John's record and edit the phone number
        john = book.find("John")
        john.edit_phone("1234567890", "1112223333")
        john.edit_email("john@test.com", "john.john@test.com")
        # Print John's record
        print(john)
        # Print John's phones
        print("John's phones:")
        print("\n".join([str(phone) for phone in john.phones]))
        # Print John's emails
        print("John's emails:")
        print("\n".join([str(email) for email in john.emails]))

        # Find the specific phone number in John's record
        found_phone = john.find_phone("5555555555")
        # Print John's phone number
        print(f"{john.name}: {found_phone}")

        # Find the specific email in John's record
        found_email = john.find_email("john.john@test.com")
        # Print John's email
        print(f"{john.name}: {found_email}")

    except Exception as e:
        print(e)

    try:

        print("#" * 20, "  Test 3  ", "#" * 20)

        # Delete Jane's record
        book.delete_record("Jane")

        # Print all records in the address book
        for name, record in book.items():
            print(record)

    except Exception as e:
        print(e)

    try:

        print("#" * 20, "  Test 4  ", "#" * 20)

        # Create a new record for Jane, including phone numbers and emails, and add it to the address book
        book.add_record(
            Record(
                "Jane",
                phones=["1111111111", "2222222222", "1111111111"],
                emails=["jane@test.com", "jane@test.com", "jane.jane@test.com"],
            )
        )

        # Print all records in the address book
        for name, record in book.items():
            print(record)

    except Exception as e:
        print(e)

    try:

        print("#" * 20, "  Test 5  ", "#" * 20)

        # Create the new address book with John's and Jane's records
        book = AddressBook(
            Record("John", phones=["1234567890"], emails=["john@test.com"]),
            Record(
                "Jane",
                phones=["1111111111", "2222222222", "1111111111"],
                emails=["jane@test.com", "jane@test.com", "jane.jane@test.com"],
            ),
            Record("John", phones=["1234567890", "5555555555"])
        )

        # Print all records in the address book
        for name, record in book.items():
            print(record)

    except Exception as e:
        print(e)

    try:

        print("#" * 20, "  Test 6  ", "#" * 20)

        # Create the new address book with John's and Jane's records
        book = AddressBook(
            Record("John", birthday="20.02.2002", phones=["1234567890"], emails=["john@test.com"]),
            Record(
                "Jane",
                phones=["1111111111", "2222222222", "1111111111"],
                emails=["jane@test.com", "jane@test.com", "jane.jane@test.com"],
            ),
            Record("John 0", birthday="22.06.2002", phones=["1234567890"]),
            Record("John 1", birthday="23.06.2002", phones=["1234567890"]),
            Record("John 2", birthday="29.06.2002", phones=["1234567890"]),
            Record("John 3", birthday="30.06.2002", phones=["1234567890"]),
            Record("John 4", birthday="01.07.2002", emails=["john@test.com"]),
            Record("John 5", birthday="02.07.2002", emails=["john@test.com"]),
            Record("John 6", birthday="03.07.2002", emails=["john@test.com"]),
            Record("John 7", birthday="04.07.2002", emails=["john@test.com"]),
            # congratulation_range_days=10,
        )

        # Print all records in the address book
        for name, record in book.items():
            print(record)

        # Print all the upcoming birthdays
        for record, congratulation_date in book.upcoming_birthdays():
            print(congratulation_date.strftime("%d.%m.%Y") + " " + str(record))

        # Print all the upcoming birthdays grouped by days
        for congratulation_date, records in  book.upcoming_birthdays_by_days().items():
            print(congratulation_date.strftime("%d.%m.%Y"))
            print("\n".join([str(record) for record in records]))

    except Exception as e:
        print(e)

    exit(0)


if __name__ == "__main__":
    main()
