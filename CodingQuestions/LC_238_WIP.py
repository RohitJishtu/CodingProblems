# 238. Product of Array Except Self
# Medium
# Topics
# Companies
# Hint


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# # Approach 
# product(all) =  24
# when element =1 , 24/1 =24 
# element 2 , 24/2 =12 .......


# [1,2,3,4]

# None(1)*24 

# 1*12

# 2*4

# 6*None(1)





nums = [1,2,3,4]
def product_byiteself(nums,output=None):
    
    if output==None:
        output=[]
    zeroexists=False
    productall=1
    
    if len(nums)==1:
        return nums[0]
    
    for element in nums:
        if element==0:
            zeroexists=True
            element=1
        productall= element*productall
        print(f'{productall=}')

    for element in nums:

        if zeroexists==True and element !=0:
            output.append(0)
        else:
            output.append(productall/element)

    return output
print(product_byiteself(nums))

# Complexity 
# Time : o(n)+o(n)
# Space : o(1)

