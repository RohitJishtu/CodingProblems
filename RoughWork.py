# Question
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example, Given [[0, 30],[5, 10],[15, 20]], return 2.


    #  > Arrange them 

    #  > Start ,end  when ever I iterate to first > I mark the Meeting room as 1 
    #  > I go to second , I check the start of second , compare it with end of first >
    #         if its greater > I keep room as 1 
    #         else : I need onre room , room goes to 2 
    #         I need minimum of end time now fpr next comparison 
    #  > I go to next : 
    #         repeat setp 2 


data= [[0,30],  
        [5,10], 
        [15,20], 
        [18,35],
        [19,35],
        [21,35] 
        ]

def required_meeting_rooms(data):
    data.sort(key=lambda x:x[0])
    prev_start=data[0][0]
    prev_end=data[0][1] 
    occupied_rooms=1
    max_needed=1

    for one_meeting in range(1,len(data)):

        curr_start=data[one_meeting][0]
        curr_end=data[one_meeting][1]

        if curr_start < prev_end:
            occupied_rooms+=1 
        else:
            occupied_rooms-=1
        if prev_end > curr_start:
            prev_end= min(curr_end,prev_end)
        max_needed=max(occupied_rooms,max_needed)

        print(f'{max_needed=} {occupied_rooms=} {prev_end=} {curr_start=}')
    return max_needed

print(required_meeting_rooms(data))