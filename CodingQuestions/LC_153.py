# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 


nums =   [1,2,3,4,5]

# nums = [4,5,6,7,8,1,2]
# 7 > right > move right  
# 7 < left  > move left 
# until 
# 7 < right and 7 < left 

def finding_minimum_elemnent(nums):

    left=0
    right=len(nums)-1

    if len(nums)==1 or nums[0]<=nums[right]:
        print('result was idetified here')
        return nums[0]

    while left <=right:
        mid = (left+right)//2
        
        # print(f'{left=} {right=} {mid=}')
        if nums[mid] <= nums[mid+1] and nums[mid] <= nums[mid-1]:
            return nums[mid] 

        elif (nums[mid] >nums[right] ) :
            left=mid+1

        else  :
            right=mid-1

    return None 

print(finding_minimum_elemnent(nums))

# Complexity :
# Time: O(logn)
# Space: O(1)