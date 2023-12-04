def parlindrome_checker(s):
    clean_str = s.replace(' ', '').lower()
    return clean_str == clean_str[::-1]

s = 'malayalam'
ans = parlindrome_checker(s)

if ans:
    print("Yes")
else:
    print("No")