class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Linked_List:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def prepend(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self._size+=1
    
    def append(self,val):
        new_node = Node(val)
        
        if self.is_empty():
            self.head=new_node
        else:
            curr = self.head
            while curr.next:
                curr=curr.next
            curr.next = new_node
        self._size+=1

    def __str__(self):
        ans = ''
        curr = self.head
        while curr:
            ans = ans + str(curr.val) + ' -> '
            curr = curr.next
        ans+='None'
        return ans

    def search(self,value):
        curr = self.head
        while curr:
            if curr.val==value:
                return True
            curr = curr.next
        return False

    def insert_at(self,index,value):
        if index<1 or index>self._size+1 :
            return
        elif index==1:
            self.prepend(value)
        elif index == self._size+1:
            self.append(value)
        else:
            new_node = Node(value)
            i = 1
            curr = self.head
            while i<index-1:
                curr =curr.next
                i+=1
            new_node.next = curr.next
            curr.next = new_node
            self._size+=1

    def remove_first(self):
        if self._size>=1:
            ans = self.head.val
            self.head = self.head.next
            self._size-=1
            return ans

    def remove_at(self,index):
        if index<1 or index>self._size:
            return
        elif index==1:
            self.remove_first()
        elif index == self._size:
            self.del_last()
        else:
            curr = self.head
            i = 1
            while i<index-1:
                curr = curr.next
                i+=1
            curr.next = curr.next.next

            self._size-=1


    def delete_by_value(self,value):
        if self._size == 0:
            return
        elif self.head.val==value:
            self.remove_first()
        else:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.val == value:
                    prev.next = curr.next
                    self._size-=1
                    return
                prev = curr
                curr = curr.next

    def del_last(self):
        if self._size==0:
            return
        elif self._size ==1:
            self.head=None
        else:
            curr = self.head
            while curr.next.next:
                curr=curr.next
            curr.next=None
        self._size-=1

    def reverse(self):
        if self._size<=1:
            return
        
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

class Stack:
    def __init__(self):
        self.ll = Linked_List()

    def __len__(self):
        return len(self.ll)

    def isEmpty(self):
        return len(self.ll)==0

    def push(self,n):
        self.ll.prepend(n)

    def pop(self):
        if self.isEmpty():
            return None
        return self.ll.remove_first()

    def top(self):
        if not self.isEmpty():
            return None 
        return self.ll.head.val

st = Stack()
for i in range(10):
    st.push(i)

while not st.isEmpty():
    print(st.pop())