class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Build tree from level order traversal array"""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def print_tree_iterative(root):
    """Print tree in pre-order traversal using iteration instead of recursion"""
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        print(node.val)
        
        # Push right first so left gets processed first (LIFO stack)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def max_depth(root):
    """Find maximum depth of binary tree"""
    if not root:
        return 0
    
    # Use BFS with a queue to find max depth
    queue = [(root, 1)]  # (node, depth)
    max_d = 0
    
    while queue:
        node, depth = queue.pop(0)
        max_d = max(max_d, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_d

# Test with the example
values = [3, 9, 20, None, None, 15, 7]
root = build_tree(values)

print("Tree in pre-order traversal (iterative):")
print_tree_iterative(root)

print("\nMaximum depth of the tree:", max_depth(root))