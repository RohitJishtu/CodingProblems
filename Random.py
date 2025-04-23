

import heapq
import queue


'''------------------------------------------------------------------------------------------------------------------
# Queue 
---------------------------------------------------------------------------------------'''

#Queue 

# Q1=queue.deque()
# Stack1=list()
# Q1.append(1)
# Q1.append(3)
# Q1.append(5)
# Stack1.append(1)
# Stack1.append(3)
# Stack1.append(5)
# # print('Queue',Q1)
# # print('Stack',Stack1)
# # Q1.pop()
# # Stack1.pop()
# # print('Queue',Q1)
# # print('Stack',Stack1)
# # Q1.popleft()
# # Stack1.pop()


# print('Queue',Q1)
# print('Stack',Stack1)


#  
'''------------------------------------------------------------------------------------------------------------------
# Heap 
---------------------------------------------------------------------------------------'''


# Stack1=[]

# heapq.heappush(Stack1,4)
# print('print',Stack1)
# heapq.heappush(Stack1,0)
# print('print',Stack1)
# heapq.heappush(Stack1,1)
# print('print',Stack1)
# # print('pop',heapq.heappop(Stack1))
# # print('pop',heapq.heappop(Stack1))


'''------------------------------------------------------------------------------------------------------------------
# ZIP 
---------------------------------------------------------------------------------------'''


# Stack1=[1,2,3]
# stack2=[11,12,13]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

# for element1, element2 in zip(l1,l2):
#     print(element1,element2)


# from itertools import zip_longest

# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]

# for element1, element2 in zip_longest(l1, l2, fillvalue=0):
#     print(element1, element2)

'''------------------------------------------------------------------------------------------------------------------
# MOD 
---------------------------------------------------------------------------------------'''


# print(10%9)


# lis1 =[1,2,3,4,-1]
# result=9

# window=3
# sum=0
# maxum=0   
# count=1
# start=0
# for element in range(len(lis1)):


#     if count <=3:
#         sum=sum+lis1[element]         
#         count+=1     
#     else:
#         sum-=sum-lis1[start]    
#         start+=1  
#         sum=+sum+list[element]

#     maxum=max(sum,maxum)  


'''------------------------------------------------------------------------------------------------------------------
# Sorting 2 d arrays and Dictionary  
---------------------------------------------------------------------------------------'''

# array=[[1,2],[3,4],[2,3],[4,1]]
# print(f'Unsorted {array=}')

# array.sort(key=lambda x:x[0])
# print(f'Sorted on key 0 {array=}')

# array.sort(key=lambda x:x[1])
# print(f'Sorted on key 1 {array=}')



'''------------------------------------------------------------------------------------------------------------------
# Sorting 2 d Empty Lists 
---------------------------------------------------------------------------------------'''

from collections import deque
Q1=deque()

Q1.append(1)
Q1.pop()
List1=[1]
List1.pop()
Dict={}
Dict[1]=2
if Dict:
    print(f'{len(Dict)=} esists')
