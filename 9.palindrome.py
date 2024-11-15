# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:27:56 2024

@author: Vivobook
"""
import re

def question_9(s: str) -> bool:
    s=re.sub("[^a-zA-Z]","",s.lower())
    if s==s[::-1]:
        return True
    elif s !=s[::-1]:
        return False

print(question_9("A man, a plan, a canal: Panama"))











    
