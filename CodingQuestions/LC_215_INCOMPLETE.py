# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

 

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4





# Approach 2 : heapify the array - which puts minimum elements to top , 
# I ll negative the elemnts value and make min heap and extract data for 4th 


# Approach 3 : , take 1st assume it is highest , if you find another more than it , 
# add it to the list pos=1 , 
# else insert into the next pos
# insert only until 4th 
# push existing pos , 




# I ll add this list to heapify function , what it does is creates a min heap heap 


#         1
#     2           3 

# 4       5   6

# Then heappop is the operatio which takes the first min element , 
# now since this is highest so we multiple the elements with -ive sign 

# and then retrive kth number from min healp 

nums1 = [3,2,1,5,6,4] 


import heapq
def find_kth_largest_element(nums,k,Output=None):
 
    # heapq.heapify(nums)  # nums has been heapified  -6 at top 
    # Rather than heapifying all the elements we ll create a heap of length k 

    heap=[]
    for element in range(len(nums)):
        heapq.heappush(heap,nums[element])
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0],heap
    
nums = [3,2,3,1,2,4,5,5,6]
k = 4
# nums = [3,2,1,5,6,4]
# k = 2
print(find_kth_largest_element(nums,k))




