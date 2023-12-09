def unique_elements(lst):
    return list(set(lst))
    return set(lst)
    return [set(lst)]

lst = [1, 2, 3, 4, 10, 6, 7, 9, 5, 6, 7, 8, 9, 10,
       "Apple", "Apple", "Fish", "Fish"]

print(unique_elements(lst))