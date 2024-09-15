# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:20:07 2024

@author: Nguyễn Thị Thanh Thùy 
"""
n = int(input("Nhập giá trị nguyên n: "))
result_dict = {i: i ** i for i in range(1, n + 1)}
print(result_dict)

