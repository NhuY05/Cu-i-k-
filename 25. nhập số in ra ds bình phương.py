# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:09:11 2024

@author: Vivobook
"""

   
def question_25(nums: list[int]) -> list[int]:
   
    
    binhphuong= [x ** 2 for x in nums]
    binhphuong.sort()
    return binhphuong
print(question_25([-4, -1, 0, 3, 10]))  