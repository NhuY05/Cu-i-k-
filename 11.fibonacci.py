# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:14:47 2024

@author: Vivobook
"""

    
def question_11(n: int) -> int:
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for i in range(2,n+1):
            a,b=b, a+b
        return b
print(question_11(5))
print(question_11(10))