# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:52:46 2024

@author: Vivobook
"""

  
def question_24(nums: list[int]) -> int:  
    
   
    dem=0
    phantuxh=None
    for i in nums:
        if dem==0:
            phantuxh=i
        elif i == phantuxh:
            dem+=1
    return phantuxh
   
print(question_24([3,2,3]))

   
            

