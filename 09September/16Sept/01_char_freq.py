# Count the frequencies of all characters in a string

txt = input('Enter the string : ')

h = []

for ch in txt:
    
    if ch not in h:

        count = 0
        for j in txt:
            if j == ch:
                count+=1
        h.append(ch)
        print(ch," : ",count)