# 53. Maximum Subarray
# Attempted
# Medium
# Topics
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 



# iterate through the lements 
# Sum  =  0 
# Maxum() Store Start and End of array as well
# New element > Sum with new element , then you restart the array 

nums = [2, -1, -2, 5, -1, 2, -1, 2]

Output = 6
def find_subarray_largest_sum(nums):
    result={}
    currsum=0
    maxsum=-999

    start=0
    end =0 
    for seq in range(len(nums)):

        currsum+=nums[seq]
        if currsum < nums[seq]:
           currsum=nums[seq]
           start=seq

        if currsum > maxsum:
           maxsum=currsum
           end=seq

        print(f'{currsum=} {maxsum=} {start=} {end=}')
    return maxsum

print(find_subarray_largest_sum(nums))