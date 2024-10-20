# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:26:33 2024

@author: DELL
"""

import random
a = random.randint(20, 30)
pt = [0] * a 
for i in range(a):
    so_t = random.uniform(18, 99)
    pt[i] = so_t ** 2
print("Số lượng phần tử: ", a)
print("Danh sách các giá trị bình phương:", pt)
