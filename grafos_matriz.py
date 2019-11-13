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
h) Busca em largura -feit
i) busca em profundidade -feita
j) Implmentar os algoritmos Prim e Kruskal
"""
def np_array_None(linhas, colunas):
   aux = [None]*colunas
   matriz = []
   for i in range(linhas):
      matriz.append(aux)
   matriz = np.array(matriz)
   return matriz

class arestas_se:
   def __init__(self, custo, i, j):
      self.custo = custo
      self.i = i
      self.j = j
   def print_arestas_se(self):
      print("(",self.custo, self.i, self.j, ")")

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
      self.matriz_adj = np_array_None(tam, tam)

      for linha in self.matriz_adj:
         for elem in linha:
            elem = None


   def adicona_vertice(self, conteudo):
      self.vertices.append(conteudo)
      self.vertices_2.append(vertice(conteudo))
      tam = len(self.vertices)
      nova_coluna = np_array_None(tam-1, 1)
      self.matriz_adj = np.concatenate((self.matriz_adj, nova_coluna), axis=1)
      nova_linha = np_array_None(1, tam)
      self.matriz_adj = np.concatenate((self.matriz_adj, nova_linha))

   def remove_vertice(self, vertice):
      i = self.vertices.index(vertice)
      del(self.vertices[i])
      del(self.vertices_2[i])
      self.matriz_adj = np.delete(self.matriz_adj, i, 0)
      self.matriz_adj = np.delete(self.matriz_adj, i, 1)

   def mostra_grafo(self):
      print(self.vertices)
      print (grafo.matriz_adj)
   
   def adiciona_aresta(self, vertice_v, vertice_u, custo = 1):
      if ( vertice_v and vertice_u in self.vertices ):
         v = self.vertices.index(vertice_v)
         u = self.vertices.index(vertice_u)
         self.matriz_adj[v][u] = custo
   def remove_areseta(self,vertice_v, vertice_u):
      if ( vertice_v and vertice_u in self.vertices ):
         v = self.vertices.index(vertice_v)
         u = self.vertices.index(vertice_u)
         self.matriz_adj[v][u] = None

   def grau_de_entrada_e_saida(self, vertice_u, print_flag = False):
      for i in range(len(self.vertices)):
         grau_entrada = 0
         grau_saida = 0
         if ( self.vertices[i] == vertice_u ):
            for j in range(len(self.vertices)):
               if ( self.matriz_adj[i][j] != None ):
                  grau_saida -= -1

            for j in range(len(self.vertices)):
               if ( self.matriz_adj[j][i] != None ):
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
         if ( grau_entrada == 0 and grau_saida == 0 ):
            _str += " é nada"
         elif ( grau_entrada == 0 ):
            _str += " é fonte"
         elif ( grau_saida == 0 ):
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

   def busca_largura(self, vertice):
      for i in range(len(self.vertices)):
         if ( self.vertices[i] == vertice ):
            print( self.vertices[i] )
            self.vertices_2[i].bandeira_de_visita = 1
            self.vertices_2[i].distancia = 0
            self.vertices_2[i].pai = None
            break
      lista = [self.vertices_2[i]]
      while ( len(lista) > 0 ):
         vertice_u = lista.pop()
         i = self.vertices_2.index(vertice_u)
         print("vertice u: ", vertice_u.conteudo)
         for j in range(len(self.vertices)):
            if (self.matriz_adj[i][j] != 0 and self.vertices_2[j].bandeira_de_visita == 0):
               self.vertices_2[j].bandeira_de_visita = 1
               self.vertices_2[j].distancia = vertice_u.distancia + 1
               self.vertices_2[j].pai = vertice_u.conteudo
               lista.insert(0, self.vertices_2[j])
               print("vertice w: ", self.vertices_2[j].conteudo, "distância: ", self.vertices_2[j].distancia, "pai: ", self.vertices_2[j].pai, "bdv: ", self.vertices_2[j].bandeira_de_visita)

   def lista_arestas(self):
      lista  = []
      tam = len(self.vertices)
      for i in range(tam):
         for j in range(tam):
            if ( self.matriz_adj[i][j] != None ):
               lista.append(arestas_se(self.matriz_adj[i][j], i, j))

      lista.sort(key=lambda a: a.custo)
      return lista

   """
   def kruskal(self, vertice_u):
      tam = len(self.vertices)
      vertices_aux = self.vertices
      matriz_aux = np_array_None(tam, tam))
      for elem in
   """




#####__INICIO__DA_EXECUÇÃO__#####
grafo = grafo_matriz(["x", "y", "z", "w"])
#grafo.mostra_grafo()
grafo.adicona_vertice("a")
#grafo.mostra_grafo()
grafo.adiciona_aresta("a", "x", 4)
grafo.adiciona_aresta("w", "a")
grafo.adiciona_aresta("z", "a", 3)
grafo.adiciona_aresta("w", "z", 7)
grafo.adiciona_aresta("y", "w", 10)
#grafo.mostra_grafo()
#grafo.remove_areseta("a", "x")
#grafo.mostra_grafo()
#grafo.grau_de_entrada_e_saida( "z",print_flag = True)
#grafo.indentifica_fontes_e_sumidouros()
#grafo.busca_em_profundidade("w")
#grafo.busca_largura("w")
#grafo.remove_vertice("z")
grafo.mostra_grafo()
grafo.lista_arestas()