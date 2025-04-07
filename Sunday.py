# 152. Maximum Product Subarray
# Medium
# Topics
# Companies
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


nums= [2,3,-2,4]

# If we go by Combination Sum , n>k 
# 2*3 =6 
# 3*-2*4 =-24
# 2*3*-1 =-6
# 2*3*-2*4 = -48


# 2 * 3 , start=0 , end=1    [Dictionary 6:[1,2] ] maxproduct=6 
# 6 * -2 -12 
# prodyct1 =

# start +=1 
# newproduct =

# if newproduct >oldproduct < takenew product 



def find_subarray(nums):
    final_start=0
    final_end=1 
    start=0
    product=1 
    newproduct=1 
    maxproduct=-999

    if len(nums)==1:
        final_start=0
        final_end=0
        return nums[0]

    if len(nums)==0:
        return None


# nums= [-2,-3,-4]

    for elements in range(len(nums)):
       
        if elements<len(nums)-1:
            newproduct = nums[elements]*nums[elements+1]

        product= product*nums[elements]

        if newproduct <= product:  
     
            if maxproduct<product:
                maxproduct=product 
                final_start= start
                final_end=elements 

        else:
           
           maxproduct=newproduct
           start= elements
           final_start=start
           final_end=elements+1

    
    return final_start,final_end,maxproduct


print(find_subarray(nums))


# Complexity : 

# Time : O(n)
# Space : o(1)