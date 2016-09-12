# -** coding: cp1252 -*-

__author__ = 'Euf'

from PIL import Image
import numpy as np

#----------------------------------------------------------------
print("\n\nVizinho mais Próximo - Ampliação:\n")

imagem = Image.open("robotech1.jpg")
imageMat = np.array(imagem,dtype=int)
print("Matriz da Imagem:\n\n",imageMat)

x,y = imageMat.shape
print("Original:",x,y)
x1 = int((imageMat.shape[0])*2)
y1 = int((imageMat.shape[1])*2)
print("Ampliação:",x1,y1)

imageAmpl = np.zeros((x1,y1),dtype=int)
print("\n\nImagem Ampliada\n",imageAmpl)

for i in range(x1):
    for j in range(y1):
        imageAmpl[i,j] = 255
print("\n\nValor Branco\n",imageAmpl)

print("\nProcesso de Ampliação\n")

i1 = 0
j1 = 0
for i in range(0,x1,2):
    for j in range(0,y1,2):
        imageAmpl[i,j] = imageMat[i1,j1]
        j1 += 1
    j1 = 0
    i1 += 1

print("\nINTERPOLAÇÃO\n",imageAmpl)

for i in range(0,x1,2):
    for j in range(0,y1,2):
        imageAmpl[i,j+1] = imageAmpl[i,j]
        imageAmpl[i+1,j] = imageAmpl[i,j]
        imageAmpl[i+1,j+1] = imageAmpl[i,j]

print("\nBrancos preenchidos\n",imageAmpl)

'''
for i in range(x1):
    for j in range(y1):
        imageAmpl[i,j] = 0
print("\n\nValor Branco\n",imageAmpl)

'''


print("Adquirindo imagem Ampliada\n")
imagem_nova = Image.fromarray(imageAmpl)
#imagem_nova.save("robotechReduzido.png")
imagem.show()
imagem_nova.show()