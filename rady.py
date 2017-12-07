# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:56:03 2017

@author: Skurkys
"""

import random
s = [random.randint(1,50) for i in range(20)] 

print(s)

print()

print("Sudá čísla jsou:")
for x in s:
    if x % 2 == 0:
        print(x, end= " ")
        
        
print()
print()


print("Čísla větší než 11 a menší než 19 jsou:")
for x in s:
    if x < 19:
        if x > 11:
            print(x, end= " ")
print()
print()


print("Čísla dělitelné 3 a 4 jsou:")
for x in s:
    if x % 3 == 0:
        if x % 4 == 0:
            print(x, end=" ")
            
print()
print()  
         
s2 = [random.randint(-50,50) for i in range(20)]         
print(s2)

print("Součet kladných čísel je:")
kladna = 0
for cislo in s2:
    if cislo > 0:
        kladna = kladna + cislo
print(kladna)

print()

print("Součet záporných čísel je:")
zaporna = 0
for cislo in s2:
    if cislo < 0:
        zaporna = zaporna + cislo
print(zaporna)

print()


mocniny = 0
for x in s2:
    mocniny += x**2
print("Součet druhých mocnin:", mocniny)


prumer = sum(s2)/len(s2)
print("Aritmetický průměr:", prumer)