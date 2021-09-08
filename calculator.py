# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:56:41 2021

@author: ÖZGE
"""

def hesapla(a,b,islem):
    if islem not in "+-*/":
        return "Lütfen geçerli bir işlem giriniz: +-*/"
    if islem=="+":
        return (str(a)+" + "+str(b)+" = "+str(a+b))
    if islem=="-":
        return (str(a)+" - "+str(b)+" = "+str(a-b))
    if islem=="*":
        return (str(a)+" * "+str(b)+" = "+str(a*b))
    if islem=="/":
        return (str(a)+" / "+str(b)+" = "+str(a/b))
    
while True:
    try:
        a=int(input("İlk sayıyı giriniz: "))
        b=int(input("İkinci sayıyı giriniz: "))
        islem=input("İşleminizi seçiniz: +-*/")
        print(hesapla(a,b,islem))
    except:
        print("Lütfen sayıları uygun formatta giriniz")
        
        
        
        
        
        
        
        
        