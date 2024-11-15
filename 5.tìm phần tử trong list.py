# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:39:23 2024

@author: Vivobook

"""


def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    else:
        return None
if __name__=="__main__":
    lst=[1,2,3,4,5]
    print(question_5(lst, 5))
    
def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    else:
        return None
print(question_5([1,2,3,4,5], 3))
print(question_5([10,20,30,40], 25))
    


    
    
