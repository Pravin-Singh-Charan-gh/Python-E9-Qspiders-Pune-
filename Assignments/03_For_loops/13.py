# 13. Count frequency of each character in string.

txt = input('Enter the string : ')

freq = dict()

for ch in txt:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1

# printing frequencies
print('Char \t Freq')
for i in freq:
    print(f"{i}\t{freq[i]}")
