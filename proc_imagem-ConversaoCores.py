# -*- coding: cp1252 -*-
__author__ = 'Eufrazio'


from PIL import Image
import numpy as np

'''
ESTRATÉGIAS:
para separar canais:
R = img[:,:,0].copy() para separar o canal RED
G = img[:,:,1].copy() para separar o canal GREEN
B = img[:,:,2].copy() para separar o canal BLUE

DIVIDINDO E MESCLANDO CANAIS:
r, g, b = im.split() para dividir os canais
im = Image.merge("RGB", (b, g, r)) para mesclar os canais

SITES FÓRMULAS PARA CONVERSÃO:
http://www.rapidtables.com/convert/color/cmyk-to-rgb.htm

'''

# Carregando a imagem original:
img = Image.open("robotech3.jpg")
print("Modo img:",img.mode)#
print(Image.VERSION)

# Criando um array da imagem
matIm = np.array(img)
print("Imagem Matriz:\n",matIm)

# Obtendo as dimensões: Largura e altura da imagem original
x, y, z = matIm.shape
print(x,y,z)
print(matIm[0,0,0])
print(matIm[0,0])
print(matIm.shape)

cmyk = np.zeros((x,y,4),dtype=int)
print("Formato Imagem 'cmyk'", cmyk.shape)
# cmyk = (int((1-matIm)/255)*100)

print(cmyk[0,0])
# for i in range(x):
#     for j in range(y):
#         cmyk[i,j] = matIm[i,j]

# print("\ncmyk\n", cmyk)

#Criar imagem nova
imagem_nova = Image.fromarray(matIm)
img.show()
imagem_nova.show()
print("MODO imagem_nova:", imagem_nova.mode)

#conversão de imagens no modo 'HSV'
imagemHSV = Image.fromarray(matIm, mode='HSV')
# imagemHSV.save("robot1.png")
arroz =
imagemHSV.show()
print("Modo e formato imagemHSV :", imagemHSV.mode)

# criando um array da imagem para conferir o formato e o modo
matHSV = np.array(imagemHSV)
print("Ponto x0 e y0 de matHSV", matHSV)
print(matHSV.shape)

# imRGB = Image.fromarray(cmyk).convert('RGB')