def iSpalindrome(s,n):
    for i in range(n//2):
        if(s[i]!=s[n-i-1]):
            return False
        else:
            return True

def minCost(s,ac,bc):
    
    totCost=0
    n=len(s)
    if(('/' not in s) and iSpalindrome(s,n) is False):
        return -1
    m=min(ac,bc)
    r=s[::-1]
    for i in range(n):
        if(r[i]=='/'):
            if(s[i]=='a'):
                totCost+=ac
            elif(s[i]=='b'):
                totCost+=bc
            else:
                totCost+=m
        elif(s[i]!=r[i] and s[i]!='/'):
            return -1
    
    return totCost
