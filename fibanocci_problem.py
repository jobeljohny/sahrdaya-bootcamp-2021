def getNthFibanocci(N):
    
    # first two terms
    n1, n2 = 0, 1
    count = 0
    # if there is only one term, return n1
    if N == 1:
       return n1
    # generate fibonacci sequence
    else:
       while count < N-1:
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
           
    return n1

def getNthFib(n):
    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    else:
        return(getNthFib(n-1) + getNthFib(n-2))

n=10
for i in range(1,n+1):
    #x = getNthFibanocci(i)
    x = getNthFib(i)
    print(str(i)+".",x)
