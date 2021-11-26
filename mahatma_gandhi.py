valid=['0','1','8']
def pal(s):
    n=len(s)
    if(not n%2==0):
        if(not s[n//2] in valid):
            return False
    for i in range(n//2):
        if(s[i] not in valid):
            return False
        if(not s[i]==s[n-1-i]):
            return False
    return True
n=int(input())
nums=[]
for _ in range(n):
    nums.append(input())

for i in nums:
    if(pal(i)):
        print("YES")
    else:
        print("NO")
