# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]
# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Input_keys=["MovingAverage", "next", "next", "next", "next"]
Input_Values  =[[3], [1], [10], [3], [5]]


from collections import deque 

class MovinGAverage:

    def __init__(self,size,sum=0,count=0):
        self.size=size
        self.TempStore=deque() 
        self.sum=sum
        self.count=count

    def next_avg(self, Input_value):
        remove_el=None
        length= self.size
        print(f'before {self.TempStore=} {self.size=} {remove_el=} {len(self.TempStore)=}')

        if len(self.TempStore) < length:
            self.TempStore.append(Input_value)
            self.sum += Input_value
            self.count += 1
        else:
            print('reaching else ')
            remove_el=self.TempStore.popleft()
            self.sum -= remove_el
            self.count -= 1
            self.TempStore.append(Input_value)
            self.sum += Input_value
            self.count += 1

        print(f'After {self.TempStore=} {self.size=} {remove_el=}')
        return self.sum/self.count


Input_keys=["MovingAverage", "next", "next", "next", "next"]
Input_Values  =[[3], [1], [10], [3], [5]]

for action_number in range(len(Input_keys)):
    print(f'calling with {Input_Values[action_number][0]} ')
    if Input_keys[action_number]=='MovingAverage':
        new_object=MovinGAverage(Input_Values[action_number][0])

    if Input_keys[action_number] =='next' and new_object:
        average = new_object.next_avg(Input_Values[action_number][0])
        print(f'average is {average}')


