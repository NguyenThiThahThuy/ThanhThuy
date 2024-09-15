# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:06:30 2024

@author: Nguyễn Thị Thanh Thùy 
"""

danh_sach = []
for so in range(2018, 2829):
    
     if so % 2 == 0 and so % 5 == 0:
        danh_sach.append(so)

print("Danh sách các số chẵn chia hết cho 5 từ 2018 đến 2828:")
print(danh_sach)