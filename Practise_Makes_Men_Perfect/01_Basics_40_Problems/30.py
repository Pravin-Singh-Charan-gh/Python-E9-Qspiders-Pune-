##Exercise 30. Word Frequency Counter (The Histogram)
##Practice Problem: Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

def count_word_in_para(para):
    ans = dict()
    words = para.split()

    for word in words:
        if word in ans :
            ans[word]+=1
        else:
            ans[word]=1
    return ans

para = input('Enter the paragraph : ')
print(count_word_in_para(para))
