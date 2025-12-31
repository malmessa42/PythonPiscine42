import sys
from ft_filter import ft_filter


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
    """
    Processes command-line arguments, splits the string, and prints words
    longer than the given number.
    """

    argc = len(sys.argv)
    if (argc != 3 or not sys.argv[2].isdigit()):
        print("AssertionError: the arguments are bad")
        sys.exit(0)
    try:
        number = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(0)

    if contains_non_printable_chars(sys.argv[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(0)
    if contains_special_chars(sys.argv[1]):
        print("AssertionError: the arguments are bad")
        sys.exit(0)

    # python ex06/filterstring.py "$(echo -e 'Hello\nWorld')" 2

    all_words = sys.argv[1].split()
    long_words = list(ft_filter(lambda word: len(word) > number, all_words))
    print(long_words)


if __name__ == "__main__":
    main()
