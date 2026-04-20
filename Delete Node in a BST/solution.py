class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            temp = self.find_min(root.right)

            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)
        return root

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
        
