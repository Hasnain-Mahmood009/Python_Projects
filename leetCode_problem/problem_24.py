# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return(
                p.val == q.val and
                check(p.left,q.right) and
                check(p.right,q.left)
            )
        return check(root.left,root.right)