# 49. Group Anagrams
# Medium
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]





# anagrams are the ones which will have same values and counts 
# # So for every work I ll make a map 
# and then if map is there I ll append 

# AllMaps={}
# map_word={e:1,a:1,t:1}

# AllMaps[map_word]=map_word


# templist=[]
# if map_word in AllMaps:
#     templist.append(map_word)


# AllMaps = { {e:1,a:1,t:1}:'eat', {e:1,a:1,t:1}: 'tea'......... }
strs = ["eat","tea","tan","ate","nat","bat"]
out=[["bat"],["nat","tan"],["ate","eat","tea"]]


from collections import Counter

AllMaps={}
def get_group_anagrams(strs):

    for word in strs:
        map_word=frozenset(Counter(word))

        if map_word in AllMaps:
            AllMaps[map_word].extend([word])
        else:
            AllMaps[map_word]=[word]

    return AllMaps.values()

print(get_group_anagrams(strs))