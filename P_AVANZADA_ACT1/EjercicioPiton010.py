# -*- coding: utf-8 -*-
"""EjercicioPiton010.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ukFocdpO8yLRZhTTbRxAdN_VbCX0HGtS
"""

print('Doble factorial')
N=int(input("Ingresa el número entero positivo: "))

if N <= 0:
  print('El valor ingresado no es el pedido')
else:
  aux=1
  for i in range(N,0,-2):
    aux=i*aux
  print(f'El doble factorial de {N} es: {aux}')