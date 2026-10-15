class Queue:
    def __init__(self):
        self.lst = []

    def __len__(self):
        return len(self.lst)

    def isEmpty(self):
        return len(self.lst)==0

    def front(self):
        return self.lst[0] if len(self)>0 else None 

    def push(self,n):
        self.lst.append(n)

    def pop(self):
        if not len(self):
            return None
        ans = self.lst[0]
        del self.lst[0]
        return ans

q = Queue()
for i in range(10):
    q.push(i)

while not q.isEmpty():
    print(q.pop())

print(q.isEmpty())