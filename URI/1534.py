from __future__ import print_function
while True:
    try:
        n=int(input())
        for y in range(n):
            for j in range(n):
                imp=3
                if (j==y):
                    imp=1
                if(j==n-y-1):
                    imp=2
                print (imp,end='')
            print ('')
    except EOFError:
        break