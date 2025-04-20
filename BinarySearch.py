# 162. Find Peak Element
# Medium

# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.



# Start this from 2 sides 
# brute force 

# for first one we check only 1 

# Iterate through the array :
# prev=None . n-1 < len
# n , n-1 , prev 

# for the last one we check only 1 

nums1 =[1,2,1,3,5,6,4]
Output1= 5

nums2 = [1,2,3,1]
Output2= 2

def find_peak_element(nums):

    left = 0 
    right = len(nums)-1
    
    while left <= right:

        mid = (left+right)//2
        if mid+1 < len(nums)-1:
            if nums[mid] < nums[mid+1]:
                left=mid+1 
            else:
                right=mid-1 
        else:
            if nums[mid] > nums[mid-1]:
                    left=mid-1 
            else:
                right=mid+1 
    
    return nums[left]


print(find_peak_element(nums1))