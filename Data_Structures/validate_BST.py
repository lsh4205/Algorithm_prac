# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
class Solution:
    def recurs(self, curr, min, max):
        if curr == None:
            return True
        if curr.left:
            if curr.left.val >= curr.val or max <= curr.left.val or min >= curr.left.val:
                return False
        if curr.right:
            if curr.right.val <= curr.val or max <= curr.right.val or min >= curr.right.val:
                return False
        l = self.recurs(curr.left, min, curr.val)
        r = self.recurs(curr.right, curr.val, max)
        return l and r
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurs(root, -sys.maxsize, sys.maxsize)