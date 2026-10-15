# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st = set()
        curr1, curr2= headA, headB
        while curr1 and curr2:
            if curr1 in st:
                return curr1
            st.add(curr1)
            curr1 = curr1.next
            if curr2 in st:
                return curr2
            st.add(curr2)
            curr2 = curr2.next

        curr = curr1 if curr1 else curr2

        while curr:
            if curr in st:
                return  curr
            curr = curr.next
        return None