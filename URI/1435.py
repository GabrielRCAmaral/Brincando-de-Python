n=1

def gera(linha,coluna,tam):
    if(linha-0<=tam-linha):
		if(coluna-0<=linha-0):
			return coluna-0+1
		elif (tam-coluna<=linha-0):
			return tam-coluna+1
		else:
			return linha-0+1
    if(linha-0>tam-linha):
	    if(coluna-0<=tam-linha):
		    return coluna-0+1
	    elif(tam-coluna<=tam-linha):
		    return tam-coluna+1
	    else:
		    return tam-linha+1
            
while(n):
    n=int(input())
    for i in range(n):
        print " ",
        for y in range(n):
            if(y==n-1):
               print gera(i,y,n-1)
            else:
               print gera(i,y,n-1),' ',

        
  
