meetings= [[0, 30], [5, 10], [31, 20]]


overlap= if first element of next is greater than first of second , post theuy are sorted  


def CanAttend_meetings(meetings):
    sorted(meetings,key=lambda x:x[0])
    canAttend=True
    if len(meetings)==0:
        return True 
    prev_first=meetings[0][0] 
    prev_last=meetings[0][1]

    for mtng in range(1,len(meetings)):

        curr_first=mtng[0]
        curr_last=mtng[1]

        if prev_last > curr_first:
            canAttend=False 
            return canAttend
    
    return canAttend

meetings= [[0, 30], [5, 10], [21, 25]]
# How many rooms are required 
# [0:Start > 5:start >10:End  >> 21 Start > 25 :End  > 30 End ]
# CREATE A list oiut of 2 d list 
# CombinedList=[]
# for item in meeting:
#     CombinedList.(item[0],'Start')
#     CombinedList.(item[1],'End')

# CombinedList.sorted(key=0)

# for NewItem in CombineList:
#     if Newitem[1]='Start'
#         Add ameeting room 
#     else:
#         remove room 


meetings= [[0, 30], [5, 10], [21, 25]]


# record[0]
# prev_start =0 
# prev_end=30 
# heapq.pushheap(heap,record[1,0])
#     0,30   [30,0]
#     5,10   [10,5]
# curr_start=5 
# curre_end=10 

import heapq
def Max_meeting_rooms_required(meetings):
    room=1
    heap=[]
    prev_start=meetings[0]
    prev_end=meetings[1]
    heapq.pushheap(heap,prev_end)

    for mtng in range(1, len(meetings))

        curr_start=meetings[mtng][0]
        curr_end=meetings[mtng][1]

        if curr_star < prev_end:
            heapq.pushheap(heap,curr_end)
            room+=1 

        else:
            prev_end=heapq.heappop()
            room-=1

    return room