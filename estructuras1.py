# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    
x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
    

while True:
    x=input("Enter a number to count to: ")
    
    if x==´q´ or x==´quit´:
        break
    x=int(x)
    y=1

    while True:
        print(y)
        y=y+1
        if y>x:
            break