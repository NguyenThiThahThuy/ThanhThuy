# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:54:26 2024

@author: Nguyễn Thị Thanh Thùy 
"""
while True:
  try:
    so_thuc = float(input("Nhập vào một số thực: "))
    if -89.9 <= so_thuc <= 88.8:
      print("Giá trị bạn nhập hợp lệ.")
      break  # Thoát khỏi vòng lặp nếu giá trị hợp lệ
    else:
      print("Giá trị không hợp lệ. Vui lòng nhập lại.")
  except ValueError:
    print("Đó không phải là một số thực. Vui lòng nhập lại.")
