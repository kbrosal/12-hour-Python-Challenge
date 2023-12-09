def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {
    "brand": "Ford",
    "model": "Mustang"
}

dict2 = {
    "year": 1964,
    "color": "White"
}

print(merge_dictionaries(dict1, dict2))