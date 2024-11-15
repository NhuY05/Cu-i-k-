# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:14:50 2024

@author: Vivobook
"""
from typing import Optional
def question_20() -> Optional[str]:
    optional=input("Nhập: ")
    if optional=="":
        return None
    elif optional:
        return optional
print(question_20())
    
