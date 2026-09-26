#Write a program that takes two separate dictionaries and merges them into one single dictionary.

def merge_dict(d1,d2):
##    ans = dict()
##    for i in d1:
##        ans[i]=d1[i]
##    for i in d2:
##        ans[i]=d2[i]
##    return ans
    return d1|d2;
d1 = eval(input('Enter the first dictionary : '))
d2 = eval(input('Enter the second dictionary : '))
print(merge_dict(d1,d2))
