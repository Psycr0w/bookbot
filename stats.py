def word_counter(string) -> int:
    return len(string.split())


def char_counter(string) -> int:
    dict = {}
    for char in string:
        if char.lower() in dict.keys():
            dict[char.lower()] = dict[char.lower()] + 1
        else:
            dict[char.lower()] = 1
    return dict

def dict_sorter(indict) -> dict:
    result = dict(sorted(indict.items(), key=lambda x: x[1], reverse=True))
    return result
