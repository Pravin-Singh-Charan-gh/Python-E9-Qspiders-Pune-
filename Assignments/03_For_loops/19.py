# 19. Check if two strings are anagrams (without sorting).

def is_anagram(txt1,txt2):
    if len(txt1)!=len(txt2):
        return False
    freq1 = dict()
    freq2 = dict()

    for i in range(len(txt1)):
        if txt1[i] not in freq1:
            freq1[txt1[i]]=1
        else:
            freq1[txt1[i]]+=1

        if txt2[i] not in freq2:
            freq2[txt1[i]]=1
        else:
            freq2[txt2[i]]+=1

    return freq1==freq2


txt1 = input('Enter first string : ')
txt2 = input('Enter second string : ')

print(is_anagram(txt1,txt2))