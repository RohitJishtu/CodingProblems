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


temp= 1,1,2,6
n= [1,2,3,4]
out=[24,12,8,6]
def find_productexceptself(n,output=[]):

    product=1
    output=[[] for n in range(len(n))]
    output[0]=1 
    for iter in range(1,len(n)):
        product=product*n[iter-1]
        output[iter] = product
    print(output)
    product=1
    for iter2 in range(len(n)-2,-1,-1):
        product= product*n[iter2+1]
        output[iter2] *= product    
    print(output)

find_productexceptself(n,output=[])