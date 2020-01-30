while True:
    try:
        n=int(input())
        
    except EOFError:
        break
    print "vai ter %s!"%('duas'if(n) else 'copa')