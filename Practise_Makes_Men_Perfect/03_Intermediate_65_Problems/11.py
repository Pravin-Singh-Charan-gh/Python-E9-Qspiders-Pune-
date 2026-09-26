##Exercise 11: Dictionary Merging (Value Grouping)
##Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.

def merge_dict(d1,d2):
    new = d1.copy()
    all_keys = set(d1.keys())|set(d2.keys())

    for key in all_keys:
        values = []
        if key in d1: values.append(d1[key])
        if key in d2: values.append(d2[key])
        new[key]=values
    return new
            

d1 = eval(input('Enter the first dictionary : '))
d2 = eval(input('Enter the second dictionary : '))
        
print(merge_dict(d1,d2))
