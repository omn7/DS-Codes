class ExprNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def construct_expression_tree(prefix):
    stack = []
    # Reverse the prefix expression for easier processing
    for char in prefix[::-1]:
        node = ExprNode(char)
        if not is_operator(char):
            stack.append(node)
        else:
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
    return stack[-1]

def postorder_non_recursive(root):
    stack = []
    output = []
    last_visited = None
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                output.append(peek.value)
                last_visited = stack.pop()
    print("Postorder traversal:", " ".join(output))

def delete_tree(root):
    if root:
        delete_tree(root.left)
        delete_tree(root.right)
        root.left = None
        root.right = None
        root.value = None

# Example usage
prefix_exp = "+--a*bc/def"
expr_tree_root = construct_expression_tree(prefix_exp)
postorder_non_recursive(expr_tree_root)
delete_tree(expr_tree_root)
