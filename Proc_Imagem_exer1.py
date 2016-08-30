# -*- coding: cp1252 -*-
__author__ = 'Euf'


# Importando as bibliotecas Pillow e Numpy:
from PIL import Image
from numpy import *

# Carregando a imagem original:
img = Image.open("peninha1.jpg")

# Obtendo as dimensões: Largura e altura da imagem original

width, height = img.size
print("Largura: ",width)
print("Altura: ",height)

#Criando uma matriz a partir da imagem original
matriz = array(img)
print("Matriz da imagem:\n",matriz)

#Imprimindo as dimensões da imagem original
print("Dimensões: \n", img.size)

#Criando variáveis do tipo inteira para Largura e Altura
x = int(img.size[0])
y = int(img.size[1])

#Exemplo de tuplas
alfabeto = (1,2,3,4)
print("Classe da variavel alfabeto: ",type(alfabeto))
print(alfabeto)

#Impressão das coordenadas x e y
print("Coord x: %d - Coord y: %d" %(x,y))

# Iterando todos os valores da Matriz Original pela largura
print("\n\nTodos os valores da matriz da imagem")

print(matriz(45,65))
# for i in range (0, x):
#     for j in range (0, y):
#         print(matriz(i,j))