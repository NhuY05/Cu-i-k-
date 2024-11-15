# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:23:43 2024

@author: Vivobook
"""
from typing import List
from collections import Counter
def question_31(paragraph: str, n: int) -> List[str]:
    tu=paragraph.lower().split()
    tongsotu=len(tu)
    solanxh= Counter(tu)
    ketqua = [tuxuathien for tuxuathien, solan in solanxh.items() if solan / tongsotu > 0.2]
    return ketqua[:n]
if __name__=="__main__":
    print(question_31("apple apple banana orange orange apple", 2))
    
    