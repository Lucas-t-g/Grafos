#coding: utf-8
"""
a) Inserir nodo -feito
b) Remover nodo -feito
c) Inserir aresta -feito
d) Remover aresta  -feito
e) Visualizar o grafo -feito
f) Identificar Fontes e sumidouros -feito
g) Calcular o grau de entrada e o grau de saída de um vértice -feito
h) Busca em largura -feito
i) busca em profundidade -feito
j) Implmentar os algoritmos Prim e Kruskal
i) Implmentar os algoritmos Bellamn-Ford e Djikstra
"""
class arestas_se:
   def __init__(self, custo, u, v):
      self.custo = custo
      self.u = u
      self.v = v

   def print_arestas_se(self):
      print("({:^6},{:^6},{:^6})".format(self.custo, self.u, self.v,))

class vertice:
   def __init__(self, conteudo):
      self.conteudo = conteudo      #referece ao conteudo do vertice
      self.adjacente = []           #os adjacentes ao vertice é uma lista de vertices
      self.custo_aresta = []
      self.bandeira_de_visita = 0
      self.distancia = None
      self.pai = None
   
   def print_vertice(self):
      _str = str(self.conteudo)
      for adj in self.adjacente:
         _str += " -> "+str(adj.conteudo)
      print(_str)

   def adc_aresta(self, vertice_v, custo = 1):
      self.adjacente.append(vertice_v)
      self.custo_aresta.append(custo)
      
   def busca_profundidade(self, vertice_v):
      #print ( self.conteudo )
      self.bandeira_de_visita = 1
      if ( self.conteudo == vertice_v ):
         #print("achouu")
         return self
      
      else:
         for vertice in self.adjacente:
            if ( vertice.bandeira_de_visita == 0 ):
               aux = vertice.busca_profundidade(vertice_v)
               if ( aux != None):
                  return aux
         return None
   
   def busca_profundidade_2(self):
      print( self.conteudo )
      self.bandeira_de_visita = 1
      for vertice in self.adjacente:
         if ( vertice.bandeira_de_visita == 0):
            vertice.busca_profundidade_2()
            print( "backtrack" )
   
   def busca_largura(self):
      self.bandeira_de_visita = 1      #branco = 0 ; cinza = 1; preto = 2
      self.distancia = 0
      self.pai = None
      lista = [self]
      while ( len(lista) > 0 ):
         vertice_u = lista.pop()
         print("vertice u: ", vertice_u.conteudo)
         for vertice_w in vertice_u.adjacente:
            if ( vertice_w.bandeira_de_visita == 0 ):
               vertice_w.bandeira_de_visita = 1
               vertice_w.distancia = vertice_u.distancia+1
               vertice_w.pai = vertice_u.conteudo
               lista.insert(0, vertice_w)
               print("vertice w: ", vertice_w.conteudo, "distância: ", vertice_w.distancia, "pai: ", vertice_w.pai, "bdv: ", vertice_w.bandeira_de_visita)
   
         vertice_u.bandeira_de_visita = 2


class grafo_lista:
   def __init__(self, lista = []):
      self.vertices = []
      if ( len(lista) > 0 ):
         for elem in lista:
            self.vertices.append(vertice(elem))
   
   def print_grafo(self):
      print("--------------------")
      for vertice in self.vertices:
         vertice.print_vertice()
      print("--------------------")

   def add_vertice(self, conteudo):
      self.vertices.append(vertice(conteudo))

   def busca_vertice(self, vertice_v):
      for vertice in self.vertices:
         if ( vertice.conteudo == vertice_v ):
            return vertice
      return None
   
   def cria_aresta(self, vertice_v, vertice_u, custo = 1):    #cria vertice direcional de v para u
      vertice_a = self.busca_vertice(vertice_v)
      vertice_b = self.busca_vertice(vertice_u)
      vertice_a.adc_aresta(vertice_b, custo)
      #vertice_b.adc_aresta(vertice_a) #comentada para ser direcional

   def cria_aresta_nao_direcional(self, vertice_v, vertice_u, custo = 1):    #cria vertice não direcional entre u e v
      vertice_a = self.busca_vertice(vertice_v)
      vertice_b = self.busca_vertice(vertice_u)
      vertice_a.adc_aresta(vertice_b, custo)
      vertice_b.adc_aresta(vertice_a, custo)
   
   def remove_vertice(self, vertice_v):
      for vertice in self.vertices:
         for elem in vertice.adjacente:
            if ( elem.conteudo == vertice_v ):
               vertice.adjacente.remove(elem)
         if ( vertice.conteudo == vertice_v ):
            self.vertices.remove(vertice)

   def remove_aresta(self, vertice_v, vertice_u):
      for vertice in self.vertices:
         if ( vertice.conteudo == vertice_v ):
            for elem in vertice.adjacente:
               if ( elem.conteudo == vertice_u ):
                  vertice.adjacente.remove(elem)
   
   def grau_de_entrada_saida(self, vertice_v, print_flag = False):
      grau_entrada = 0
      grau_saida = 0
      for vertice in self.vertices:
         if ( vertice.conteudo == vertice_v ):
            grau_saida = len(vertice.adjacente)
         else:
            for elem in vertice.adjacente:
               if ( elem.conteudo == vertice_v ):
                  grau_entrada -= -1
      if (print_flag):
         print("grau de entrada é: ", grau_entrada )
         print("grau de saida é: ", grau_saida )
      return grau_entrada, grau_saida

   def indentifica_fontes_e_sumidouros(self):
      for vertice in self.vertices:
         grau_entrada, grau_saida = self.grau_de_entrada_saida(vertice.conteudo)
         _str = "vértice "+str(vertice.conteudo)
         if ( grau_entrada == 0 ):
            _str += " é fonte"
         if ( grau_saida == 0 ):
            _str += " é sumidouro"
         print(_str)
   
   def lista_arestas(self):
      lista_arestas = []
      for vertice in self.vertices:
         for i in range(len(vertice.adjacente)):
            nova_aresta = arestas_se(vertice.custo_aresta[i], vertice.conteudo, vertice.adjacente[i].conteudo)
            ja_esta = False
            for aresta in lista_arestas:
               if ( (nova_aresta.u == aresta.u and nova_aresta.v == aresta.v) or (nova_aresta.u == aresta.v and nova_aresta.v == aresta.u) ):
                  ja_esta = True
                  break
            if ( not ja_esta ):
               lista_arestas.append( nova_aresta )
      lista_arestas.sort(key=lambda a: a.custo)
      return lista_arestas

   def nao_e_geradora(self):
      for vertice_u in self.vertices:
         for vertice_v in self.vertices:
            if(vertice_u != vertice_v):
               if (vertice_u.busca_profundidade(vertice_v.conteudo == None)):
                  return True
      return False
   
   def zera_visitas(self):
      for vertice in self.vertices:
         vertice.bandeira_de_visita = 0
         vertice.pai = None
         vertice.distancia = float("inf")
   
   def zera_arestas(self):
      for vertice in self.vertices:
         vertice.adjacente = []
   
   def kruskal_sem_direcao(self, teste_print = True, atualiza_matriz = False):
      lista_arestas = self.lista_arestas()
      self.zera_arestas()
      while ( self.nao_e_geradora and len(lista_arestas) > 0 ):
         aresta = lista_arestas.pop(0)
         self.zera_visitas()
         vertice_u = self.busca_vertice(aresta.u)
         if( vertice_u.busca_profundidade(aresta.v) == None ):
            self.cria_aresta_nao_direcional(aresta.u, aresta.v)


   

#####__INICIO__DA_EXECUÇÃO__#####
"""
grafo = grafo_lista()
grafo.add_vertice("x")
grafo.add_vertice("y")
grafo.add_vertice("z")
grafo.add_vertice("a")
grafo.add_vertice("l")
grafo.add_vertice("m")
grafo.add_vertice("n")
grafo.cria_aresta("x", "a")
grafo.cria_aresta("x", "y")
grafo.cria_aresta("y", "z")
grafo.cria_aresta("x", "z")
grafo.cria_aresta("z", "m")
grafo.cria_aresta("n", "n")
grafo.cria_aresta("n", "l")
grafo.cria_aresta("l", "n")
grafo.cria_aresta("l", "x")
grafo.cria_aresta("a", "m")
grafo.cria_aresta("m", "l")
grafo.cria_aresta("y", "a")
grafo.cria_aresta("z", "l")

grafo.cria_aresta("a", "x")
grafo.cria_aresta("m", "n")
grafo.cria_aresta("y", "n")
grafo.cria_aresta("m", "a")
#grafo.print_grafo()
#grafo.remove_vertice("a")
#grafo.remove_aresta("n", "l")
#grafo.print_grafo()
#grafo.grau_de_entrada_saida("x", True)
#grafo.indentifica_fontes_e_sumidouros()
grafo.print_grafo()
#print(grafo.vertices[4].adjacente[0].conteudo)
#grafo.vertices[4].adjacente[0].conteudo = "k"
#grafo.print_grafo()

#grafo.vertices[4].busca_profundidade("z")
"""
grafo = grafo_lista(["a", "b", "c", "d", "e", "f", "g", "h", "i"])
"""
grafo.cria_aresta("r", "s")
grafo.cria_aresta("s", "r")#

grafo.cria_aresta("r", "v")
grafo.cria_aresta("v", "r")#

grafo.cria_aresta("w", "s")
grafo.cria_aresta("s", "w")#

grafo.cria_aresta("t", "w")
grafo.cria_aresta("w", "t")#

grafo.cria_aresta("w", "x")
grafo.cria_aresta("x", "w")#

grafo.cria_aresta("t", "u")
grafo.cria_aresta("u", "t")#

grafo.cria_aresta("t", "x")
grafo.cria_aresta("x", "t")#

grafo.cria_aresta("u", "x")
grafo.cria_aresta("x", "u")#

grafo.cria_aresta("y", "x")
grafo.cria_aresta("x", "y")#

grafo.cria_aresta("y", "u")
grafo.cria_aresta("u", "y")#
"""
grafo.cria_aresta_nao_direcional("a", "b", 4)
grafo.cria_aresta_nao_direcional("b", "c", 8)
grafo.cria_aresta_nao_direcional("c", "d", 7)
grafo.cria_aresta_nao_direcional("d", "e", 9)
grafo.cria_aresta_nao_direcional("e", "f", 10)
grafo.cria_aresta_nao_direcional("f", "g", 2)
grafo.cria_aresta_nao_direcional("g", "h", 1)
grafo.cria_aresta_nao_direcional("h", "a", 8)
grafo.cria_aresta_nao_direcional("b", "h", 11)
grafo.cria_aresta_nao_direcional("h", "i", 7)
grafo.cria_aresta_nao_direcional("i", "c", 2)
grafo.cria_aresta_nao_direcional("c", "f", 4)
grafo.cria_aresta_nao_direcional("i", "g", 6)
grafo.cria_aresta_nao_direcional("d", "f", 14)
grafo.print_grafo()


#grafo.vertices[1].busca_profundidade_2()
#grafo.vertices[0].busca_largura()
#a = grafo.lista_arestas()
#for elem in a:
#   elem.print_arestas_se()

grafo.kruskal_sem_direcao()
grafo.print_grafo()
