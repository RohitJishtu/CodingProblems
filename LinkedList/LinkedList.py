# 2. Add Two Numbers
# Medium
# Topics
# Companies

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:
# Input: 
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]





class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next 


class LinkedList:

    def __init__(self,head=None):
        self.head=head


    def InsertintoList(self,node):

        if self.head:
           curr=self.head
           while curr.next:
                curr=curr.next
           curr.next=node

        else:
            self.head= node

    def make_newlist_by_adding(self,e1,e2,carry=0):
        
        if (e1+e2) >9:
            data=(e1+e2)%10
        else:
            data=e1+e2+carry
        if self.head:
            curr=self.head
            while curr.next:
                curr=curr.next 
            
            curr.next=Node(data)
        else:
            self.head=Node(e1+e2)
        return 

    def printlist(self):

        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
        return 

l1 = [2,4,3] 
l2 = [5,6,4]
output=[7,0,8]


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# [8,9,9,9,0,0,0,1]

LL1=LinkedList()
LL2=LinkedList()
LL3=LinkedList()


def pass_elements(e1,e2,carry=0):
    if (e1+e2)>9 :
        carry = (e1+e2)%9
    return e1,e2,carry


from itertools import zip_longest
# Insertion into one List 
oldcarry=0
for element1,element2 in  zip_longest(l1,l2,fillvalue=0):

    e1,e2,carry=pass_elements(element1,element2)
    if carry>0:
        oldcarry=carry
        carry=0
    else:
        carry=oldcarry
        oldcarry=0
    LL1.InsertintoList(Node(e1))
    LL2.InsertintoList(Node(2))

    print(f'called by {element1=} {element2=} {carry=} {oldcarry=}')

    LL3.make_newlist_by_adding(element1,element2,carry)

LL3.printlist()




