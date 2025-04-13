# 268. Missing Number
# Easy
# Topics
# Companies
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

nums = [3,0,1]

# 0 to n numbers , if we find a number missing , we report that 

# Sequence 
# 0 to len()= 3

# 0  then if 0 exists : Move forward 
# 1: then if 1 exists : Move forward 
# 2: doesnt exist , print 2 
# 2: exists , list ends , then I putput counter+1 


# if i am in zero position i find 3 
#     So Insert nums[3]= what I found 
#     nums[0]= 1 # what was at 3 

# next position I find 0 
#     nums[0]=0
#     num[1]= 1  # what was at zeo 

# next position I find 1
#     nums[1]=1
#     num[2]= 2 , what was at 1 

#     if num[2]==2:
#         else : 2 is the missing num 

nums = [9,6,4,2,3,5,7,0,1]


def find_missing_number(nums):
    i=0
    while i<len(nums):
        if nums[i]!= i and nums[i] < len(nums):
            nums[nums[i]], nums[i]=nums[i],nums[nums[i]]
        else:
            i+=1
        print(nums)

print(find_missing_number(nums))