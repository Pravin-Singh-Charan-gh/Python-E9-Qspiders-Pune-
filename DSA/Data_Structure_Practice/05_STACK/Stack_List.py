class Stack:
    def __init__(self):
        self.lst = []
        self.size = 0

    def __len__(self):
        return self.size

    def push(self,n):
        self.lst.append(n)
        self.size+=1

    def pop(self):
        if not self.isEmpty():
            self.size-=1
            return self.lst.pop()
        else:
            return None

    def top(self):
        if not self.isEmpty():
            return self.lst[-1]
        else:
            return None

    def isEmpty(self):
        return len(self)==0

# s = Stack()
# print(s.isEmpty())
# s.push(10)
# print(s.isEmpty())
# print(s.top())
# print(s.pop())
# print(s.isEmpty())
# print(len(s))

st = Stack()
for i in range(10):
    st.push(i)

while not st.isEmpty():
    print(st.pop())