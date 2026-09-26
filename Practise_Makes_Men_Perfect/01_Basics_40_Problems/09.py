#Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

def vowel_count(txt):
    ans = 0
    for ch in txt:
        if ch in 'AEIOUaeiou':
            ans+=1
    return ans

txt = input('Enter the string : ')

print(f"Number of vowels present in '{txt}' : {vowel_count(txt)}")
