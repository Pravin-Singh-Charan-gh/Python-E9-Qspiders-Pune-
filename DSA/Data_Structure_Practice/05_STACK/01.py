# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(' , ']':'[', '}':'{'}
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif len(stack)==0 or map[ch]!=stack[-1]: 
                    return False
            else:
                stack.pop()
        
        return len(stack)==0