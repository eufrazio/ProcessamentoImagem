# -*- coding: cp1252 -*-
__author__ = 'Euf'

from PIL import Image
import numpy as np


# Carregando a imagem original:
img = Image.open("lenna.jpg")

# Criando um array da imagem
matIm = np.array(img)
print("Imagem Matriz:\n",matIm)

# Obtendo as dimensões: Largura e altura da imagem original
x, y = matIm.shape
print(matIm.size)
# print("Largura: ",x)
# print("Altura: ",y)

# criação da look-up table
rk = np.zeros((256,1),dtype=int)
#c = 0
for i in range(256):
    for j in range(1):
        rk[i,0] = i
        #c = c + 1
print("Coluna rk:\n",rk)

#Vetor para contar a qtde de pixel do nivel de cinza
nk = np.zeros((256,1),dtype=int)

for i in range(x):
    for j in range(y):
        nk[matIm[i,j]] = nk[matIm[i,j]] + 1
# print("Valores:\n", nk)

somank = 0
for i in range(256):
    somank = somank + nk[i]
print("Somatorio de pixels: ", somank)

# prrk = np.zeros((256,1))

# for i in range(256):
#     prrk[i] = nk[i]/somank
prrk = nk/somank
print("prrk: \n",prrk)


somaprrk = 0
for i in range(256):
    somaprrk = somaprrk + prrk[i]
print("Somatorio prrk: ", somaprrk)

aux = 0
freq = np.zeros((256,1))
for i in range(256):
    freq[i] = prrk[i] + aux
    aux = freq[i]
print("Frequencia Acumulada:\n",freq)

eq = freq*255
print("\n\nequalização:\n",eq)

eq1 = np.array((eq),dtype=int)
print("\n\nEqualização em Inteiros:\n",eq1)

#arredondamento
print("Antigo: ",eq[100])
print("Novo: ",eq1[100])

# Matriz original recebendo valores novos
matImnova = matIm
for i in range(x):
    for j in range(y):
        matImnova[i,j]=eq1[matImnova[i,j]]
print("MatrizNova:\n",matImnova)

#Criar imagem nova
imagem_nova = Image.fromarray(matImnova)
imagem_nova.save("lennahist.jpg")
img.show()
imagem_nova.show()

