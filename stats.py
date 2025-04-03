def count_words(text: str) -> int:
    return len(text.split())

def char_count(text: str) -> dict[str, int]:
    low_text = text.lower()
    char_dict = {}
    for c in low_text:
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict

def char_dict_sorter(char_dict: dict[str, int]) -> list[dict]:
    dict_lst = [ {'char': c, 'count': count } for c, count in char_dict.items() ]
    dict_lst.sort(reverse=True, key=lambda a: a['count'])
    return dict_lst
