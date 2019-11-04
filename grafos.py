#coding: utf-8
"""
a) Inserir nodo -feito
b) Remover nodo -feito
c) Inserir aresta -feito
d) Remover aresta 
e) Visualizar o grafo -feito
f) Identificar Fontes e sumidouros
g) Calcular o grau de entrada e o grau de saída de um vértice 
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
   
   def cria_aresta(self, vertice_v, vertice_u):
      vertice_a = self.busca_vertice(vertice_v)
      vertice_b = self.busca_vertice(vertice_u)
      vertice_a.adc_aresta(vertice_b)
      vertice_b.adc_aresta(vertice_a)
   
   def remove_vertice(self, vertice_v):
      for vertice in self.vertices:
         for elem in vertice.adjacente:
            if ( elem.conteudo == vertice_v ):
               vertice.adjacente.remove(elem)
         if ( vertice.conteudo == vertice_v ):
            self.vertices.remove(vertice)



#####__INICIO__DA_EXECUÇÃO__#####
grafo = grafo_lista()
grafo.add_vertice("x")
grafo.add_vertice("y")
grafo.add_vertice("z")
grafo.add_vertice("a")
grafo.cria_aresta("x", "a")
grafo.cria_aresta("x", "y")
grafo.print_grafo()
grafo.remove_vertice("a")
grafo.print_grafo()