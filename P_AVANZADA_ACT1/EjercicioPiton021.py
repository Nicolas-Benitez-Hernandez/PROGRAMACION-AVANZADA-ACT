# -*- coding: utf-8 -*-
"""EjercicioPiton021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pxMGRGA4Lznn7AfQUOBTGskDsLgIiVd1
"""

print('Número feliz')
N=int(input("Ingresa un número entero positivo: "))
print('')

if N < 1:
  print('El valor no es el pedido')
else:
  nStr=str(N)
  valores=[i for i in nStr]
  control=True
  m=0
  while control==True:
    suma=0
    for j in range(0,len(valores),1):
      suma=(int(valores[j]) ** 2) + suma
    for l in range(0,len(valores)-1,1):
      print(f'{valores[l]}^2 + ', end='')
    print(f'{valores[len(valores)-1]}^2 = {suma}')
    valores=[k for k in str(suma)]
    m += 1
    if suma==1:
      print('')
      print(f'{N} es un número feliz :)')
      break
    elif m == 9:
      print('')
      print(f'{N} no es un número feliz :(')
      break