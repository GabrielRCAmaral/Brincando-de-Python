import math
a=1
while(a):
    dados=raw_input().split()
    if(int(dados[0])):
        a,b,c=map(int,dados)
        print '%i'%math.sqrt((a*b/(c/100.0)))
    else:
        a=0