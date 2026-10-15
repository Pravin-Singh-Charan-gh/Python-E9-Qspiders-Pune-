from collections import deque

q = deque()
for i in range(10):
    q.append(i)

while len(q):
    print(q[0])
    q.popleft()