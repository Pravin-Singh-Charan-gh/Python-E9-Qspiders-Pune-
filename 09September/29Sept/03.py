#write a program to validate a email

# pravin123@gmail.(com/in/gov.in)
# pravin123@gmail.(com/in/gov.in)
# pravin123@gmail.(com/in/gov.in)

# def validate_email(email):
#     if '@' not in email or '.' in email:
#         return False
#     elif email.count('@')>1:
#         return False
#     elif email.

#     is_a_found = is_dot_fount=False

#     for ch in email:
#         if (not is_a_found) and (not ('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9')):
#             return False


def validate_email(email):
    if '@' in email:
        s = email.split('@')
        if len(s) != 2:
            return False

        add,domain = s
        if not add.isalnum():
            return False

        if ' ' in domain:
            return False

        if domain.endswith('com') or domain.endswith('gov.in'):
            return True

    return False

def validate_email(email):
    