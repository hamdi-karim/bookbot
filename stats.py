def get_words_number(text):
    words = text.split()
    return len(words)


def get_characters_occurrences(text):
    dict_characters = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char in dict_characters:
            dict_characters[char] += 1
        else:
            dict_characters[char] = 1
    return dict_characters


def sort_on(dict):
    return dict["num"]


def get_sorted_report_dictionaries(dict):

    report_list = []
    for key, value in dict.items():
        report_dict = {"char": key, "num": value}
        report_list.append(report_dict)

    report_list.sort(reverse=True, key=sort_on)
    return report_list
