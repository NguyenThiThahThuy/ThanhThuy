# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:20:14 2024

@author: Nguyễn Thị Thanh Thùy  
"""
str_input = input("Nhập chuỗi: ")
length = len(str_input)
print(f"Độ dài của chuỗi: {length}")

special_chars = set("!@#$%^&*()-=+./")

special_count = 0
lower_count = 0
digit_count = 0
upper_count = 0
for char in str_input:
    if char in special_chars:
        special_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isupper():
        upper_count += 1
print(f"Số ký tự đặc biệt: {special_count}")
print(f"Số ký tự chữ cái từ a-z: {lower_count}")
print(f"Số ký tự chữ số từ 0-9: {digit_count}")
print(f"Số ký tự chữ cái hoa từ A-Z: {upper_count}")

