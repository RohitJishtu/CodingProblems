
# Code
# Testcase
# Test Result
# Test Result
# 217. Contains Duplicate
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false



input= [1,2,3,1]

def find_duplicates1(input):   
    if len(input)==len(set(input)):
        return False 
    return True 

# Complexity 
# Time:O(n)
# Space: O(n)




def find_duplicates2(input):   
    set1=set()

    for element in input:
        if element in set1:
            return True 
        else:
            set1.add(element)

    return False 

# Complexity 
# Time:O(n)
# Space: O(n)


def find_duplicates3(input):   
    input.sort()   #merge sort nlogn

    for incr in range(len(input)-1):
        if input[incr]==input[incr+1]:
            return True 

    return False 

# Complexity 
# Time:O(n)
# Space: O(n)

print(find_duplicates3(input))
print(find_duplicates2(input))




