#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Indent the text based on delimiters '?', ':', and '.'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        text = (delimiter + "\n\n").join(
            [sentence.strip(" ") for sentence in text.split(delimiter)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
