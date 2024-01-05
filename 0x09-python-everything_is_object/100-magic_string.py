#!/usr/bin/python3

def generate_magic_string():
    generate_magic_string.count = getattr(generate_magic_string, 'count', 0) + 1
    return ("BestSchool, " * (generate_magic_string.count - 1) + "BestSchool")
