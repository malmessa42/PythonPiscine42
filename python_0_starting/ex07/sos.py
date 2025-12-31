import sys


def contains_non_printable_chars(s):
    """
    Returns True if the string contains non-printable characters.
    """
    return any(not c.isprintable() for c in s)


def contains_special_chars(s):
    """
    Returns True if the string contains special characters (punctuation).
    """

    punctuation_chars = ".,!?;:'\"()[]{}<>-_+=#@&$%^*|\\/~`"
    return any(c in punctuation_chars for c in s)


def main():
    argc = len(sys.argv)
    if (argc != 2):
        print("AssertionError: the arguments are bad")
        exit(0)

    if contains_non_printable_chars(sys.argv[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(0)
    if contains_special_chars(sys.argv[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(0)

    NESTED_MORSE = {"A": ".- ", "B": "-... ", "C": "-.-. ",
                    "D": "-.. ", "E": ". ", "F": "..-. ",
                    "G": "--. ", "H": ".... ", "I": ".. ",
                    "J": ".--- ", "K": "-.- ", "L": ".-.. ",
                    "M": "-- ", "N": "-. ", "O": "--- ",
                    "P": ".--. ", "Q": "--.- ", "R": ".-. ",
                    "S": "... ", "T": "- ", "U": "..- ",
                    "V": "...- ", "W": ".-- ", "X": "-..- ",
                    "Y": "-.-- ", "Z": "--.. ", "0": "----- ",
                    "1": ".---- ", "2": "..--- ", "3": "...-- ",
                    "4": "....- ", "5": "..... ", "6": "-.... ",
                    "7": "--... ", "8": "---.. ", "9": "----. ",
                    " ": "/ "}
    for c in sys.argv[1]:
        if c.upper() not in NESTED_MORSE:
            print("AssertionError: the arguments are bad")
            sys.exit(0)
    print(''.join(NESTED_MORSE[c.upper()] for c in sys.argv[1]).strip())


if __name__ == "__main__":
    main()

# Double Quotes ("): In many shells (like Bash), double quotes allow
    # the expansion of certain special characters (e.g., $, *, etc.).
    # This means that if you use double quotes around a string that includes $,
    # the shell will attempt to interpret it (e.g., as a variable).
# Single Quotes ('): Single quotes prevent the shell from expanding special
    # characters.Everything inside single quotes is treated literally.
