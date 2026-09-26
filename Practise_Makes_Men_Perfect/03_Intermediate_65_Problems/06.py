# Exercise 6: Reverse Each Word of a String
# Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order.

def reverse_words(txt):
    words = txt.split()
    reversed_words = [word[::-1] for word in words]

    return " ".join(reversed_words)

txt = input('Enter the text : ')
print(reverse_words(txt))