# 146. LRU Cache
# Medium
# Topics
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 


 # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]


HashMap ={}
Tuple=()

# LRUCache= I create a object of size (n)
# size length of the listinside that 
#  ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# from collections import defaultdict

# Map=  [ [1,1], [2,2]]
# Usage=defaultdict{}

class LRU:

    def __init__(self,size):
        self.size=size 
        self.list1={}
        self.Frequencymap={}

    def put(self,element):

        if len(self.list1) >= self.size:
            self.CleartheQueue()    
        self.list1[element[0]]=element[1]


    def get(self,key):

        key1=key[0]
        if key1 not in self.Frequencymap:
            self.Frequencymap[key1]=1
        else:
            self.Frequencymap[key1]+=1
        return  self.list1[key1]


    def CleartheQueue(self):

        Array=  sorted(self.Frequencymap.items(),key=lambda x: x[1],reverse=False)
        keytoremove= Array[0][0]

        print(f'{Array=}  {keytoremove=}')

        self.list1.popitem()
        
  


LRU1= LRU(2)
LRU1.put([1, 1])
print(LRU1.list1)
LRU1.put([2, 2])
print(LRU1.list1)
print(LRU1.get([]))
print(LRU1.list1)
LRU1.put([3, 3])
print(LRU1.list1)




      