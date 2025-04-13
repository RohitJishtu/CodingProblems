# 56. Merge Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 


intervals =  [[1,4],[2,7],[8,10],[15,18]]
output=[]

# if second element of current batch > first element of newbatch & second is less than second of new  , we merge 
# elif : second element of current batch is greater tahn both , then we continue to next batch 
# else :we append previous interval as is  

def make_intervals_merge(intervals,output=None ):

    if output is None :
       output=[] 
    prev_first =None 
    prev_second =None 

    for interval in range(len(intervals)):

        curr_first=intervals[interval][0]
        curr_second=intervals[interval][1]

        print(f'{curr_first} {curr_second}')

        if interval==0:
            prev_first=curr_first
            prev_second=curr_second
            continue 

        elif prev_second >= curr_first and prev_second <= curr_second:
            # we merge 
           output.append([prev_first,curr_second])
           prev_first =prev_first
           prev_second =curr_second 
        
        elif prev_second > curr_second:
            continue
        
        else:
            output.append([curr_first,curr_second])
            prev_first =curr_first
            prev_second =curr_second 
    return output

print(make_intervals_merge(intervals))