list1=[1,2,3,4]


# I need all possible combinations 
# [
# 1,2,3,4
# 1,2,3 
# 1,2
# 1
# 2,
# 2,3
# 2,3,4
# 3
# 3,4
# 4
# ]
# Approach :

# I start from 1 : go to the list and generate combinatioms 
# then again reoeat with 2 



list1=[1,2,3,4]
def Combinations(nums):
    result=[]
    def backtrack(start,path):

        if path:
            result.append(path[:])
            print(f'result is {result=}')

        for item in range(start,len(nums)):
            path.append(nums[item])
            backtrack(item+1,path)
            path.pop()


    backtrack(0,[])
    return result


print(Combinations(list1))

