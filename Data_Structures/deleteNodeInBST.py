class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def deleteNode(self, root, key):
        def recursion(self, root, key):
            # get the replacement from Right node
            # Left

            # Right

            # Found!
            if root.val == key:
                # 1. NO child
                if root.left == None and root.right == None:
                    root = None
                # 2. One child child
                elif root.right and root.left == None:
                    root = root.right

                elif root.left and root.right == None:
                    root = root.left

                else:
                    temp = None
                    if root.left.right:
                        temp = root.left.right
                    root = root.left

    def replaceWithP(self, curr, r_node): 
        # Reached to the predecessor
        if curr.right == None:
            r_node.val = curr.val
            return curr.left
        else:
            curr.right = self.replaceWithP(curr.right, r_node)
            return curr
            