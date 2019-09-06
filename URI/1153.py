# -*- coding: utf-8 -*-
def fat(n):
    if n==1:
        return 1
    if not n:
        return 1
    return fat(n-1)*n
  
n=int(input())
print fat(n)