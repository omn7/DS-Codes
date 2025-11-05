class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

   
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root

bst = BST()
root = None
root = bst.insert(root, 50)
root = bst.insert(root, 30)
root = bst.insert(root, 20)
root = bst.insert(root, 40)
root = bst.insert(root, 70)
root = bst.insert(root, 60)
root = bst.insert(root, 80)

print("Inorder traversal:")
bst.inorder(root)
print("\nDeleting 20")
root = bst.deleteNode(root, 20)
print("Inorder traversal after deletion:")
bst.inorder(root)
