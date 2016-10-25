# -*- coding: cp1252 -*-
__author__ = 'Euf'

from PIL import Image
import numpy as np


# Carregando a imagem original:
img = Image.open("carro.jpg")
'''
arquivos:
laplace_lenna.JPG
lennaSlide.JPG
carro.jpg
olhar.JPG
lua1.jpg
'''

# Criando um array da imagem
matIm = np.array(img,dtype=int)
print("Imagem Matriz:\n",matIm)

# Obtendo as dimensões: Largura e altura da imagem original
x, y = matIm.shape
print(matIm.shape)

#Laplaciano1: Máscara 'a'
laplaciano1 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        laplaciano1[i,j] = (0*matIm[i-1,j-1]) + (1*matIm[i-1,j]) + (0*matIm[i-1,j+1]) +\
                          (1*matIm[i,j-1]) + (-4*matIm[i,j]) + (1*matIm[i,j+1]) +\
                          (0*matIm[i+1,j-1]) + (1*matIm[i+1,j]) + (0*matIm[i+1,j+1])
        if(laplaciano1[i,j] < 0):
            laplaciano1[i,j] = 0

#Laplaciano2: Máscara 'b'
laplaciano2 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        laplaciano2[i,j] = (1*matIm[i-1,j-1]) + (1*matIm[i-1,j]) + (1*matIm[i-1,j+1]) +\
                          (1*matIm[i,j-1]) + (-8*matIm[i,j]) + (1*matIm[i,j+1]) +\
                          (1*matIm[i+1,j-1]) + (1*matIm[i+1,j]) + (1*matIm[i+1,j+1])
        if(laplaciano2[i,j] < 0):
            laplaciano2[i,j] = 0

#Laplaciano: Máscara 'c'
laplaciano3 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        laplaciano3[i,j] = (0*matIm[i-1,j-1]) + (-1*matIm[i-1,j]) + (0*matIm[i-1,j+1]) +\
                          (-1*matIm[i,j-1]) + (4*matIm[i,j]) + (-1*matIm[i,j+1]) +\
                          (0*matIm[i+1,j-1]) + (-1*matIm[i+1,j]) + (0*matIm[i+1,j+1])
        if(laplaciano3[i,j] < 0):
            laplaciano3[i,j] = 0

#Laplaciano: Máscara 'd'
laplaciano4 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        laplaciano4[i,j] = (-1*matIm[i-1,j-1]) + (-1*matIm[i-1,j]) + (-1*matIm[i-1,j+1]) +\
                          (-1*matIm[i,j-1]) + (8*matIm[i,j]) + (-1*matIm[i,j+1]) +\
                          (-1*matIm[i+1,j-1]) + (-1*matIm[i+1,j]) + (-1*matIm[i+1,j+1])
        if(laplaciano4[i,j] < 0):
            laplaciano4[i,j] = 0

#Filtro Laplaciano com Média
laplaciano5 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        laplaciano5[i,j] = int(((-1*matIm[i-1,j-1]) + (-1*matIm[i-1,j]) + (-1*matIm[i-1,j+1]) +\
                          (-1*matIm[i,j-1]) + (8*matIm[i,j]) + (-1*matIm[i,j+1]) +\
                          (-1*matIm[i+1,j-1]) + (-1*matIm[i+1,j]) + (-1*matIm[i+1,j+1]))/9)
        if(laplaciano5[i,j] < 0):
            laplaciano5[i,j] = 0


#Filtro Laplaciano com Imagem Negativa
neg1 = 255-laplaciano5
neg2 = 255-laplaciano4

print("\nlaplaciano a\n", laplaciano1)
print("\nlaplaciano b\n", laplaciano2)
print("\nlaplaciano c\n", laplaciano3)
print("\nlaplaciano d\n", laplaciano4)
print("\nlaplaciano com média\n", laplaciano5)

#Criar imagem nova
lap1 = Image.fromarray(laplaciano1)
lap2 = Image.fromarray(laplaciano2)
lap3 = Image.fromarray(laplaciano3)
lap4 = Image.fromarray(laplaciano4)
lap5 = Image.fromarray(laplaciano5)
negativa1 = Image.fromarray(neg1)
negativa2 = Image.fromarray(neg2)


img.show()
lap1.show()
lap2.show()
lap3.show()
lap4.show()
lap5.show()
negativa1.show()
negativa2.show()