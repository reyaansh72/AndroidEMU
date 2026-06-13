# consoleutils.py

import os
import sys
import time

RESET = "\033[0m"

# Normal Colors
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"

# Bold Colors
BOLD_BLACK = "\033[1;30m"
BOLD_RED = "\033[1;31m"
BOLD_GREEN = "\033[1;32m"
BOLD_YELLOW = "\033[1;33m"
BOLD_BLUE = "\033[1;34m"
BOLD_PURPLE = "\033[1;35m"
BOLD_CYAN = "\033[1;36m"
BOLD_WHITE = "\033[1;37m"

# Underline Colors
UNDERLINE_BLACK = "\033[4;30m"
UNDERLINE_RED = "\033[4;31m"
UNDERLINE_GREEN = "\033[4;32m"
UNDERLINE_YELLOW = "\033[4;33m"
UNDERLINE_BLUE = "\033[4;34m"
UNDERLINE_PURPLE = "\033[4;35m"
UNDERLINE_CYAN = "\033[4;36m"
UNDERLINE_WHITE = "\033[4;37m"

# Background Colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_PURPLE = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# High Intensity Colors
HI_BLACK = "\033[0;90m"
HI_RED = "\033[0;91m"
HI_GREEN = "\033[0;92m"
HI_YELLOW = "\033[0;93m"
HI_BLUE = "\033[0;94m"
HI_PURPLE = "\033[0;95m"
HI_CYAN = "\033[0;96m"
HI_WHITE = "\033[0;97m"

# High Intensity Backgrounds
BG_HI_BLACK = "\033[100m"
BG_HI_RED = "\033[101m"
BG_HI_GREEN = "\033[102m"
BG_HI_YELLOW = "\033[103m"
BG_HI_BLUE = "\033[104m"
BG_HI_PURPLE = "\033[105m"
BG_HI_CYAN = "\033[106m"
BG_HI_WHITE = "\033[107m"


def slow_print(text, delay=0.03):
    """Print text slowly."""
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def color_print(text, color):
    """Print text with a specified ANSI color."""
    print(f"{color}{text}{RESET}")


def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


# Quick color print functions
def black_print(text): color_print(text, BLACK)
def red_print(text): color_print(text, RED)
def green_print(text): color_print(text, GREEN)
def yellow_print(text): color_print(text, YELLOW)
def blue_print(text): color_print(text, BLUE)
def purple_print(text): color_print(text, PURPLE)
def cyan_print(text): color_print(text, CYAN)
def white_print(text): color_print(text, WHITE)