import re

def is_valid_email(email):
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    
    return re.match(pattern, email) is not None        

test_emails = ["test@example.com", "invalidemail@.com", "noatdot.com", 
               "multiple..dots@domain.com", "valid.email@domain.co.uk"]
for email in test_emails:
    print(f"Is {email} a valid email? {is_valid_email(email)}")


# return "a" in email and "." in email and email.count("@") == 1 \
#         and email[email.index("@") + 1:].count(".") >= 1

#^[-!#$%&'*+/=?^_`{|}~A-Za-z0-9]+(?:\.[-!#$%&'*+/=?^_`{|}~A-Za-z0-9]+)*@([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9]"]