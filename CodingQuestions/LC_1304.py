# 1304. Find N Unique Integers Sum up to Zero


def UniqueInt_SumZero(limit):
    result=[]

    if limit%2!=0 or limit==1: 
        print('Entered in loop1 ')
        result.append(0)
        if limit==1:
            return result 
      
    for element in range(1,(limit//2)+1):
        result.extend([element,-element])
    return result

n=3
print(UniqueInt_SumZero(n))
