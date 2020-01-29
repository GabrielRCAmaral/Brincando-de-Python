n =int(input())
while(n):
    space_num=len(str(pow(4,n-1)))
    space=''
    for x in range(1,space_num):
        space+=' '
    for i in range(0,n):
        for y in range(0,n):
            if(i!=n-1 or y!=n-1):
                print ('%s%i' %(space,pow(2,i+y))),
            else:
                print ('%s%i' %(space,pow(2,i+y)))
        if(i!=n-1 or y!=n-1):
            print ('')
    print('')
        
    n=int(input())

