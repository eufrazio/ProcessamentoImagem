# -*- coding: cp1252 -*-
__author__ = 'Euf'

from PIL import Image
import numpy as np


# Carregando a imagem original:
img = Image.open("pimentãoA.jpg")

'''
arquivos:
pimentãoA.jpg
pimentãoSlide.jpg
'''

# Criando um array da imagem
matIm = np.array(img,dtype=int)
print("Imagem Matriz:\n",matIm)

# Obtendo as dimensões: Largura e altura da imagem original
x, y = matIm.shape
print(matIm.shape)

#Sobel1:
sobel1 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        sobel1[i,j] = (-1*matIm[i-1,j-1]) + (-2*matIm[i-1,j]) + (-1*matIm[i-1,j+1]) +\
                          (0*matIm[i,j-1]) + (0*matIm[i,j]) + (0*matIm[i,j+1]) +\
                          (1*matIm[i+1,j-1]) + (2*matIm[i+1,j]) + (1*matIm[i+1,j+1])
        if(sobel1[i,j] < 0):
            sobel1[i,j] = 0

# sobel2:
sobel2 = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        sobel2[i,j] = (-1*matIm[i-1,j-1]) + (0*matIm[i-1,j]) + (1*matIm[i-1,j+1]) +\
                          (-2*matIm[i,j-1]) + (0*matIm[i,j]) + (2*matIm[i,j+1]) +\
                          (-1*matIm[i+1,j-1]) + (0*matIm[i+1,j]) + (1*matIm[i+1,j+1])
        if(sobel2[i,j] < 0):
            sobel2[i,j] = 0

print("\nSobel-1 a\n", sobel1)
print("\nSobel-2 b\n", sobel2)

sb1 = 255 - sobel1
sb2 = 255 - sobel2

#Criar imagem nova
h1 = Image.fromarray(sb1)
h2 = Image.fromarray(sb2)

img.show()
h1.show()
h2.show()