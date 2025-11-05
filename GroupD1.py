class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.val = []

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key< root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    