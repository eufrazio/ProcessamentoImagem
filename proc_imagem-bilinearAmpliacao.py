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
x1 = int(((imageMat.shape[0])*2))
y1 = int(((imageMat.shape[1])*2))
print("Ampliação:",x1,y1)

bilinearAmpl = np.zeros((x1,y1),dtype=int)
print("\n\nImagem Ampliada\n",bilinearAmpl)



for i in range(x1):
    for j in range(y1):
        bilinearAmpl[i,j] = 255
print("\n\nValor Branco\n",bilinearAmpl)

print("\nProcesso de Ampliação\n")

i1 = 0
j1 = 0
for i in range(0,x1-1,2):
    for j in range(0,y1-1,2):
        bilinearAmpl[i,j] = imageMat[i1,j1]
        j1 += 1
    j1 = 0
    i1 += 1

print("\nINTERPOLAÇÃO\n",bilinearAmpl)

i1 = 0
j1 = 0
for i in range(0,x1-2,2):
    for j in range(0,y1-2,2):
        bilinearAmpl[i,j+1] = int((imageMat[i1,j1] + imageMat[i1,j1+1])/2)
        bilinearAmpl[i+1,j] = int((imageMat[i1,j1] + imageMat[i1+1,j1])/2)
        bilinearAmpl[i+1,j+1] = int((imageMat[i1,j1] + imageMat[i1,j1+1] + imageMat[i1+1,j1] + imageMat[i1+1,j1+1] )/4)
        bilinearAmpl[i+1,j+2] = int((imageMat[i1,j1+1] + imageMat[i1+1,j1+1])/2)
        bilinearAmpl[i+2,j+1] = int((imageMat[i1+1,j1] + imageMat[i1+1,j1+1])/2)
        j1 += 1
    j1 = 0
    i1 += 1
'''
Substitua: a = (f(i,j) + f(i,j+1)) / 2
? e = (f(i+1,j) + f(i+1,j+1)) / 2
? b = (f(i,j) + f(i+1,j)) / 2
? d = (f(i,j+1) + f(i+1,j+1)) / 2
? c = (f(i,j) + f(i,j+1) + f(i+1,j) + f(i+1,j+1)) / 4
'''


print("\nBrancos preenchidos\n",bilinearAmpl)

'''
for i in range(x1):
    for j in range(y1):
        bilinearAmpl[i,j] = 0
print("\n\nValor Branco\n",bilinearAmpl)

'''


print("Adquirindo imagem Ampliada\n")
imagem_nova = Image.fromarray(bilinearAmpl)
#imagem_nova.save("robotechReduzido.png")
imagem.show()
imagem_nova.show()