# Runtime 2027 ms Beats 5.07%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        li = []
        temp = head
        while temp is not None:
            if temp in li:
                return True
            li.append(temp)
            temp = temp.next 
        return False
    
# <<<----------------------------------------------------------------------------------------------------->>>

# Runtime 39 ms Beats 46.05%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False 
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True