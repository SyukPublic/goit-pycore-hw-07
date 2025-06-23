# -*- coding: utf-8 -*-"

"""
Help for contacts bot
"""


CONTACTS_BOT_HELP: str = """
1. Command "hello" – displays the phrase "How can I help you?"

Example:
Input: "hello"
Output: "How can I help you?"

---

2. Command "add [name] [phone number]" – adds a contact

Example:
Input: "add John 1234567890"
Output: "Contact added."

---

3. Command "change [name] [existing phone number] [new phone number]" – updates the contact's phone number

Example:
Input: "change John 0987654321 1234567890"
Output: "Contact updated." or an error message if the name is not found

---

4. Command "phone [name]" – returns the phone numbers for the contact

Example:
Input: "phone John"
Output: [phone numbers] or an error message if the name is not found

---

5. Command "add-birthday [name] [date of birth]" – adds a contact's date of birth

Example:
Input: "add-birthday John 02.12.1991"
Output: "Date of birth added." or an error message if the name is not found

---

6. Command "change-birthday [name] [date of birth]" – updates the contact's date of birth

Example:
Input: "change-birthday John 12.02.1991"
Output: "Date of birth updated." or an error message if the name is not found

---

7. Command "show-birthday [name]" – returns the date of birth for the contact

Example:
Input: "show-birthday John"
Output: [date of birth] or an error message if the name is not found

---

8. Command "delete [name]" – deletes the contact

Example:
Input: "delete John"
Output: "Contact deleted." or an error message if the name is not found

---

9. Command "all" – returns the list of all contacts

Example:
Input: "all"
Output: all saved contacts with their phone numbers

---

10. Command "birthdays" – returns the date of birth for the contacts whose birthday is within the next week,
including today, grouped by date

Example:
Input: "birthdays"
Output: all contacts whose birthday is within the next week, including today, grouped by date,
        along with the congratulation date. If the birthday falls on a weekend, the congratulation date
        is moved to the following Monday.

---

11. Command "quit", "exit", or "close" – ends the bot session

Example:
Input: any of these words
Output: "Good bye!" and the bot stops running
"""
