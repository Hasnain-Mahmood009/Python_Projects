# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        temp = head
        li = []
        if temp.next is not None:
            while temp is not None:
                li.append(temp.val)
                temp = temp.next
        
        if li == li[::-1]:
            return True
        return False