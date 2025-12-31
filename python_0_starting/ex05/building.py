# Allowed functions : sys or any other library that allows to receive the args

import sys


"""

The script counts characters in a given text.
    1. It checks if the text is passed as a command-line
        argument or prompts the user for input.
    2. Counts uppercase letters, lowercase letters,
        punctuation, spaces, and digits.
If more than one argument is provided, it shows an error and exits.

"""


def main():

    # your tests and your error handling
    # print(__doc__)

    """

    The script counts characters in a given text.
        1. It checks if the text is passed as a command-line
            argument or prompts the user for input.
        2. Counts uppercase letters, lowercase letters,
            punctuation, spaces, and digits.
    If more than one argument is provided, it shows an error and exits.

    """

    argc = len(sys.argv)
    if argc > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(0)
    text = None
    if argc == 1:
        while text is None:
            print("What is the text to count?")
            text = sys.stdin.readline()
            if len(text) == 0:
                text = None
    else:
        text = sys.argv[1]

    print("The text contains {} characters:".format(len(text)))
    up = 0
    down = 0
    punc = 0
    space = 0
    digits = 0
    for c in text:
        if c.isupper():
            up = up + 1
        elif c.islower():
            down = down + 1
        elif c.isspace() or c == '\t':
            space = space + 1
        elif c.isdigit():
            digits = digits + 1
        elif not c.isalpha():
            punc = punc + 1
    print(f"{up} upper letters")
    print(f"{down} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")

    # print("---" + text + "---")


if __name__ == "__main__":
    main()
