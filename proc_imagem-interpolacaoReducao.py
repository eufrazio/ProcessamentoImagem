# -** coding: cp1252 -*-

__author__ = 'Euf'

from PIL import Image
import numpy as np

#----------------------------------------------------------------
print("\n\nVizinho mais Próximo - Redução:\n")

imagem = Image.open("robotech1.jpg")
imageMat = np.array(imagem,dtype=int)
print("Matriz da Imagem:\n\n",imageMat)

x,y = imageMat.shape
print("Original:",x,y)
x1 = int((imageMat.shape[0])/2)
y1 = int((imageMat.shape[1])/2)
print("Reducao:",x1,y1)

imageReduz = np.zeros((x1,y1),dtype=int)
print("\n\nImagem Reduzida\n",imageReduz)

print("\nProcesso de Redução\n")

i1 = 0
j1 = 0
for i in range(x1):
    for j in range(y1):
        imageReduz[i,j] = imageMat[i1,j1]
        j1 += 2
    j1 = 0
    i1 += 2

print("Adquirindo imagem reduzida\n")
imagem_nova = Image.fromarray(imageReduz)
#imagem_nova.save("rbreduz.jpg")
#Image.open('old.jpeg').convert('RGB').save('new.jpeg')
imagem.show()
imagem_nova.show()



'''
#-------------------------------------------
# T R E I N A M E N T O
lista1 = np.random.randint(7,size=(4,4))
lista1 = lista1.copy()
x,y=lista1.shape
lista2 = np.ones((2,2),dtype=int)
lista2 = lista2.copy()
x1,y1=lista2.shape
print("\n--------\nMatriz1\n",lista1)
print("\n\n--------\nMatriz2\n",lista2)

#for i in (x):
 #   for j in (y):
  #      lista2[i,j] = lista1[i,j]

i1=0
j1=0
for i in range(x1):
    for j in range(y1):
        lista2[i,j] = lista1[i1,j1]
        j1 += 2
    j1=0
    i1 += 2

print("---------\nLista Reduzida\n\n",lista2)
# Criando imagem nova




#arredondando valores
# matrnova[i+1,j+1] = int(round((matrnova[i,j] + matrnova[i,j+1] + matrnova[i,j+2] + matrnova[i+1,j] + matrnova[i+2,j]+ matrnova[i+2,j+1] + matrnova[i+2,j+2] + matrnova[i+1,j+2] + matrnova[i+1,j+1])/9))

'''