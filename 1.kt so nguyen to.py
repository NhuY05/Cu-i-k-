# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:43:39 2024

@author: Vivobook
Bạn được cung cấp một số nguyên dương n . Viết một hàm để xác định xem n có phải là
số nguyên tố hay không.
Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
Chữ ký hàm
Đầu vào
Đầu ra
Một số nguyên n (1 ≤ n ≤ 10^9).
Trả về True nếu n là số nguyên tố, ngược lại trả về False .
"""



def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(question_1(11))

def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%2==0:
            return False
    return True
print(question_1(11))
print(question_1(4))












