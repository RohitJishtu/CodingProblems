# LeetCode Question: Moving Average from Data Stream
# Problem Statement:
# Given a stream of integers and a window size k, implement a class MovingAverage that calculates the moving average of the last k elements in the stream.
# Implement the class:
# MovingAverage(int size): Initializes the object with the window size size.
# double next(int val): Returns the moving average of the last k numbers after inserting the new value val.
# Example 1 :
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output 
# [null, 1.0, 5.5, 4.67, 6.0]


# MovingAverage m = new MovingAverage(3);
# m.next(1);   // Returns 1.0  -> [1]
# m.next(10);  // Returns 5.5  -> [1, 10]
# m.next(3);   // Returns 4.67 -> [1, 10, 3]
# m.next(5);   // Returns 6.0  -> [10, 3, 5] (1 is removed)

Input = [[3], [1], [10], [3], [5]]
from queue import deque 
class MovingAverages:

    def __init__(self,bucket,newlist=deque()):
        self.bucket= bucket
        self.list=newlist

    def GiveMovingAvg(self):
        count=0
        sum=0
        print('reached GiveMovingAvg ', self.list)
        for elemnt in self.list:
            sum+= elemnt
            count+=1
            print(f'{sum=}{count=}')
        return sum/count
    
    def AppendInBucker(self,element):
        print('reached AppendInBucker ', self.list)
        if len( self.list) < self.bucket:
            self.list.append(element)
        else:
            self.list.popleft()
            self.list.append(element)
        return self.list

    def next(self,next):
        self.AppendInBucker(next)
        average =self.GiveMovingAvg()
        print(f'{average=}')
        return average



MVG1=MovingAverages(3)
MVG1.next(1)
MVG1.next(10)
MVG1.next(12)
MVG1.next(11)




