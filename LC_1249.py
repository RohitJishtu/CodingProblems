# 1249. Minimum Remove to Make Valid Parentheses
# Medium
# Topics
# Companies
# Hint
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
# so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 





# list1 = opens  # Dictionary : location 
# list2 : closed 
# ( : Put it to a list1
# ) : Put it to the list2
# ) 1 needs to be removed         
# ) : Location iof this  



def get_valid_parenthesis(s):

    Brackets=[]
    deleteset=set()

    for char_number in range(len(s)):

        if s[char_number] == '(':
            Brackets.append(char_number)  

        elif s[char_number] == ')': 
            if len(Brackets)>0:
                Brackets.pop() 
            else:
                deleteset.add(char_number)  

    deleteset.updatede(Brackets
    result=""

    for char in range(len(s)):
        if char not in deleteset:
            result+=(s[char])
    return result




s1 = "))(("
Output1= ""

s2 = "lee(t(c)o)de)"
Output2= "lee(t(c)o)de"

s3 = "a)b(c)d"
Output3="ab(c)d"


print(get_valid_parenthesis(s1))

print(get_valid_parenthesis(s1)==Output1)
print(get_valid_parenthesis(s2)==Output2)
print(get_valid_parenthesis(s3)==Output3)