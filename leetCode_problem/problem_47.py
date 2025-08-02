# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()
        temp = head
        if temp is not None:
            while temp is not None:
                q.append(temp)
                temp = temp.next
        if head is None:
            return None
        else:
            head = q.pop()
            nt = head
            while len(q):
                nt.next = q.pop()
                nt = nt.next
                nt.next = None
            return head