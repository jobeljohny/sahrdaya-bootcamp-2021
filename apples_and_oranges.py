def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    ac,bc=0,0
    for apple in apples:
        if(apple+a>=s and apple+a<=t):
            ac+=1
    for orange in oranges:
        if(orange+b>=s and orange+b<=t):
            bc+=1
    print(ac)
    print(bc)
