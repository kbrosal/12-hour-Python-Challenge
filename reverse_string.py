def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

s = "Apple"
print(reverse_string(s))