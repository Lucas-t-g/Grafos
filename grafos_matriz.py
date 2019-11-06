#coding: utf-8
import numpy as np

"""
a) Inserir nodo -feito
b) Remover nodo -feito
c) Inserir aresta -feito
d) Remover aresta  -feito
e) Visualizar o grafo -feito
f) Identificar Fontes e sumidouros 
g) Calcular o grau de entrada e o grau de saída de um vértice 
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
   
   def adiciona_aresta(self, vertice_v, vertice_u):
      if ( vertice_v and vertice_u in self.vertices ):
         v = self.vertices.index(vertice_v)
         u = self.vertices.index(vertice_u)
         self.matriz_adj[v][u] = 1
   def remove_areseta(self,vertice_v, vertice_u):
      if ( vertice_v and vertice_u in self.vertices ):
         v = self.vertices.index(vertice_v)
         u = self.vertices.index(vertice_u)
         self.matriz_adj[v][u] = 0

   def grau_de_entrada_e_saida(self, vertice_u, print_flag = False):
      for i in range(len(self.vertices)):
         grau_entrada = 0
         grau_saida = 0
         if ( self.vertices[i] == vertice_u ):
            for j in range(len(self.vertices)):
               if ( self.matriz_adj[i][j] == 1 ):
                  grau_saida -= -1

            for j in range(len(self.vertices)):
               if ( self.matriz_adj[j][i] == 1 ):
                  grau_entrada -= -1
            if (print_flag):
               print(self.vertices[i])
               print("grau de entrada é: ", grau_entrada )
               print("grau de saida é: ", grau_saida )
            return grau_entrada, grau_saida


#####__INICIO__DA_EXECUÇÃO__#####
grafo = grafo_matriz(["x", "y", "z", "w"])
#grafo.mostra_grafo()
grafo.adicona_vertice("a")
#grafo.mostra_grafo()
grafo.adiciona_aresta("a", "x")
grafo.adiciona_aresta("w", "a")
grafo.adiciona_aresta("z", "a")
grafo.adiciona_aresta("w", "z")
grafo.adiciona_aresta("y", "w")
#grafo.mostra_grafo()
grafo.remove_areseta("z", "a")
grafo.mostra_grafo()
grafo.grau_de_entrada_e_saida( "z",print_flag = True)