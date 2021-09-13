# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:53:05 2021

@author: ricar
"""

#Taller de algoritmos condicionales

# 1.Hacer un algoritmo que calcule el total a pagar por la
#compra de camisas. Si se compran tres camisas o mas se
#aplica un descuento del 30% sobre el total de la compra 
#y si son menos de tres camisas un descuento del 10%.
print("1/ Total a pagar por compra de camisas")
cantCamisas = int(input("Ingrese numero de camisas vendidas: "))
precioCamisas = int(input("Ingrese precio de las camisas: "))
valorDesc = 0.3
if (cantCamisas > 0 and cantCamisas >= 3):
    descuento = int((cantCamisas * precioCamisas)* valorDesc)
    total = (cantCamisas * precioCamisas)-descuento
elif (cantCamisas < 3):
    total = (cantCamisas*precioCamisas)
else:
    print("Ingrese un numero mayor que 0")
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
if (numeroAzar > 0 and numeroAzar < 74):
    descuentoTotal = totalCompra * descuentoA
elif (numeroAzar >= 74):
    descuentoTotal = totalCompra * descuentoB
else:
    print("Ingrese un numero mayor que 0")
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
if (montoSolicitado > 0 and montoSolicitado < 50000):
    total = montoSolicitado + (montoSolicitado*fianzaA)
elif (montoSolicitado >= 50000):
    total = montoSolicitado + (montoSolicitado*fianzaB)
else:
    print("Ingrese un numero mayor que 0")
print("La cuota a pagar al cliente es: ",total)
print("")

# 4. Una fábrica ha sido sometida a un programa de control
#de contaminación para lo cual se efectúa una revisión de
#los puntos de contaminación generados por la fábrica. El
#programa de control de contaminación consiste en medir los
#puntos que emite la fábrica en cinco días de una semana y
#si el promedio es superior a los 170 puntos entonces
#tendrá la sanción de parar su producción por una semana y
#una multa del 50% de las ganancias diarias cuando no se
#detiene la producción. Si el promedio obtenido de puntos
#es de 170 o menos entonces no tendrá ni sanción ni multa.
#El dueño de la fábrica desea saber cuanto dinero perderá
#después de ser sometido a la revisión.
print("4/ Cuanto dinero perdera la fabrica despues de la revision")
multa = 0.5
aux = 0
dineroProduccion = 0
for i in range(5):
    dineroProduccion += int(input(f"Ingrese cuanto dinero gano la fabrica el dia {i+1}: $"))
    aux += int(input(f"Ingrese los puntos de contaminacion generados el dia {i+1}: "))
prom = aux/5
if (prom > 0 and prom > 170):
    totalPerdida = dineroProduccion * multa
elif (prom <= 170):
    totalPerdida = 0
else:
    print("Ingrese un numero mayor que 0")
print(f"La fabrica perdio ${totalPerdida} despues de la revision")
print("")

# 5.Una persona se encuentra con un problema de comprar un
#automóvil o un terreno, los cuales cuestan exactamente lo
#mismo. Sabe que mientras el automóvil se devalúa, con el
#terreno sucede lo contrario. Esta persona comprará el
#automóvil si al cabo de tres años la devaluación de este
#no es mayor que la mitad del incremento del valor del
#terreno. Ayúdale a esta persona a determinar si debe o no
#comprar el automóvil. 
print("5/ Determinar si debe o no comprar el automovil")
precioCarro = int(input("Ingrese el precio del Carro: "))
precioTerreno = int(input("Ingrese el precio del Terreno: "))
incrementoAnual = int(input("Ingrese el porcentaje de incremento anual del terreno: "))
devaluacionAnual = int(input("Ingrese el porcentaje de devaluacion anual del carro: "))
incremento = ((precioTerreno * incrementoAnual)/ 100)*3
decremento = ((precioCarro * devaluacionAnual)/100)*3
if (incremento/2 > decremento):
    print("Debe comprar el automovil")
else:
    print("No debe comprar el automovil")
print("")

# 6. En una fábrica de computadoras se planea ofrecer a
#los clientes un descuento que dependerá del número de
#computadoreas que compre. Si las computadoras son menos
#de cinco se les dará un 10% de descuento sobre el total
#de la compra; si el número de computadoras es mayor o
#igual a cinco pero menos de diez se le otorga un 20% de
#descuento; y si son 10 o más se les da un 40%. El
#precio de cada computadora es de $11.000.
print("6/ Descuento de los computadores")
valorUnitario = 11000
cantComputador = int(input("Ingrese la cantidad de computadores: "))
if (cantComputador > 0 and cantComputador < 5):
    valorT = valorUnitario * cantComputador
    descuentoT = valorT * 0.1
    totalP = valorT - descuentoT
elif (cantComputador >= 5 and cantComputador < 10):
    valorT = valorUnitario * cantComputador
    descuentoT = valorT * 0.2
    totalP = valorT - descuentoT
elif (cantComputador >= 10):
    valorT = valorUnitario * cantComputador
    descuentoT = valorT * 0.4
    totalP = valorT - descuentoT
else:
    print("Ingrese un numero mayor que 0")
print(f"El descuento es de ${descuentoT}, el total a pagar es ${totalP}")
print("")

# 7.Un proveedor de estéreos ofrece un descuento del 10%
#sobre el precio sin IVA, de algún aparato si este cuesta
#$2000 o más. Además, independientemente de esto, ofrece
#un 5% de descuento si la marca es NOSY. Determinar cuanto
#pagará, con IVA incluido, un cliente cualquiera por la
#compra de su aparato. IVA es del 16%.
print("7/ Determinar cuanto pagara con IVA incluido")
precioEstereo = int(input("Ingrese el precio del estereo: "))
marcaEstereo = input("Ingrese el nombre de la marca del estereo: ")
iva = 0.16
if(precioEstereo >= 2000):
    if(marcaEstereo == 'nosy' or marcaEstereo == 'Nosy' or marcaEstereo == 'NOSY'):
        descEstereo = (precioEstereo*0.15)
    else:
        descEstereo = (precioEstereo*0.1)
    subtotal = precioEstereo - descEstereo
    totalE = subtotal + (subtotal*iva)
elif(precioEstereo > 0 and precioEstereo < 2000):
    totalE = precioEstereo + (precioEstereo*iva)
else:
    print("Ingrese un numero mayor que 0")
print(f"El precio total a pagar por el estereo es: ${totalE}")
print("")

# 8.Una empresa quiere hacer una compra de varias piezas
#de la misma clase a una fábrica de refacciones. La
#empresa, dependiendo del monto total de la compra,
#decidirá que hacer para pagar al fabricante. Si el monto
#total de la compra excede de $500.000 la empresa tendrá
#la capacidad de invertir de su propio dinero un 55% del
#monto de la compra, pedir prestado al banco un 30% y el
#resto lo pagará solicitando un crédito al fabricante. Si
#el monto total de la compra no excede de $500.00 la
#empresa tendrá capacidad de invertir de su propio dinero
#un 70% y el restante 30% lo pagará solicitando crédito
#al fabricante. El fabricante cobra por concepto de
#interes un 20% sobre la cantidad que se le pague a
#crédito. Obtener la cantidad a inverir, valor del
#préstamo, valor del crédito y los intereses.
print("8/ Obtener la cantidad a invertir, valor del préstamo, valor del crédito y los intereses.")
cantidadI = int(input("Ingrese la cantidad a invertir: "))
if cantidadI > 500000:
    inversion = (cantidadI * 0.55)
    prestamo = (cantidadI * 0.3)
    prestamoFabrica = (cantidadI *0.15)
    interes = (prestamoFabrica * 0.2)
    print(f"La cantidad a invertir es ${inversion}")
    print(f"La cantidad a prestamo al banco es ${prestamo}")
    print(f"El prestamo a la fabrica es ${prestamoFabrica}")
    print(f"Los intereses son: ${interes}")
elif cantidadI <= 500000:
    inversion = (cantidadI * 0.7)
    prestamoFabrica = (cantidadI *0.3)
    interes = (prestamoFabrica * 0.2)
    print(f"La cantidad a invertir es ${inversion}")
    print(f"El prestamo a la fabrica es ${prestamoFabrica}")
    print(f"Los intereses son: ${interes}")
print("")

# 9. Leer 2 números; si son iguales que lo multiplique, si
#el primero es mayor que el segundo que los reste y sino
#que los sume.
print("9/ Lea 2 numeros y haga operaciones entre ellos")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
if (n1 == n2):
    resultado = n1 * n2
elif (n1 > n2):
    resultado = n1 - n2
elif (n1 < n2):
    resultado = n1 + n2
print("El resultado es: ",resultado)
print("")

# 10. Leer tres números diferentes e imprimir el número
#mayor de los tres
print("10/ Lea tres numeros diferentes e imprima el mayor")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
if (n1 > n3 and n1 > n2):
    print(f"El numero mayor es el {n1}")
elif (n2 > n3 and n2 > n1):
    print(f"El numero mayor es el {n2}")
elif (n3 > n2 and n3 > n1):
    print(f"El numero mayor es el {n3}")
else:
    print("Todos los numeros son iguales.")