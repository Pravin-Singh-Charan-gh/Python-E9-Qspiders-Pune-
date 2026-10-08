#WAP which takes n number of keyword argument and verify
#whether email exist or not . if email exist, validate the email

def verify(**kwargs):
    return kwargs.get('email') and validate_email(kwargs['email'])

def validate_email(email):
    items = email.split('@')

    if len(items)!=2:
        return False
    address,domain = items
    domain_items = domain.split('.')

    if not address.isalnum():
        return False
    for item in domain_items:
        if not item.isalnum():
            return False
    if len(domain_items)==2 and (domain.endswith('.in') or domain.endswith('.com')) :
        return True
    elif len(domain_items)==3 and domain.endswith('.gov.in'):
        return True

    return False


print(verify(email = 'abc@gma.il.com'))
print(verify(email = 'abc@gmail.com'))
print(verify(email = 'abc@gmail.com'))
