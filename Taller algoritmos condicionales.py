# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:53:05 2021

@author: ricar
"""

#Taller de algoritmos condicionales

# 1. Hacer un algoritmo que calcule el total a pagar por la
#compra de camisas. Si se compran tres camisas o mas se
#aplica un descuento del 30% sobre el total de la compra 
#y si son menos de tres camisas un descuento del 10%.
print("1/ Total a pagar por compra de camisas")
cantCamisas = int(input("Ingrese numero de camisas vendidas: "))
precioCamisas = int(input("Ingrese precio de las camisas: "))
valorDesc = 0.3
if (cantCamisas >= 3):
    descuento = int((cantCamisas * precioCamisas)* valorDesc)
    total = (cantCamisas * precioCamisas)-descuento
elif (cantCamisas < 3):
    total = (cantCamisas*precioCamisas)
print("El total a pagar es: ",total)