# head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []



class Node:
    def __init__(self,data=None,next=None):

        self.data=data 
        self.next=next 
        


class LinkedList:

    def __init__(self,head=None):
        if head==None:
            self.head=None
        else:
            self.head=Node(head) 

    def append_into_list(self,element:int):
        if self.head :
            # print('head exists')
            curr=self.head 
            while curr.next:
                curr=curr.next 
            curr.next = Node(element)
            return 
        else:
            # print('making head')
            self.head=Node(element)
        # print('inserted ',element)
        return 

    def print_list(self):
        curr=self.head
        while curr.next:
            print(curr.data)
            curr=curr.next
        return 
    
    def reverse_list(self,Entirelist='yes'):

        curr=self.head 
        prev=Node(None)
        next=curr.next

        while curr.next:
            next=curr.next
            curr.next=prev 
            prev=curr
            curr=next
  

        curr.next=None 
        self.head=prev
        print(f' {self.head.data=} ')


        return  self.head



head= [1, 2, 3,  4,  5 ]

LL1 = LinkedList()
for elements in head:
   LL1.append_into_list(elements)
# LL1.print_list()


LL1.reverse_list()
print(LL1.print_list())

