#!/usr/bin/python3

class ExampleClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def display_attributes(self):
        print(f"Attribute 1: {self.attribute1}")
        print(f"Attribute 2: {self.attribute2}")


if __name__ == "__main__":
    example_instance = ExampleClass(42, "Hello")
    example_instance.display_attributes()
