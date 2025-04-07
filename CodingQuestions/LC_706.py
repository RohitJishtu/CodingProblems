# 706. Design HashMap
# Easy
# Topics
# Companies
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# # int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# Example 1:

InputCode =["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
InputValue= [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

class MyHashMap:

    def __init__(self,hashlist=None):
        self.hashlist=hashlist
        if self.hashlist is None:
            self.hashlist=[]

    def put(self, key: int, value: int) -> None:

        if len(self.hashlist)>1:
            for occurance in self.hashlist:
                if key ==occurance[0]:
                    occurance=key,value
                else:
                    self.hashlist.append([key,value])
        else:
            self.hashlist.append([key,value])

    def get(self, key: int) -> int:
        for occurance in self.hashlist:
            # print(f'{occurance=},{key=}')
            if key ==occurance[0]:
                return occurance[1]

    def displayHishlist(self):

        print(self.hashlist)



    def remove(self, key: int) -> None:
        
        for occurance in self.hashlist:
            print(f'{occurance=},{key=}')
            if key ==occurance[0]:
               self.hashlist.remove(occurance)


        return self.hashlist




InputCode =["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
InputValue= [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]



for commands in range(len(InputCode)):

    if InputCode[commands]=='MyHashMap':
        print('We are in MyHashMap')
        myHashMap = MyHashMap()
    
    elif InputCode[commands]=='put':
        print('We are in put')
        value=InputValue[commands]

        print(myHashMap.put(value[0],value[1]))
        myHashMap.displayHishlist()

    elif InputCode[commands]=='get':
        print('We are in get')
        value=InputValue[commands]
        print(myHashMap.get(value[0]))
        myHashMap.displayHishlist()
        
    elif InputCode[commands]=='remove':

        print('We are in remove')
        key=InputValue[commands]
        print(myHashMap.remove(key[0]))
        myHashMap.displayHishlist()


