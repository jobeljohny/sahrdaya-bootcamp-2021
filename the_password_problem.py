def check(x,y):
    
    n=len(x)
    m=len(y)
    if(n!=m):
        return False
    for i in range(n):
        if(x[i]!=y[n-1-i]):
            return False
    return True

n=int(input())
passwords=[]
for i in range(n):
    passwords.append(input())

for i in range(n-1):
    for j in range(i+1,n):
        if(check(passwords[i],passwords[j])):               
            w=passwords[i]
            l=len(w)
            print(l,w[l//2])
