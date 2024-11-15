# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:47:18 2024

@author: Vivobook
"""

import collections
def question_26(s: str) -> int:
    sotu = collections.Counter(s)
    dodai = sum(so // 2 * 2 for so in sotu.values())
    return dodai + (1 if any(so % 2 == 1 for so in sotu.values()) else 0)
print(question_26("abccccdd"))
