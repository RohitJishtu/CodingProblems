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


        #                             1 
                    
        #                 2                   3

        #         3           4           4  

        #     4      Nothing 

        # [1,2,3,4]  [1,2] [1,2,3]  [1,2,4]   [1,3,4] [1,3] [1]

list1=[1,2,3,4]

def combinations(list1):
    output=[]
    def backtrack(list1,index,temp):

        print(f'before {temp=} {output=}')
        if len(temp)>0:
            output.append(temp[:])

        for element in range(index,len(list1)):
            temp.append(list1[element])
            backtrack(list1,element+1,temp)
            temp.pop()
            
        return output

    backtrack(list1,0, [])


print(combinations(list1))

