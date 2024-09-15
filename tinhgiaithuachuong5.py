# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 03:22:53 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
def tinh_giai_thua(n):
    giai_thua = 1  
    for i in range(1, n + 1):  
        giai_thua *= i  
    return giai_thua 


try:
    n = int(input("Nhập một số nguyên dương n: "))
    if n < 0:
        print("Vui lòng nhập số nguyên dương!")
    else:
        ket_qua = tinh_giai_thua(n)
        print(f"Giai thừa của {n} là: {ket_qua}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
