#!/usr/bin/python3
# 2-print_alphabet.py
# Brennan D Baraban <375@holbertonschool.com>

"""Print the alphabet in lowercase, not followed by a new line."""
for char_code in range(ord('a'), ord('z') + 1):
    print(chr(char_code), end='')
