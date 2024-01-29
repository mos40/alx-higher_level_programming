#!/usr/bin/python3
"""Appends all arguments to a Python list and writes them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').
    load_from_json_file

    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    new_items = sys.argv[1:]
    existing_items.extend(new_items)

    save_to_json_file(existing_items, "add_item.json")
