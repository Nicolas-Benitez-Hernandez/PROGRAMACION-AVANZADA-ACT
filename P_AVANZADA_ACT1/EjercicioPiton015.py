# -*- coding: utf-8 -*-
"""EjercicioPiton015.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-4dDK8-p-zD7gjieizdeFXCGvcuJ5zNz
"""

print('MCM y MCD')
nUno=int(input("Ingresa el número entero positivo mayor: "))
nDos=int(input("Ingresa el número entero positivo menor: "))
print('')

if (nUno <= 0) or (nDos <= 0) or (nUno <= nDos):
  print('El valor ingresado no es el pedido')

else:
  a=int(nUno/nDos)

  if((nUno % nDos) == 0):
    print(f'El maximo común divisor de {nUno} y {nDos} es: {a}')
    m=int((nDos * nUno)/a)
    print(f'El minimo común multiplo es: {m}')
  else:
    c=int(nDos*a)
    d=int(nUno-c)
    y=int(d)
    r=int(nDos)
    while ((nDos % d) != 0):
      s=int(r/d)
      f=int(s*d)
      d=int(r-f)
    print(f'El maximo común divisor de {nUno} y {nDos} es: {d}')
    m=int((nDos*nUno)/d)
    print(f'El minimo común multiplo es: {m}')