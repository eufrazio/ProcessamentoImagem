# -*- coding: cp1252 -*-
__author__ = 'Euf'

from PIL import Image
import numpy as np


# Carregando a imagem original:
img = Image.open("lua1.jpg")

# Criando um array da imagem
matIm = np.array(img,dtype=int)
print("Imagem Matriz:\n",matIm)

# Obtendo as dimensões: Largura e altura da imagem original
x, y = matIm.shape

media = np.zeros((x,y),dtype=int)

for i in range(1,x-1):
    for j in range(1,y-1):
        media[i,j] = int((matIm[i,j] + matIm[i-1,j-1] + matIm[i-1,j] + matIm[i-1,j+1] + matIm[i,j-1] + matIm[i,j+1] + matIm[i+1,j-1] + matIm[i+1,j] + matIm[i+1,j+1])/9)

print("\nmedia\n", media)
#Criar imagem nova
imagem_nova = Image.fromarray(media)
img.show()
imagem_nova.show()

