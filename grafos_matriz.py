#coding: utf-8
import numpy as np

"""
a) Inserir nodo -feito
b) Remover nodo -feito
c) Inserir aresta -feito
d) Remover aresta  -feito
e) Visualizar o grafo -feito
f) Identificar Fontes e sumidouros -feito
g) Calcular o grau de entrada e o grau de saída de um vértice -feito
h) Busca em largura
i) busca em profundidade
"""

class vertice:
   def __init__(self, conteudo):
      self.conteudo = conteudo

class grafo_matriz:
   def __init__(self, lista = []):
      tam = len(lista)
      self.vertices = lista
      self.matriz_adj = np.zeros([tam, tam])

   def adicona_vertice(self, conteudo):
      self.vertices.append(conteudo)
      tam = len(self.vertices)
      nova_coluna = np.zeros([tam-1, 1])
      self.matriz_adj = np.concatenate((self.matriz_adj, nova_coluna), axis=1)
      nova_linha = np.zeros([1, tam])
      self.matriz_adj = np.concatenate((self.matriz_adj, nova_linha))
   def mostra_grafo(self):
      print(self.vertices)
      print (grafo.matriz_adj)
      
      


grafo = grafo_matriz(["x", "y", "z"])
grafo.mostra_grafo()
grafo.adicona_vertice("a")
grafo.mostra_grafo()
grafo.adicona_vertice("c")
grafo.mostra_grafo()
grafo.adicona_vertice("d")
grafo.mostra_grafo()