from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from random import shuffle, randint
import random
 
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
  
def geraInversa(size):
  lista=list(range(size,1,-1))
  return lista

def geraOrdenado(size):
	return list(range(size))


def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", name='fig'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo Aleatório")
    #ax.plot(x,y2, label = "Melhor Tempo Decrescente")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name+'.png')

operacoes=[]

def radixSort(arr):
    exp = 1
    maior = max(arr) if len(arr) > 2 else 0


    aux = [ [] for i in range(10)]

    while maior // exp > 0:
        for i in arr:
            aux[(i//exp)%10].append(i)

        del arr[:]

        for i in range(len(aux)):
            arr.extend(aux[i])
            aux[i] = []

        exp *= 10
    return arr
            

listas=[]
listaInversa=[]
listaOrdenada=[]
x2 = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
y2=[]
y3=[]

for i in range(len(x2)):
  listas.append(geraLista(x2[i]))
  listaInversa.append(geraInversa(x2[i]))


for i in range(len(x2)):
  y.append(timeit.timeit("radixSort({})".format(listas[i]),setup="from __main__ import radixSort",number=1))
  print("Terminou de ordenar um vetor de tamanho " + str(x2[i]) + "...")


print(operacoes[:])

desenhaGrafico(x2,y,'Quantidade','Tempo', 'radixSort')
