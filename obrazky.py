# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:25:56 2017

@author: Skurkys
"""


   
def obrazek1(r):
    print()
    h = r
    while h > 0:
        print(h*"*")
        h -= 1

def obrazek2(r):
    m = r
    h = 1
    print()
    while m > 0:
        print(m*" " + h*"*")
        h += 2
        m -= 1

def obrazek3(r):
    print()
    h = 1
    polovina = r//2
    while r > polovina:
        print(h*"*")
        h += 1
        r -= 1
    while r >= 0:
        print(h*"*")
        h -= 1
        r -= 1
    

r = int(input(">>"))        
obrazek1(r)
obrazek2(r)
obrazek3(r)