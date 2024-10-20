# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:13:43 2024

@author: DELL
"""
import math
def chuvi(hinh, *args, **kwargs):
    if hinh == "vuong":
        canh = args[0];
        return 4*canh
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2* (dai+rong)
    elif hinh == "tron":
        bankinh = args[0]
        return 2 * math.pi * bankinh
    else:
        return "hình không hợp lệ"
if __name__=="__main__":
    print("chu vi hình vuông: ", chuvi('vuong',3))
    print("chu vi hình chữ nhật: ", chuvi('chunhat',3,4))
    print("chu vi hình tròn: ", chuvi('tron',3))