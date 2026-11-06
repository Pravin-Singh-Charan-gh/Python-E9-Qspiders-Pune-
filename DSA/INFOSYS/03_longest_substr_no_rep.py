# Longest Substring Without Repeating Characters
# naiva
# def fun(s):
#     n = len(s)
#     ans = 0
#     for i in range(n):
#         st = set()
#         curr = 0
#         for j in range(i,n):
#             if s[j] in st:
#                 break
#             st.add(s[j])
#             curr+=1
#         ans = max(curr,ans)
#     return ans


def real(s):
    hm = {}
    ans = 0
    st = 0
    for i in range(len(s)):
        ch = s[i]
        if ch in hm:
            ind = hm[ch]
            if ind>=st:
                st = ind+1
        hm[ch] = i
        ans = max(ans,i-st+1)
    return ans
            
s = 'geeksforgeeks'
print(real(s))