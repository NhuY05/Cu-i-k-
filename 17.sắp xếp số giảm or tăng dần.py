# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:21:04 2024

@author: Vivobook
"""
import random

    

def question_17(n: int) -> list:
    ds=[random.randint(1,100) for _ in range(n)]
    ds.sort(reverse=True)
    return ds
print(question_17(5))














