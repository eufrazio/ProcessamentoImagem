# -** coding: cp1252 -*-

__author__ = 'Euf'

from PIL import Image
import numpy as np

#----------------------------------------------------------------
print("\n\nBilinear - Redução:\n")

imagem = Image.open("robotech1.jpg")
imageMat = np.array(imagem,dtype=int)
print("Matriz da Imagem:\n\n",imageMat)

x,y = imageMat.shape
print("Original:",x,y)
x1 = int((imageMat.shape[0])/2)
y1 = int((imageMat.shape[1])/2)
print("Reducao:",x1,y1)

bilinearReduz = np.zeros((x1,y1),dtype=int)
print("\n\nImagem Reduzida\n",bilinearReduz)

print("\nProcesso de Redução\n")

i1 = 0
j1 = 0
for i in range(x1):
    for j in range(y1):
        bilinearReduz[i,j] = int((imageMat[i1,j1] + imageMat[i1,j1+1] + imageMat[i1+1,j1] + imageMat[i1+1,j1+1])/4)
        #bilinearReduz[i,j] = np.median(np.array([imageMat[i1,j1] + imageMat[i1,j1+1] + imageMat[i1+1,j1] + imageMat[i1+1,j1+1]]))
        j1 += 2
    j1 = 0
    i1 += 2

print("Adquirindo imagem reduzida\n")
imagem_nova = Image.fromarray(bilinearReduz)
#imagem_nova.save("rbreduz.jpg")
#Image.open('old.jpeg').convert('RGB').save('new.jpeg')
imagem.show()
imagem_nova.show()

