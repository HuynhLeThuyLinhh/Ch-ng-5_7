# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:23:01 2024

@author: DELL
"""

n=int(input("Số nguyên dương n: "))
giai_thua=1
for i in range(1,n+1):
    giai_thua *= i
print("S=n!=",giai_thua)
