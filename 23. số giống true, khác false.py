# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:23:39 2024

@author: Vivobook
"""

def question_23(nums: list[int]) -> bool:
    dathay=set()
    for i in nums:
        if i in dathay:
            return True
        dathay.add(i)
    return False

   
print(question_23([1,2,3,1]))
    



