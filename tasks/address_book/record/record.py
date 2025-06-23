# -*- coding: utf-8 -*-"

"""
Record class for address book implementation
"""

import re
import datetime
from typing import Optional, Any


from ..error import (
    ContactNameMandatory,
    ContactPhoneNotFound,
    ContactPhoneAlreadyExist,
    ContactPhoneValueError,
    ContactEmailNotFound,
    ContactEmailAlreadyExist,
    ContactEmailValueError,
    ContactBirthdayAlreadyExist,
    ContactBirthdayValueError,
)


class Field:
    def __init__(self, value: Any):
        """ Initialize the field with the specified value

        :param value: the value (string, mandatory)
        """
        self.value = value

    def __str__(self) -> str:
        """ Create a readable string for the class instance

        :return: readable string (string)
        """
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        """ Initialize the Name field with the specified value

        :param value: the value (string, mandatory)
        """
        # Check whether the name is empty or None
        if not value:
            raise ContactNameMandatory()
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str):
        """ Initialize the Birthday field with the specified value

        :param value: the value (string, mandatory)
        """
        super().__init__(self.prepare(value))

    @classmethod
    def prepare(cls, value: str) -> datetime.date:
        """ Birthday validation and conversion

        :param value: birthday string (string, mandatory)
        :return: birthday (datetime)
        """
        # Check whether the birthday value is correct
        try:
            return datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ContactBirthdayValueError()

    def date_of_birth(self) -> datetime.date:
        """Return the date of birth.

        :return: Date of birth (date)
        """
        return self.value

    def birthday(self, year: int) -> datetime.date:
        """Return the anniversary of the birth shifted to the specified year. If the date is on February 29 and
        today's year is not a leap year, move it to March 1.

        :param year: Year to which the date should be shifted (int, mandatory)
        :return: Date shifted to the specified year (date)
        """
        try:
            return self.value.replace(year=year)
        except ValueError:
            # Handles February 29 in a non-leap year, shifts it to March 1
            return datetime.date(year, 3, 1)

    def __str__(self) -> str:
        """ Create a readable string for the Birthday class instance

        :return: readable string (string)
        """
        return self.value.strftime("%d.%m.%Y")


class Phone(Field):
    value_clear_pattern = re.compile(r"[()-]|\s")
    value_match_pattern = re.compile(r"^\d{10}$")

    def __init__(self, value: str):
        """ Initialize the Phone number field with the specified value

        :param value: the value (string, mandatory)
        """
        super().__init__(self.prepare(value))

    @classmethod
    def prepare(cls, value: str) -> str:
        """ Phone number validation and sanitization

        :param value: phone number (string, mandatory)
        :return: sanitized phone number (string)
        """

        # Check whether the phone number is empty or None
        if not value:
            raise ContactPhoneValueError()
        # Clear the phone number from formatting symbols and whitespaces
        value = re.sub(cls.value_clear_pattern, '', value)
        # Verify the phone number
        if not re.match(cls.value_match_pattern, value):
            raise ContactPhoneValueError()
        return value


class Email(Field):
    value_clear_pattern = re.compile(r"\s")
    value_match_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def __init__(self, value: str):
        """ Initialize the Email field with the specified value

        :param value: the value (string, mandatory)
        """
        super().__init__(self.prepare(value))

    @classmethod
    def prepare(cls, value: str) -> str:
        """ Email number validation and sanitization

        :param value: email (string, mandatory)
        :return: sanitized email (string)
        """

        # Check whether the email is empty or None
        if not value:
            raise ContactEmailValueError()
        # Clear the email from whitespaces
        value = re.sub(cls.value_clear_pattern, '', value)
        # Verify the email
        if not re.match(cls.value_match_pattern, value):
            raise ContactEmailValueError()
        return value


class Record:
    def __init__(
            self,
            name: str,
            birthday: Optional[str] = None,
            phones: Optional[list[str]] = None,
            emails: Optional[list[str]] = None,
    ):
        """ Initialize the Contact record for the specified Name and with the Birthday, Phone numbers oe Emails, if given

        :param name: the name value (string, mandatory)
        :param name: the birthday value (string, optional)
        :param phones: the phone numbers (list of strings, optional)
        :param emails: the emails (list of strings, optional)
        """
        self.name = Name(name)
        self.birthday = None
        self.phones = []
        self.emails = []
        # Add birthday if given
        if isinstance(birthday, str):
            self.edit_birthday(birthday)
        # Add phone numbers if given, removing duplicates
        if isinstance(phones, list):
            for phone in phones:
                if self.__find_phone(phone) is None:
                    self.add_phone(phone)
        # Add emails if given, removing duplicates
        if isinstance(emails, list):
            for email in emails:
                if self.__find_email(email) is None:
                    self.add_email(email)

    def __find_phone(self, phone: str) -> Optional[Phone]:
        """ Private method for searching the phone number

        :param phone: phone number (string, mandatory)
        :return: phone field, if found (Phone, optional)
        """
        # Clear the phone number from formatting symbols and whitespaces
        phone = Phone.prepare(phone)
        # Find and return by phone number
        return next((p for p in self.phones if p.value == phone), None)

    def __find_email(self, email: str) -> Optional[Email]:
        """ Private method for searching the email

        :param email: email (string, mandatory)
        :return: email field, if found (Email, optional)
        """
        # Clear the email fom whitespaces
        email = Email.prepare(email)
        # Find and return by email
        return next((p for p in self.emails if p.value == email), None)

    def edit_name(self, name: str) -> None:
        """ Edit the name, or raise the name value mandatory exception

        :param name: contact`s name (string, mandatory)
        """
        self.name = Name(name)

    def add_birthday(self, birthday: str) -> None:
        """ Add the birthday, or raise the birthday already exists exception

        :param birthday: birthday (string, mandatory)
        """
        if self.birthday is not None:
            raise ContactBirthdayAlreadyExist()
        # Add the birthday
        self.edit_birthday(birthday)

    def edit_birthday(self, birthday: str) -> None:
        """ Edit the birthday, or raise the birthday value error exception

        :param birthday: birthday (string, mandatory)
        """
        self.birthday = Birthday(birthday)

    def next_birthday(self, today: datetime.date) -> Optional[datetime.date]:
        """Return the next birthday of contact. If the birthday is on February 29 and today's year is not a leap year,
        move it to March 1.

        :param today: Today's date (date, mandatory)
        :return: Next birthday date (date, optional)
        """
        # If contact does not have a birthday, return None
        if self.birthday is None:
            return None

        birthday: datetime.date = self.birthday.birthday(today.year)
        if birthday < today:
            # If the birthday has already passed this year, shift the date to the next year
            birthday = self.birthday.birthday(today.year + 1)

        return birthday

    def find_phone(self, phone: str) -> Phone:
        """ Search and return the phone number, or raise the phone number not found exception

        :param phone: phone number (string, mandatory)
        :return: phone field, if found (Phone)
        """
        phone_object: Optional[Phone] = self.__find_phone(phone)
        if phone_object is None:
            # Phone number not found - raise the phone number not found exception
            raise ContactPhoneNotFound()
        # Return the phone number field
        return phone_object

    def add_phone(self, phone: str) -> None:
        """ Add the phone number, or raise the phone number already exists exception

        :param phone: phone number (string, mandatory)
        """
        if self.__find_phone(phone):
            # Phone number found - raise the phone number already exists exception
            raise ContactPhoneAlreadyExist()
        # Add the phone number
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """ Remove the phone number, or raise the phone number not found exception

        :param phone: phone number (string, mandatory)
        """
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, existing_phone: str, phone: str) -> None:
        """ Edit the phone number, or raise the phone number not found exception

        :param existing_phone: phone number (string, mandatory)
        :param phone: new phone number (string, mandatory)
        """
        self.phones[self.phones.index(self.find_phone(existing_phone))] = Phone(phone)

    def find_email(self, email: str) -> Phone:
        """ Search and return the email, or raise the email not found exception

        :param email: email (string, mandatory)
        :return: email field, if found (Email)
        """
        email_object: Optional[Phone] = self.__find_email(email)
        if email_object is None:
            # Email not found - raise the email not found exception
            raise ContactEmailNotFound()
        # Return the phone number field
        return email_object

    def add_email(self, email: str) -> None:
        """ Add the email, or raise the email already exists exception

        :param email: email (string, mandatory)
        """
        if self.__find_email(email):
            # Email found - raise the email already exists exception
            raise ContactEmailAlreadyExist()
        # Add the email
        self.emails.append(Email(email))

    def remove_email(self, email: str) -> None:
        """ Remove the email, or raise the email not found exception

        :param email: email (string, mandatory)
        """
        self.emails.remove(self.find_email(email))

    def edit_email(self, existing_email: str, email: str) -> None:
        """ Edit the email, or raise the email not found exception

        :param existing_email: email (string, mandatory)
        :param email: new email (string, mandatory)
        """
        self.emails[self.emails.index(self.find_email(existing_email))] = Email(email)


    def __str__(self) -> str:
        """ Create a readable string for the class instance

        :return: readable string (string)
        """
        return "Contact name: {name}, birthday: {birthday}, phones: {phones}, emails: {emails}".format(
            name=str(self.name),
            birthday=str(self.birthday) if self.birthday is not None else "-",
            phones="; ".join(str(p) for p in self.phones),
            emails="; ".join(str(p) for p in self.emails),
        )
