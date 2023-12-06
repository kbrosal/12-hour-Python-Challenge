def filter_by_profession(people, profession):
    #The get method is used here instead of direct indexing (like person['profession'])
    # to avoid potential KeyError exceptions in case the key 'profession' does not exist in some dictionaries.
    return [person for person in people if person.get('profession') == profession]

people = [
    {'name': 'Thanos', 'age': 30, 'profession': 'Villain'},
    {'name': 'Raven', 'age': 25, 'profession': 'Doctor'},
    {'name': 'Kuku', 'age': 35, 'profession': 'Dancer'},
    {'name': 'Tims', 'age': 26, 'profession': 'Dancer'},
    {'name': 'Kipii', 'age': 25, 'profession': 'Dota Player'}
]

print(filter_by_profession(people, "Dancer"))
