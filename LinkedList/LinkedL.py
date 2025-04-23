# 2. Add Two Numbers


# Output: [7,0,8]





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

    def printlist(self):

        cur=self.head
        while cur:
            print(cur.data,end=" -> ")
            cur=cur.next
        print() 

    def reverse_list(self):

        head=self.head
        prev=None 
        cur=head
        next=cur.next 
        while next:
            next=cur.next 
            cur.next=prev
            prev=cur
            cur=next
        self.head=prev

    def FIND_NTH(self,NTH):

        head=self.head 
        slow=fast=head
        for i in range(NTH):
            fast=fast.next 
        while fast.next:
            slow=slow.next
            fast=fast.next
        print(f'{slow.data}\n')

    
    def RemoveNode(self,N):
        curr=self.head 
        counter=0
        while curr.next:
            counter+=1 
            next=curr.next
            if counter==N:
                prev.next=next
                print(f'removing {curr.data=}')
                return 
            prev=curr
            curr=curr.next
        if counter <N :
           print('it exceeds the length of the list')

    def InsertAtEnd(self,value):
        curr=self.head 
        while curr.next:
            curr=curr.next
        curr.next=Node(value)

    def InsertAtBeg(self,value):
        newNode=Node(value)
        curr=self.head 
        newNode.next=curr
        self.head=newNode

Output= [7, 0, 8, 9, 1, 2,  6]

Node1=Node(7)
Node2=Node(0)
Node3=Node(8)
Node4=Node(9)
Node5=Node(1)
Node6=Node(2)
Node7=Node(6)

LL1=LinkedList(Node1)
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
Node4.next=Node5
Node5.next=Node6
Node6.next=Node7

LL1.printlist()
LL1.reverse_list()
LL1.printlist()
print('After Reverse')
LL1.FIND_NTH(2)
LL1.RemoveNode(4)
# Remove 8 from list 
LL1.printlist()

LL1.InsertAtEnd(11)
LL1.printlist()
LL1.InsertAtBeg(3)
LL1.printlist()
