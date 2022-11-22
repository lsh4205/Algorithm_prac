class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    kth = None
    def kthSmallest(self, root, k):
        global kth
        kth = root.val
        self.traverse(root, k)
        return kth
    def traverse(self, curr, k):
        global kth
        if curr == None:
            return 0
        if curr.left:
            c = 1 + self.traverse(curr.left, k)
            if c == k:
                kth = curr.val
            return c 
        if curr.right:
            c = 1 + self.traverse(curr.right, k)
            if c == k:
                kth = curr.val
            return c

    def convertToTree(self, arr):
        root = None
        for i, num in enumerate(arr):
            if i == 0:
                root = TreeNode(num)
                pass
            else: 
                if root.left == None:
                    root.left = TreeNode(num)
                    pass
                if root.right == None:
                    root.right = TreeNode(num)
                    pass
                