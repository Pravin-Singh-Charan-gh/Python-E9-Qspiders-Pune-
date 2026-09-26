# 7. Count vowels in a string.

txt = input('Enter the string : ')
ans = 0
for ch in txt:
    if ch in 'AEIOUaeiou':
        ans += 1
print(ans)