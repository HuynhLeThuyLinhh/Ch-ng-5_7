# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:31:34 2024

@author: DELL
"""

import math
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    if hinh == "vuong":
        canh = args[0];
        return 4*canh if pheptinh == "chuvi" else canh**2
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2* (dai+rong) if pheptinh == "chuvi" else dai*rong
    elif hinh == "tron":
        bankinh = args[0]
        return 2 * math.pi * bankinh if pheptinh == "chuvi" else math.pi* bankinh **2
    else:
        return "hình không hợp lệ"
if __name__=="__main__":
    print("chu vi hình vuông: ", chuvi_dt('vuong', 'chuvi',3))
    print("diện tích hình vuông: ", chuvi_dt('vuong', 'dientich',3))
    print("chu vi hình chữ nhật: ", chuvi_dt('chunhat', 'chuvi',3,4))
    print("diện tích hình chữ nhật: ", chuvi_dt('chunhat', 'dientich',3,4))
    print("chu vi hình tròn: ", chuvi_dt('tron', 'chuvi',3))
    print("chu vi hình tròn: ", chuvi_dt('tron', 'dientich',3))