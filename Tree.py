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

# def LevelOrderTraversal(root):
#     Q1=deque()
#     if root is None:
#         return 
#     Q1.append(root)
#     Treemap={}
#     level=1

#     while len(Q1)>0:
#         print(f'reached part 1 {Q1=}')
#         Node=Q1.popleft()
#         if Node is None:
#             return 
#         if level not in Treemap:
#             Treemap[level]=[Node.val]
#         else:
#             Treemap[level].append(Node.val)
#         print(f'reached part 1 {Treemap=}')

#         if root.left:
#             Q1.append(Node.left)
#             child+=1
#         if root.right:
#             Q1.append(Node.right)
#             child+=1
#             level+=1

#     return Treemap


    #         4 

    #     8        5

    # 0      1  None    6 


# def AverageofTree(root,output=[]):

#     if root is None:
#         return 0, 0 ,output
    
#     left_sum,left_count,output=AverageofTree(root.left,output)
#     right_sum,right_count,output=AverageofTree(root.right,output)

#     value=root.val

#     curr_sum=left_sum+right_sum+root.val
#     count=left_count+right_count+1

#     if value==curr_sum//count:
#         output.append(value)
    
#     return curr_sum,count,output

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build binary tree from level-order list"""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def printTree_inOrder(root):
    """Prints tree nodes in in-order traversal"""
    if root is None:
        return
    printTree_inOrder(root.left)
    print(root.val)
    printTree_inOrder(root.right)

def printTree_PreOrder(root):
    """Prints tree nodes in in-order traversal"""
    if root is None:
        return
    print(root.val)
    printTree_PreOrder(root.left)
    printTree_PreOrder(root.right)
   

def find_depth_Tree(root):
    """Finds depth of tree"""
    if root is None:
        return 0
    return max(find_depth_Tree(root.left), find_depth_Tree(root.right)) + 1


def AverageofTree(root):
    """Returns list of nodes whose value == avg of subtree (int division)"""
    def dfs(node):
        if not node:
            return 0, 0, []
        
        left_sum, left_count, left_output = dfs(node.left)
        right_sum, right_count, right_output = dfs(node.right)
        
        curr_sum = left_sum + right_sum + node.val
        count = left_count + right_count + 1
        output = left_output + right_output

        if node.val == curr_sum // count:
            output.append(node.val)

        return curr_sum, count, output

    _, _, result = dfs(root)
    return result
from collections import deque



def find_debth_tree_level_order(root):
    TreeQ=deque()
    TreeQ.append(root)
    level=0
    while len(TreeQ)>0:
        level+=1
        length= len(TreeQ)
        print(f'{level=} {length=}')
        for elements in range(length):
            Node=TreeQ.popleft()
            if Node.left:
                TreeQ.append(Node.left)
            if Node.right:
                TreeQ.append(Node.right)
    return level 

def find_sumroot(root):
    
    if root is None :
        return 0 , 0 

    ret1,cnt1 = find_sumroot(root.left)
    ret2,cnt2 = find_sumroot(root.right)
    sum= root.val+ret1+ret2
    count= 1 +cnt1+cnt2

    # print(f' left side {find_sumroot (root.left)=}')
    # print(f' ride side {find_sumroot (root.right)=}')
    
    return sum,count



def find_max_path(root):
    
    if root is None:
        return 0 ,0

    leftdebt,rightdebt= find_max_path(root.left),find_max_path(root.right)

    # Path = (leftdebt-1) + (rightdebt -1)
    print(f'{leftdebt=} {rightdebt=}')

    return leftdebt+1, rightdebt+1

# ------------------------------
# Test

#     1
#    / \
#   2   3
#  /     \
# 4       5

#      1
#    /  \
#   2    3
#  / \   
# 4   5   

# print("In-order Traversal:")
# printTree_PreOrder(root)  # Optional: just to visualize tree
# print("\nTree Depth:", find_depth_Tree(root))
# # print("\nTree Depth Level order:", find_debth_tree_level_order(root))
# # print("Average of Subtree Nodes:", AverageofTree(root))
# print("\nTree Path:", find_max_path(root))
# find_max_path

# Test with the example
# values = [3, 9, 20, 4, 11,15,7,22,24,55,71]
# values=[4,8,5,0,1,None,6]
# root = build_tree(values)

# you are given a tree 
# values = [3, 9, 20, 4, 11, 15, 7,22,24,55,71]
# Q1 :Write print Tree Function s1


#                 3 

#     9                   20

# 15    7           4           11


# print(find_debth_Tree(root))

# values = [1, 2, 3, 4, None, None ,5]
#     1
#    / \
#   2   3
#  /     \
# 4       5


# ------------------------------------------------------------------------------------------------------------------------
# 129. Sum Root to Leaf Numbers
# ------------------------------------------------------------------------------------------------------------------------


# Medium
# Topics
# Companies
# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:


# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.



values = [1,2,3,None,5,null,4]
root = build_tree(values)

print("Pre-order Traversal:")
printTree_PreOrder(root)  # Optional: just to visualize tree


#     1
#    / \
#   2   3
#  /     \
# 4       5




def find_Concat_sumroot(root):
    
    if root is None :
        return '' ,'',0 

    ret1,_,sum_root= find_Concat_sumroot(root.left)
    ret2,_,sum_root= find_Concat_sumroot(root.right)

    print(f'{root.val=} {ret1=} {ret2=} ')

    conc_left = str(root.val)+str(ret1)
    conc_right = str(root.val)+str(ret2)

    print(f'{conc_left=} {conc_right=} ')

    sum_root = int(conc_left)+ int(conc_right)

    print(f'{conc_left=} {conc_right=} {sum_root=}')
    
    return conc_left,conc_right,sum_root

# print(f' DFS = {find_sumroot(root)} ')
# print(f' DFS = {find_Concat_sumroot(root)} ')
# Input: root = [1,2,3,null,5,null,4]
# print(f'find_Concat_sumroot=  {find_Concat_sumroot(root)}')

        

def find_rightside(root,output=[]):

    if root is None:
        return 
    output.append(root.val)
    if root.right:
        find_rightside(root.right,output)
    else:
        find_rightside(root.left,output)

    # print(output)
    return output

print(f'DFS output {find_rightside(root)=}')


def find_rightside_bfs(root,output=[]):    
    Q1=deque()
    Q1.append(root)
    while Q1:
        length= len(Q1)
        for i in range(length):
            Node=Q1.popleft()
            if i==(length-1):
               output.append(Node.val)   
            if Node.left:
                Q1.append(Node.left)
            if Node.right:
                Q1.append(Node.right)
    print(f'BFS {output=} ')
   

print(f'before  {find_rightside_bfs(root)}')



def switch_tree(root):   

    if root is None:
        return 

    root.left,root.right=root.right,root.left 
    switch_tree(root.left)
    switch_tree(root.right)
    
    return  

switch_tree(root)
find_rightside_bfs(root)

    
   

