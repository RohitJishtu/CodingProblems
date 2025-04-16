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


def printTree_inOrder(root):

    if root is None:
        return 

    printTree_inOrder(root.left)
    print(root.val)
    printTree_inOrder(root.right)
    


def find_debth_Tree(root):
    if root is None:
        return 0
    return max(find_debth_Tree(root.left),find_debth_Tree(root.right))+1

from collections import deque

def LevelOrderTraversal(root):
    Q1=deque()
    if root is None:
        return 
    Q1.append(root)
    Treemap={}
    level=1

    while len(Q1)>0:
        print(f'reached part 1 {Q1=}')
        Node=Q1.popleft()
        if Node is None:
            return 
        if level not in Treemap:
            Treemap[level]=[Node.val]
        else:
            Treemap[level].append(Node.val)
        print(f'reached part 1 {Treemap=}')

        if root.left:
            Q1.append(Node.left)
            child+=1
        if root.right:
            Q1.append(Node.right)
            child+=1
            level+=1

    return Treemap



# Test with the example
values = [3, 9, 20, 4, 11,15,7,22,24,55,71]
root = build_tree(values)
# you are given a tree 
# values = [3, 9, 20, 4, 11, 15, 7,22,24,55,71]
# Q1 :Write print Tree Function s1


#                 3 

#     9                   20

# 15    7           4           11


# print(find_debth_Tree(root))

printTree_inOrder(root)
LevelOrderTraversal(root)