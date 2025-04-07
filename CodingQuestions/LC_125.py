# 125. Valid Palindrome
# Solved
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.




# left >  compare   (len)
# right >            (zero) [l <right ]

# if match > move ahead in both 
# l+=1
# r-=1

# if l special char l+=1 , keep right as is 
# vice versa  

set1 = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5'}



s=" "
def Finding_plaindrome(s):

    left=0       #0
    right=len(s)-1  #9

    while left <right:
        
        if s[left].lower() in set1:

            if s[right].lower() in set1:

                if s[left].lower()!=s[right].lower():
                    return False 
                else:
                    left+=1
                    right-=1
            else:
                right-=1
        else:
            left+=1

    return True 

print(Finding_plaindrome(s))

# complexity : 
# time:O(n)
# Space : O(1)


