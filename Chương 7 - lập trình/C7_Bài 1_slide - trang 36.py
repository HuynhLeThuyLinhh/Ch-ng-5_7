# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:04:27 2024

@author: DELL
"""
def tinhtong(*args, **kwargs):
    return sum(args)
def tinh_tich(*args, **kwargs):
    tich = 1
    for i in args:
        tich *= i
    return tich
    
if __name__=="__main__":
        ds = [1,2,3,4,5]
        print(tinhtong(*ds))
        print(tinh_tich(*ds))
        