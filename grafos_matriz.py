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
j) Implmentar os algoritmos Prim e Kruskal - feito
i) Implmentar os algoritmos Bellamn-Ford e Djikstra -feito
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
      self.bandeira_de_visita = 0
      self.distancia = None
      self.pai = None
   def print_vertice(self):
      #print("v: ", self.conteudo, " || pai: ", self.pai, " || d: ", self.distancia, " || bdv: ", self.bandeira_de_visita)
      _str = 'v: {:^6} | pai: {:^6} | d: {:^6} | bdv: {:^6}'.format(str(self.conteudo), str(self.pai), str(self.distancia), str(self.bandeira_de_visita))
      print(_str)
   
   def print_vertice_detalhes(self):
      print("v: {:^6} | pai: {:^6} | d: {:^6} | bdv: {:^6}".format(str(self.conteudo), str(self.pai), str(self.distancia), str(self.bandeira_de_visita)))

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
      _str = '     ['
      for elem in self.vertices:
         _str += '{:>5},'.format(elem)
      print(_str,"]")
      tam = len(self.vertices)
      for i in range(tam):
         _str = '{:>5}['.format(self.vertices[i])
         for j in range(tam):
            _str += '{:>5},'.format(str(self.matriz_adj[i][j]))
         print(_str,"]")
   
   def adiciona_aresta(self, vertice_v, vertice_u, custo = 1):
      if ( vertice_v and vertice_u in self.vertices ):
         v = self.vertices.index(vertice_v)
         u = self.vertices.index(vertice_u)
         self.matriz_adj[v][u] = custo

   def adiciona_aresta_sem_direcao(self, vertice_v, vertice_u, custo = 1):
      if ( vertice_v and vertice_u in self.vertices ):
         v = self.vertices.index(vertice_v)
         u = self.vertices.index(vertice_u)
         self.matriz_adj[v][u] = custo
         self.matriz_adj[u][v] = custo

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
         if(self.matriz_adj[i, j] != None and self.vertices_2[j].bandeira_de_visita == 0):
            self.busca_em_profundidade(self.vertices[j])
            print("backtrack")
   
   def busca_em_profundidade_2(self, vertice_u, vertice_x):
      if( vertice_u == vertice_x ):
         #print("achou")
         return True

      for i in range(len(self.vertices)):
         if ( self.vertices[i] == vertice_u ):
            #print( self.vertices[i] )
            self.vertices_2[i].bandeira_de_visita = 1
            break

      for j in range(len(self.vertices)):
         if(self.matriz_adj[i, j] != None and self.vertices_2[j].bandeira_de_visita == 0):
            temp = self.busca_em_profundidade_2(self.vertices[j], vertice_x)
            if (temp):
               return temp
            #print("backtrack")
      return False

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
            if (self.matriz_adj[i][j] != None and self.vertices_2[j].bandeira_de_visita == 0):
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

   def busca_largura_2(self, vertice, vertice_x):
      for i in range(len(self.vertices)):
         if ( self.vertices[i] == vertice ):
            #print( self.vertices[i] )
            self.vertices_2[i].bandeira_de_visita = 1
            self.vertices_2[i].distancia = 0
            self.vertices_2[i].pai = None
            break
      lista = [self.vertices_2[i]]
      while ( len(lista) > 0 ):
         vertice_u = lista.pop()
         i = self.vertices_2.index(vertice_u)
         #print("vertice u: ", vertice_u.conteudo)
         for j in range(len(self.vertices)):
            if (self.matriz_adj[i][j] != None and self.vertices_2[j].bandeira_de_visita == 0):
               self.vertices_2[j].bandeira_de_visita = 1
               self.vertices_2[j].distancia = vertice_u.distancia + 1
               self.vertices_2[j].pai = vertice_u.conteudo
               lista.insert(0, self.vertices_2[j])
               #print("vertice w: ", self.vertices_2[j].conteudo, "distância: ", self.vertices_2[j].distancia, "pai: ", self.vertices_2[j].pai, "bdv: ", self.vertices_2[j].bandeira_de_visita)
               print("igua: ",self.vertices_2[j].conteudo, vertice_x)
               if( self.vertices_2[j].conteudo == vertice_x ):
                  return self.vertices_2[j]
      return None
   
   def nao_e_geradora(self):
      tam = len(self.vertices)
      for vertice_u in self.vertices:
         for vertice_v in self.vertices:
            #print("u - ", vertice_u, " || v - ", vertice_v)
            self.zera_visitas()
            if ( self.busca_em_profundidade_2(vertice_u, vertice_v) == False ):
               return True
      return False

   def kruskal_sem_direcao(self, teste_print = True, atualiza_matriz = False):
      aux = grafo_matriz(self.vertices)
      arestas = self.lista_arestas()
      while ( aux.nao_e_geradora() and len(arestas) > 0 ):
         aresta = arestas.pop(0)
         aux.zera_visitas()
         temp = aux.busca_em_profundidade_2(self.vertices[aresta.i], self.vertices[aresta.j])
         if ( not temp ):
            if ( teste_print ):
               print("i = ", aresta.i," -> ", aux.vertices[aresta.i], "|| j = ", aresta.j," -> ", aux.vertices[aresta.j])
            aux.matriz_adj[aresta.i][aresta.j] = aresta.custo
            aux.matriz_adj[aresta.j][aresta.i] = aresta.custo

      if( atualiza_matriz ):
         self.matriz_adj = aux.matriz_adj
   
   def zera_visitas(self):
      for vertice in self.vertices_2:
         vertice.bandeira_de_visita = 0
         vertice.pai = None
         vertice.distancia = float("inf")

   def visitou_todos(self):
      for vertice in self.vertices_2:
         if ( vertice.bandeira_de_visita == 0 ):
            return False
      return True

   def prim_sem_direcao(self, raiz = False, teste_print = True, atualiza_matriz = False):

      self.zera_visitas()
      raiz = 0 if (raiz == False) else self.vertices.index(raiz)
      self.vertices_2[raiz].bandeira_de_visita = 1
      self.vertices_2[raiz].distancia = 0
      i = raiz
      Q = self.vertices_2
      V = []
      while ( len(Q) > 0 ):
         Q.sort(key=lambda a: a.distancia)
         vertice_u = Q.pop(0)
         #vertice_u.print_vertice()
         V.append(vertice_u)

         i = self.vertices.index(vertice_u.conteudo)

         for j in range(len(self.vertices)):
            if ( self.matriz_adj[i][j] != None ):  #para pegar somente aqueles que são adjacentes a 'i'
               #print(i,j)
               pertence_Q = False
               for index in range(len(Q)):
                  if ( Q[index].conteudo == self.vertices[j] ):
                     pertence_Q = True
                     break
               if ( pertence_Q and self.matriz_adj[i][j] < Q[index].distancia ):
                  Q[index].pai = vertice_u.conteudo
                  Q[index].distancia = self.matriz_adj[i][j]
      if( teste_print ):
         for elem in V:
            elem.print_vertice()
      if( atualiza_matriz ):
         for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
               self.matriz_adj[i][j] = None
         for elem in V:
            self.adiciona_aresta_sem_direcao(elem.conteudo, elem.pai, elem.distancia)

   def Bellman_ford_direcionado(self, raiz = False, teste_print = True, atualiza_matriz = False):
      self.zera_visitas()
      raiz = 0 if (raiz == False) else self.vertices.index(raiz)
      self.vertices_2[raiz].distancia = 0
      self.vertices_2[raiz].pai = None
      self.vertices_2[raiz].bandeira_de_visita = 1
      lista_arestas = self.lista_arestas()

      for i in range(len(self.vertices)-1):
         if (teste_print):
            print("____________________i:",i)
            for elem in self.vertices_2:
               elem.print_vertice_detalhes()
         for aresta in lista_arestas:
            vertice_u = self.vertices_2[ aresta.i ]
            vertice_v = self.vertices_2[ aresta.j ]
            if ( vertice_v.distancia > aresta.custo + vertice_u.distancia ):
               vertice_v.pai = vertice_u.conteudo
               vertice_v.distancia = aresta.custo + vertice_u.distancia
               if (teste_print):
                  print("relax", vertice_v.distancia)
                  aresta.print_arestas_se()

      for aresta in lista_arestas:
         vertice_u = self.vertices_2[ aresta.i ]
         vertice_v = self.vertices_2[ aresta.j ]
         if ( vertice_v.distancia > aresta.custo + vertice_u.distancia ):
            return False
         
      if( teste_print ):
         print("final:")
         for vertice in self.vertices_2:
            vertice.print_vertice_detalhes()

      if ( atualiza_matriz ):
         for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
               self.matriz_adj[i][j] = None
         for vertice in self.vertices_2:
            for aresta in lista_arestas:
               if( self.vertices[aresta.i] == vertice.pai and self.vertices[aresta.j] == vertice.conteudo ):
                  self.adiciona_aresta(vertice.pai, vertice.conteudo, aresta.custo)

   def Dijkstra_direcionado(self, raiz = False, teste_print = True, atualiza_matriz = False):
      self.zera_visitas()
      lista_arestas = self.lista_arestas()
      raiz = 0 if (raiz == False) else self.vertices.index(raiz)
      self.vertices_2[raiz].bandeira_de_visita = 1
      self.vertices_2[raiz].distancia = 0
      i = raiz
      Q = self.vertices_2
      V = []
      while ( len(Q) > 0 ):
         Q.sort(key=lambda a: a.distancia)
         vertice_u = Q.pop(0)
         #vertice_u.print_vertice()
         V.append(vertice_u)

         i = self.vertices.index(vertice_u.conteudo)

         for j in range(len(self.vertices)):
            if ( self.matriz_adj[i][j] != None ):  #para pegar somente aqueles que são adjacentes a 'i'
               #print(i,j)
               pertence_Q = False
               for index in range(len(Q)):
                  if ( Q[index].conteudo == self.vertices[j] ):
                     pertence_Q = True
                     break
               if ( pertence_Q and self.matriz_adj[i][j] < Q[index].distancia ):
                  Q[index].pai = vertice_u.conteudo
                  Q[index].distancia = self.matriz_adj[i][j] + vertice_u.distancia
      if( teste_print ):
         V.sort(key=lambda a : a.conteudo)
         for elem in V:
            elem.print_vertice()
      
      if( atualiza_matriz ):
         for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
               self.matriz_adj[i][j] = None
         for vertice in V:
            for aresta in lista_arestas:
               if( self.vertices[aresta.i] == vertice.pai and self.vertices[aresta.j] == vertice.conteudo ):
                  self.adiciona_aresta(vertice.pai, vertice.conteudo, aresta.custo)
      


#####__INICIO__DA_EXECUÇÃO__#####
"""
grafo = grafo_matriz(["a", "b", "c", "d", "e", "f", "g", "h", "i"])
#grafo.mostra_grafo()
#grafo.adicona_vertice("a")
#grafo.mostra_grafo()
grafo.adiciona_aresta_sem_direcao("a", "b", 4)
grafo.adiciona_aresta_sem_direcao("b", "c", 8)
grafo.adiciona_aresta_sem_direcao("c", "d", 7)
grafo.adiciona_aresta_sem_direcao("d", "e", 9)
grafo.adiciona_aresta_sem_direcao("e", "f", 10)
grafo.adiciona_aresta_sem_direcao("f", "g", 2)
grafo.adiciona_aresta_sem_direcao("g", "h", 1)
grafo.adiciona_aresta_sem_direcao("h", "a", 8)
grafo.adiciona_aresta_sem_direcao("b", "h", 11)
grafo.adiciona_aresta_sem_direcao("h", "i", 7)
grafo.adiciona_aresta_sem_direcao("i", "c", 2)
grafo.adiciona_aresta_sem_direcao("c", "f", 4)
grafo.adiciona_aresta_sem_direcao("i", "g", 6)
grafo.adiciona_aresta_sem_direcao("d", "f", 14)
"""

"""
#exemplo Bellman
grafo = grafo_matriz(["s", "t", "x", "y", "z"])
grafo.adiciona_aresta("s", "t", 6)
grafo.adiciona_aresta("s", "y", 7)
grafo.adiciona_aresta("t", "x", 5)
grafo.adiciona_aresta("x", "t", -2)
grafo.adiciona_aresta("t", "y", 8)
grafo.adiciona_aresta("t", "z", -4)
grafo.adiciona_aresta("y", "x", -3)
grafo.adiciona_aresta("y", "z", 9)
grafo.adiciona_aresta("z", "s", 2)
grafo.adiciona_aresta("z", "x", 7)
"""
"""
#exemplo dijkstra
grafo = grafo_matriz(["s", "t", "x", "y", "z"])
grafo.adiciona_aresta("s", "t", 10)
grafo.adiciona_aresta("s", "y", 5)
grafo.adiciona_aresta("t", "x", 1)
grafo.adiciona_aresta("t", "y", 2)
grafo.adiciona_aresta("y", "t", 3)
grafo.adiciona_aresta("y", "x", 9)
grafo.adiciona_aresta("y", "z", 2)
grafo.adiciona_aresta("z", "s", 7)
grafo.adiciona_aresta("z", "x", 6)
grafo.adiciona_aresta("x", "z", 4)

#grafo.mostra_grafo()
#grafo.remove_areseta("a", "x")
#grafo.mostra_grafo()
#grafo.grau_de_entrada_e_saida( "z",print_flag = True)
#grafo.indentifica_fontes_e_sumidouros()
#grafo.busca_em_profundidade("w")
#grafo.busca_largura("w")
#grafo.remove_vertice("z")
grafo.mostra_grafo()
#print(grafo.nao_e_geradora())
print("{:_>100}".format("_"))
#grafo.kruskal_sem_direcao(teste_print=False, atualiza_matriz=True)
#grafo.mostra_grafo()
print("{:_>100}".format("_"))
#grafo.prim_sem_direcao("a", teste_print=False, atualiza_matriz=True)
#grafo.Bellman_ford_direcionado(raiz = "s", teste_print=False, atualiza_matriz=True)
grafo.Dijkstra_direcionado("s", teste_print=True, atualiza_matriz=True)
grafo.mostra_grafo()
"""