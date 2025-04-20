# 528. Random Pick with Weight
# Medium
# Topics
# Companies
# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

# Example 1:

# Input  
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
# Example 2:

# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed.
# All of the following outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......





# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Creating Object and array 

# How do we pick random number 

import random

class Solution:

    def __init__(self,list1=[]):
        self.list1=list1
        self.sum_l=sum(list1)

    def pickindex(self):
        indexlist=list(range(len(self.list1)))
        weights=[]
        for item in self.list1:
            weights.append(item/self.sum_l)
        return random.choices(indexlist,weights=weights,k=1)

    @staticmethod
    def main():

        output=[]
        Input_Action=["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
        Input_Val=[[[1,3]],[],[],[],[],[]]

        for one_input in range(len(Input_Action)):

            if Input_Action[one_input]=='Solution':
                print(f'making OBJECT now with {Input_Val[one_input]=}')
                Obj1=Solution(Input_Val[one_input][0])
                output.append(None)
            if Input_Action[one_input]=='pickIndex':
                output.append(Obj1.pickindex())    

        print(output)



Solution.main()