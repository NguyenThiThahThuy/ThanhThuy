# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:20:16 2024

@author: Nguyễn Thị Thanh Thùy 
"""
import random
a=input("nguoi choi:" )
luachon = ["Kéo","Búa","Bao"]
b= random.choice(luachon)
print("may chon:", b)
if a==b:
    print("hoa")
elif a=="Kéo" and b=="Bao":
    print("nguoi choi thang")
elif a=="Búa" and b=="Kéo":
    print("nguoi choi thang")
elif a=="Bao" and b=="Búa":
    print("nguoi choi thang")
else:
    print("Nguoi may thang")
    