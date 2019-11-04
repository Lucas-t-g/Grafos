#coding: utf-8
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
      self.conteudo = conteudo      #referece ao conteudo do vertice
      self.adjacente = []           #os adjacentes ao vertice é uma lista de vertices
   
   def print_vertice(self):
      _str = str(self.conteudo)
      for adj in self.adjacente:
         _str += " -> "+str(adj.conteudo)
      print(_str)

   def adc_aresta(self, vertice_v):
      self.adjacente.append(vertice_v)

class grafo_lista:
   def __init__(self, lista = []):
      self.vertices = lista
   
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
   
   def cria_aresta(self, vertice_v, vertice_u):    #cria vertice direcionar de v para u
      vertice_a = self.busca_vertice(vertice_v)
      vertice_b = self.busca_vertice(vertice_u)
      vertice_a.adc_aresta(vertice_b)
      #vertice_b.adc_aresta(vertice_a) #comentada para ser direcional
   
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
            



#####__INICIO__DA_EXECUÇÃO__#####
grafo = grafo_lista()
grafo.add_vertice("x")
grafo.add_vertice("y")
grafo.add_vertice("z")
grafo.add_vertice("a")
grafo.cria_aresta("x", "a")
grafo.cria_aresta("x", "y")
grafo.cria_aresta("y", "z")
grafo.print_grafo()
#grafo.remove_vertice("a")
grafo.remove_aresta("x", "a")
grafo.print_grafo()

grafo.grau_de_entrada_saida("a", True)

grafo.indentifica_fontes_e_sumidouros()