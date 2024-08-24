# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:31:31 2024

@author: Administrator
"""
a=32**0.2-(1/64)**(-0.25)+(8/27)**(1/3)
print("ket qua la ",round(a,3))

import math 
a=float(input("nhap gia tri a: "))
b=float(input("nhap gia tri b: "))
c=(math.sqrt(a)-math.sqrt(b))/(a**(1/4)-b**(1/4))-(math.sqrt(a)+(a*b)**(1/4))/(a**(1/4)+b**(1/4))
print("ket qua la: ",c)
