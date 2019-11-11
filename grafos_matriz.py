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
i) busca em profundidade -feita
j) Implmentar os algoritmos Prim e Kruskal
"""

class vertice:
   def __init__(self, conteudo):
      self.conteudo = conteudo      #referece ao conteudo do vertice
      self.adjacente = []           #os adjacentes ao vertice é uma lista de vertices
      self.bandeira_de_visita = 0
      self.distancia = None
      self.pai = None

class grafo_matriz:
   def __init__(self, lista = []):
      tam = len(lista)
      self.vertices = lista
      
      self.vertices_2 = []
      for elem in lista:
         self.vertices_2.append(vertice(elem))

      self.matriz_adj = np.zeros([tam, tam])

   def adicona_vertice(self, conteudo):
      self.vertices.append(conteudo)
      self.vertices_2.append(vertice(conteudo))
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
   
   def indentifica_fontes_e_sumidouros(self):
      for vertice_u in self.vertices:
         grau_entrada, grau_saida = self.grau_de_entrada_e_saida(vertice_u)
         _str = "vértice "+str(vertice_u)
         if ( grau_entrada == 0 ):
            _str += " é fonte"
         if ( grau_saida == 0 ):
            _str += " é sumidouro"
         print(_str)

   def busca_em_profundidade(self, vertice_u):
      for i in range(len(self.vertices)):
         if ( self.vertices[i] == vertice_u ):
            print( self.vertices[i] )
            self.vertices_2[i].bandeira_de_visita = 1
            break

      for j in range(len(self.vertices)):
         if(self.matriz_adj[i, j] != 0 and self.vertices_2[j].bandeira_de_visita == 0):
            self.busca_em_profundidade(self.vertices[j])
            print("backtrack")




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
#grafo.grau_de_entrada_e_saida( "z",print_flag = True)
#grafo.indentifica_fontes_e_sumidouros()
grafo.busca_em_profundidade("w")