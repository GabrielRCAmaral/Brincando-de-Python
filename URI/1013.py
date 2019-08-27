# -*- coding: utf-8 -*-
a,b,c=raw_input().split(" ")
a=int(a)
b=int(b)
c=int(c)
maiorAB=(a+b+abs(a-b))/2
maiorABC=(maiorAB+c+abs(maiorAB-c))/2
print("%i eh o maior" %maiorABC)
