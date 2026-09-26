# # Exercise 4: Anagram Checker
# # Practice Problem: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).

def pythonic_is_anagram(s1,s2):
    return sorted(s1.lower().replace(' ','')) == sorted(s2.lower().replace(' ',''))

# def optimized_is_anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     freq = dict()

#     for ch in s1:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1

#     for ch in s2:
#         if ch not in freq:
#             return False
#         freq[ch]-=1
#         if freq[ch]<0:
#             return False
#     return True


# # Optimized program uses a dictionary to store the frequencies of all characters of the first string. It does not need to sort the strings which reduces much the time complexity by high margin, it also need not to create 

txt1 = input('Enter the first string : ')
txt2 = input('Enter the second string : ')

# if optimized_is_anagram(txt1,txt2):
#     print('Anagaram')
# else:
#     print('Not anagram')

# if pythonic_is_anagram(txt1,txt2):
#     print('Anagaram')
# else:
#     print('Not anagram')

import tracemalloc

# Start tracing memory allocations
tracemalloc.start()

# --- Your code goes here ---
if pythonic_is_anagram(txt1,txt2):
    print('Anagaram')
else:
    print('Not anagram')
# ---------------------------

# Get current and peak memory usage (in bytes)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6} MB")
print(f"Peak memory usage: {peak / 10**6} MB")

# Stop tracing
tracemalloc.stop()