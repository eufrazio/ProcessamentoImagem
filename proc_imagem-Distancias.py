#-* coding: cp1252 -*-
__author__ = 'Euf'


from PIL import Image
import numpy as np
from math import sqrt
import math#biblioteca para poenciacao

#----------------------------------------------------------------
print("\n\nCálculo de Distâncias\n")

imagem = Image.open("robotech1.jpg")
imageDist = np.array(imagem,dtype=int)
print("Matriz da Imagem:\n\n",imageDist)

x,y = imageDist.shape
print("Formato da Imagem:",x,y)

print(20*"--","\nDistância D4" )

print("Informe valores para xp e yp para o ponto 'P'")
xp = int(input("xp:"))
yp = int(input("yp:"))
print("Ponto P(%d,%d)" %(xp,yp))

print("Informe valores para xq e yq para o ponto 'Q'")
xq = int(input("xq:"))
yq = int(input("yq:"))
print("Ponto Q(%d,%d)\n" %(xq,yq))

D4 = abs(xp-xq) + abs(yp-yq)
print(5*"*********","\nDistância D4 ----> ", D4)
De = (sqrt((xp-xq)**2 + (yp-yq)**2))
print("\nDistância De ----> %.2f" %De)
D8 = max(abs(xp-xq),abs(yp-yq))
print("\nDistância D8 ----> ", D8)
print(5*"*********")