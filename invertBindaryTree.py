# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        
        if not head or not (head.left or head.right):
            return head
        
        temp = head.left
        head.left = head.right
        head.right = temp
        
        self.invertTree(head.right)
        self.invertTree(head.left)
        
        return head