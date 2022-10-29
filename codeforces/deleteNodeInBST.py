class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def deleteNode(self, root, key):
        def recursion(self, root, key):
            if root.val == key:
                if root.right:
                    temp = root.right
                    l = root.left
                    root = root.right
                    root.left = l

                else:
                    temp = None
                    if root.left.right:
                        temp = root.left.right
                    root = root.left