# 647. Palindromic Substrings
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.
# give more examples 

# Example 3:
# Input: s = "racecar"
# Output: 10
# Explanation:
# Palindromic substrings are:

# "r", "a", "c", "e", "c", "a", "r" (single letters)

# "cec", "aceca", "racecar" (multi-letter palindromes)
# Total = 7 + 3 = 10



# len=len(s)
# r > start counting :1 
# first=r , last =r , plain=1 
# first=r , second=a , plain =0 
# first =r >>>>keep on checking for every element 
# a = keep on checking for every elemnt 
# c keep on checking 
s = "racecar"
output=10 

def get_string_plaindrome_count(s,count=None):

    if count is None :
        count=0

    def plaindromecheck(s):
        first=0
        last=len(s)-1
        while last > first:
            if s[first]!=s[last]:
               return False 
            else:
                first+=1
                last-=1
        return True 

    s = "racecar"
    def backtrack(s,count):
        element=[]
        for sequence in range(len(s)):
            element.append(s[sequence])
            if plaindromecheck(element):
               count+=1
            backtrack(s[sequence:],count)
        return 
    
    backtrack(s,count)

print(get_string_plaindrome_count(s))

# Complexity : Time 
# s = "racecar"
# output=10 
# r > n 
# Time :n(power)k
# Space :o(1)