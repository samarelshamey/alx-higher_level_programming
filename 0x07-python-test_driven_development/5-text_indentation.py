#!/usr/bin/python3
"""module for text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after char: ., ? and :

    Args:
        text: testx to be modified

    Raises:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
