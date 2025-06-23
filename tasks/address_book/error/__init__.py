# -*- coding: utf-8 -*-"

__title__ = 'Address book errors and exceptions'
__author__ = 'Roman'


from .exceptions import *

__all__ = [
    'ContactNotFound',
    'ContactAlreadyExist',
    'ContactNameMandatory',
    'ContactPhoneNotFound',
    'ContactPhoneAlreadyExist',
    'ContactPhoneValueError',
    'ContactEmailNotFound',
    'ContactEmailAlreadyExist',
    'ContactEmailValueError',
    'ContactBirthdayAlreadyExist',
    'ContactBirthdayValueError',
]
