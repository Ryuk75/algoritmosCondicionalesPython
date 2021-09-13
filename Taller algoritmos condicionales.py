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
print("")

# 2. En un supermercado se hace una promoción, mediante la
#cual el cliente obtiene un descuento dependiendo de un
#número que se escoge al azar. Si el número escogido es
#menor que 74 el descuento es del 15% sobre el total de la
#compra, si es mayor o igual a 74 el descuento es del 20%. #Obtener cuanto dinero se le descuenta.
print("2/ Cuanto dinero se le descuenta a un cliente")
totalCompra = int(input("Ingrese el monto total de la compra: "))
numeroAzar = int(input("Ingrese el numero escogido al azar: "))
descuentoA = 0.15
descuentoB = 0.2
if (numeroAzar < 74):
    descuentoTotal = totalCompra * descuentoA
elif (numeroAzar >= 74):
    descuentoTotal = totalCompra * descuentoB
print("El descuento total de la compra es: ",descuentoTotal)
print("")

# 3. Una compañía de seguros está abriendo un departamento
#de finanzas y estableció un programa para captar clientes,
#que consiste en lo siguiente: Si el monto por el que se
#efectúa la fianza es menor que $50.000 la cuota a pagar
#será por el 3% del monto, y si el monto es mayor que
#$50.000 la cuota a pagar será el 2% del monto. La
#afianzadora desea determinar cual será la cuota que debe
#pagar al cliente.
print("3/ Cual es la cuota que debe pagar el cliente")
montoSolicitado = int(input("Ingrese el monto a pedir: "))
fianzaA = 0.03
fianzaB = 0.02
if (montoSolicitado < 50000):
    total = montoSolicitado + (montoSolicitado*fianzaA)
elif (montoSolicitado >= 50000):
    total = montoSolicitado + (montoSolicitado*fianzaB)
print("La cuota a pagar al cliente es: ",total)
print("")