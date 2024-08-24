# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:31:31 2024

@author: Administrator
"""

print("=========MENU========")
print("1.Hu tieu")
print("2.Chao long")
print("3.Banh canh")
print("4.Bun rieu")
print("5.Pho bo")
print("======================")
ban=int(input("moi ban nhap lua chon:" ))
if ban==1:
    print("Hu tieu")
elif ban==2:
    print("Chao long")
elif ban==3:
    print("Banh canh")
elif ban==4:
    print("Bun rieu")
elif ban==5:
    print("Pho bo")
else:
        print("khong co lua chon trong menu")