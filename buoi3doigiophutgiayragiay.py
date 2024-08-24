# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:57:47 2024

@author: Administrator
"""
h=int(input("nhap so gio: "))
p=int(input("nhap so phut: "))
g=int(input("nhap so giay: "))
if h>24 or p>60 or g>60 :
    print("khong the tinh ket qua, nhap lai gio phut giay")
else: 
    x=h*3600+p*60+g;
    print("gio phut giay doi ra giay la: ",x)
