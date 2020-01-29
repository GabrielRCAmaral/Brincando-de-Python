while True:
    try:
        n=int(input())
        print "vai ter %s!"%('duas'if(n) else 'copa')
    except EOFError:
        break