# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 00:19:17 2024

@author: Vivobook
Viết một hàm để kiểm tra xem một số nguyên được nhập vào có phải là số chẵn hay không.
Trả về True nếu số đó là số chẵn, và False nếu là số lẻ.
Chữ ký hàm
Đầu vào
Đầu ra
Ví dụ
Ví dụ 1:
Giải thích: 4 là số chẵn.
Ví dụ 2:
Một số nguyên n .
Trả về True nếu n là số chẵn.
Trả về False nếu n là số lẻ.
"""


    
def question_4(n: int) -> bool:

    if n%2==0:
        return True
    elif n%2!=0:
        return False
print(question_4(4))
print(question_4(7))
    
    
    
    
    
    
    
    
    
    

    
        