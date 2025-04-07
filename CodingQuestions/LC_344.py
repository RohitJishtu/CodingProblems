# 344. Reverse String
# Easy
# Topics
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]



word = "par_marth"
s=list(word)
def Reverse_Array(s):
    mid=len(s)//2
    last=len(s)-1
    for iter in range(mid):
        s[iter],s[last]=s[last],s[iter]
        last -= 1
    return s 

print(Reverse_Array(s))