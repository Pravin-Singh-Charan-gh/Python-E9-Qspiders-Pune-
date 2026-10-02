def validate_mail(email):
    items = email.split('@')

    if len(items)!=2:
        return False
    address,domain = items
    domain_items = items[1].split('.')

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

print(validate_mail(      'pravin@gmail.gov.in.in'     ))