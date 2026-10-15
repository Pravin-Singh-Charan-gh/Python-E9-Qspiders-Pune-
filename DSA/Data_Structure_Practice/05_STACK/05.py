# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

class Stack:
    def __init__(self):
        self.lst = []
    def push(self,data):
        self.lst.append(data)
    def pop(self):
        if self.lst:
            return self.lst.pop()
        return None
    def top(self):
        if self.lst:
            return self.lst[-1]
        return None

    def isEmpty(self):
        return len(self.lst)==0

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = Stack()
        st2 = Stack()
        for ch in s:
            if ch=='#':
                st1.pop()
            else: st1.push(ch)

        for ch in t:
            if ch=='#':
                st2.pop()
            else: st2.push(ch)
        
        while (not st1.isEmpty()) and (not st2.isEmpty()):
            ch1 = st1.pop()
            ch2 = st2.pop()

            if ch1 != ch2:
                return False

        return st1.isEmpty() and st2.isEmpty()