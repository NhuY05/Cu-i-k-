# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:05:51 2024

@author: Vivobook
n
"""
import random
def question2(n: int) -> (int, float):
    songaunhien=[random.randint(1,100) for _ in range(n)]
    tong=sum(songaunhien)
    trungbinh = float(tong/n)
    return tong, trungbinh
if __name__=="__main__":
    n=int(input("Nhập n: "))
    while n<1 or n>1000:
        n=int(input("Nhập lại: "))
        
    print(question2(n))
def question_2(n: int) -> (int, float):
    songaunhien=[random.randint(1,100) for _ in range(n)]
    tong=sum(songaunhien)
    tbc=sum/n
    return tong, tbc
print(question2(5))
print(question2(10))