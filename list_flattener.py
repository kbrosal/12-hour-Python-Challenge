def list_flatten(nested_list):
    
    flat_list = []

    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(list_flatten(element))
        else:
            flat_list.append(element)
    return flat_list

nested_list = [[1,[2,3,4], "Carabao", ["Apple", "Orange", "Banana", "Mango"], 
               ["Dried", "Ripe", ["Overripe", "Rotten"]], "Belgian"]]

flat_list = list_flatten(nested_list)
print(flat_list)