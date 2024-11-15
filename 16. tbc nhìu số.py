# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:07:18 2024

@author: Vivobook
"""




def question_16(arg) -> float:
    if not arg:
        return None
    tong=sum(arg)
    tbc=tong/len(arg)
    return tbc
print(question_16([1,2,3,4,5]))
print(question_16([]))




