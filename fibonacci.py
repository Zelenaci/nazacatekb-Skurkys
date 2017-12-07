# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:20:54 2017

@author: Skurkys
"""

k = int(input("Kolik čísel posloupnosti se má tisknout? > "))
x = 0
y = 1
z = 0
for z in range(k):
    z = x + y
    y = x
    x = z
print(z)