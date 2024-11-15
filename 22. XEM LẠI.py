# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:34:19 2024

@author: Vivobook
"""

from typing import List

def question_22(nums: list[int]) -> None:
    ds=[]
    for i in nums:
        if i!=0:
            ds.append(i)
    so0=len(nums)-len(ds)
    for i in range(so0):
        ds.append(0)
    return ds
print(question_22([0, 1, 0, 3, 12]))

def question_22(nums: list[int]) -> None:
    ds=[]
    for i in nums:
        if i!=0:
            ds.append(i)
    so0=len(nums)-len(ds)
    for i in range(so0):
        ds.append(0)
















