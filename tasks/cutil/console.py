# -*- coding: utf-8 -*-"

"""
Functions for works with the console input/output
"""

from typing import Union
from colorama import Style, Fore


HELP_TEXT_COLOR = Fore.BLUE
EXIT_TEXT_COLOR = Fore.YELLOW
WELLCOME_TEXT_COLOR = Fore.GREEN
ERROR_TEXT_COLOR = Fore.RED


def console_style_reset() -> None:
    """Reset console output to defaults
    """
    print(Style.RESET_ALL)


def print_colored(*args) -> None:
    """Print colored text to the console output

    :param args: arguments to print (tuple of Fore and strings)
    """
    if len(args) > 0 and isinstance(args[0], tuple):
        color, *strings = args[0]
        print(color + " ".join(strings), Style.RESET_ALL)
    else:
        print(" ".join([*args]))


def print_error(error: Union[str, Exception]) -> None:
    """Print RED colored text to the console output

    :param error: error to print (string, Exception)
    """
    print_colored((ERROR_TEXT_COLOR, str(error) if isinstance(error, Exception) else error, ))


def print_welcome(text: str) -> None:
    """Print GREEN colored welcome text to the console output

    :param text: text  to print (string)
    """
    print()
    print_colored((WELLCOME_TEXT_COLOR, text, ))
    print()


def print_exit(text: str) -> None:
    """Print YELLOW colored exit text to the console output

    :param text: text  to print (string)
    """
    print()
    print_colored((EXIT_TEXT_COLOR, text, ))
    print()


def print_help(text: str) -> None:
    """Print BLUE colored help text to the console output

    :param text: text  to print (string)
    """
    print()
    print_colored((HELP_TEXT_COLOR, "#" * 60,))
    print_colored((HELP_TEXT_COLOR, text, ))
    print_colored((HELP_TEXT_COLOR, "#" * 60, ))
    print()
