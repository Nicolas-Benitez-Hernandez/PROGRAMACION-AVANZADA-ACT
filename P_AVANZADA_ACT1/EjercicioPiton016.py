# -*- coding: utf-8 -*-
"""EjercicioPiton016.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uSnFVRfZq-NW1BDjSkHJuR1JLELYGN7N
"""

print('Números narcisistas dentro de un intervalo')
nUno=int(input("Ingresa el valor menor del intervalo: "))
nDos=int(input("Ingresa el valor mayor del intervalo: "))
print('')

if (nUno <= 0) or (nDos <= 0) or (nUno>nDos):
  print('El valor ingresado no es el pedido')
else:

  valores=[]
  for i in range(nUno,nDos+1,1):
    suma=0
    iStr=str(i)
    iTamaño=len(iStr)
    iList=[j for j in iStr]
    for k in range(0,iTamaño,1):
      valor=int(iList[k]) ** iTamaño
      suma=suma + valor
    if suma == i:
      valores.append(i)
  valTamaño=len(valores)
  if valTamaño>0:
    print(f'Los números narcisistas dentro del intervalo {nUno}-{nDos} son:')
    for l in range(0,valTamaño-1,1):
      print(f'{valores[l]}, ',end='')
    print(f'{valores[valTamaño-1]}')
  else:
    print("No existen números narcisistas dentro de este intervalo")