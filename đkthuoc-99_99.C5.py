# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:32:11 2024

@author: Nguyễn Thị Thanh Thùy 23704131
"""
while True:
    number = int(input("Nhập vào một số nguyên trong khoảng [-99; 99]: "))
    if -99 <= number <= 99:
        break
    else:
        print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")

print("Bạn đã nhập: ", number)
