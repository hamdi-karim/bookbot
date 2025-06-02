from stats import (
    get_characters_occurrences,
    get_sorted_report_dictionaries,
    get_words_number,
)

import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text(sys.argv[1])
    occurrences = get_characters_occurrences(book_text)
    sorted_dictionaries_list = get_sorted_report_dictionaries(occurrences)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words_number(book_text)} total words")
    print("--------- Character Count -------")

    for i in range(len(sorted_dictionaries_list)):
        char = sorted_dictionaries_list[i]["char"]
        if not char.isalpha():
            continue
        num = sorted_dictionaries_list[i]["num"]

        print(f"{char}: {num}")

    print("============= END ===============")


main()
