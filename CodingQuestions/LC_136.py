
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

 
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1


# Space = Same 
# Time= O(n)


nums = [4,1,2,1,2,4,7]

# 4:1 
# 1:1  1:None 
# 2:1  2:None  

storagemap={}
def FindSingleElement(nums,storagemap):

    for iter in range(len(nums)):
        if nums[iter] not in storagemap:
            storagemap[nums[iter]]=1 
        else:
            storagemap[nums[iter]]=None 

    # {4:1,1:None,2:None }

    for key,value in storagemap.items():
        if value is not None:
            return key

# Time: o(n+m) 
# Space : o(m) 

print(FindSingleElement(nums,storagemap))