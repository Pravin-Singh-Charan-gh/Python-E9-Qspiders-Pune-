# Exercise 2: Dictionary Merging with Logic
# Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.


def merge_dict(d1,d2):
    ans = d1.copy()
    for key in d2:
        if key in ans:
            ans[key]=ans[key]+d2[key]
        else:
            ans[key]=d2[key]
    return ans

d1 = eval(input('Enter the first dictionary : '))
d2 = eval(input('Enter the second dictionary : '))
print(merge_dict(d1,d2))