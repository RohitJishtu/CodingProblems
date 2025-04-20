def get_power1(number,power):
    prd=1

    for i in range(power):
        prd=prd*number
        print(f'prodt is {prd=}')



def get_power2(number,power):
    prd=1

    if power <0:
       number=1/number
       power=abs(power)

    def backtrack(number,power):

        if power==1:
           return number
        if power%2==0:
            product = backtrack(number,power//2)*backtrack(number,power//2)
        else:
            product=backtrack(number,power//2)*backtrack(number,power//2)*number

        return product
    print(backtrack(number,power))

number =2
power=-2


print(get_power2(number,power))