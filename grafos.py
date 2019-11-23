#coding: utf-8

import grafos_lista as gl
import grafos_matriz as gm

def menu():
   print("{:-^40}".format("MENU"))
   print("{:^40}".format("1-para criar grafo por lista"))
   print("{:^40}".format("2-para criar grafo por matriz"))
   print("{:^40}".format("3-para adicionar um vertice"))
   print("{:^40}".format("4-para remover um vertice"))
   print("{:^40}".format("5-para adicionar uma aresta"))
   print("{:^40}".format("6-para remover uma aresta"))
   print("{:^40}".format("7-para converter o grafo"))
   print("{:^40}".format("8-para ver lista de grafos prontos"))
   print("{:^40}".format("9-para visualizar o grafo"))
   print("{:^40}".format("10-para identificar fontes e sumidouros"))
   print("{:^40}".format("11-para ver os graus de entrada e saida"))
   #print("{:^40}".format(""))
   #print("{:^40}".format(""))
   #print("{:^40}".format(""))
   print("{:^40}".format("0-para sair"))
   print("{:-^40}".format("END_MENU"))

def grafos_prontos():
   print("{:-^40}".format("EXEMPLOS"))
   print("{:^40}".format("1-para grafos por listas"))
   print("{:^40}".format("2-para grafos por matriz"))

   entrada1 = eval(input("escolha: "))

   if ( entrada1 == 1 ): #por listas

      print("{:-^40}".format("EXEMPLOS"))
      print("{:^40}".format("1-Busca em Largura"))
      print("{:^40}".format("2-Busca em Profundidade"))
      print("{:^40}".format("3-Algoritmo de Kruskal e Prim"))
      print("{:^40}".format("4-Algoritmo de Bellman-Ford"))
      print("{:-^40}".format("5-Algoritmo de Djikstra"))
      print("{:-^40}".format("END_MENU"))

      entrada2 = eval(input("escolha: "))

      if ( entrada2 == 1 ):   #exemplo busca em largura
         return gl.exemplo_da_busca_em_largura(), "lista"
      if ( entrada2 == 2 ):   #exemplo busca em profundidade
         return gl.exemplo_da_busca_em_profundidade(), "lista"
      if ( entrada2 == 3 ):   #exemplo prim e kruskal
         return gl.exemplo_prim_kruskal(), "lista"
      if ( entrada2 == 4 ):   #exemplo Bellman
         return gl.exemplo_bellman_ford(), "lista"
      if ( entrada2 == 5 ):   #exemplo dijkstra
         return gl.exemplo_djikstra(), "lista"
   
   if ( entrada1 == 2 ): #por matrizes
      print("{:-^40}".format("EXEMPLOS"))
      print("{:^40}".format("1-Busca em Largura"))
      print("{:^40}".format("2-Busca em Profundidade"))
      print("{:^40}".format("3-Algoritmo de Kruskal e Prim"))
      print("{:^40}".format("4-Algoritmo de Bellman-Ford"))
      print("{:-^40}".format("5-Algoritmo de Djikstra"))
      print("{:-^40}".format("END_MENU"))

      entrada2 = eval(input("escolha: "))

      if ( entrada2 == 1 ):   #exemplo busca em largura
         return gm.exemplo_da_busca_em_largura(), "matriz"
      if ( entrada2 == 2 ):   #exemplo busca em profundidade
         return gm.exemplo_da_busca_em_profundidade(), "matriz"
      if ( entrada2 == 3 ):   #exemplo prim e kruskal
         return gm.exemplo_prim_kruskal(), "matriz"
      if ( entrada2 == 4 ):   #exemplo Bellman
         return gm.exemplo_bellman_ford(), "matriz"
      if ( entrada2 == 5 ):   #exemplo dijkstra
         return gm.exemplo_djikstra(), "matriz"




######__START__##############################
on = True
tipo_do_grafo = None

while( on ):
   print("\n")
   menu()
   entrada = eval(input("{:>20}".format("escolha: ")))
   if ( entrada == 0 ):
      on = False

   elif ( entrada == 1 ):  #cria grafo por lista
      print("{:-^40}".format("criando grafo por listas"))
      tipo_do_grafo = "lista"
      grafo = gl.grafo_lista()
      print("{:^40}".format("grafo criado"))

   elif ( entrada == 2 ):  #cria grafo por matriz
      print("{:-^40}".format("criando grafo por matriz"))
      tipo_do_grafo = "matriz"
      grafo = gm.grafo_matriz()
      print("{:^40}".format("grafo criado"))

   elif ( entrada == 3 ):  #adiciona vertice
      print("{:-^40}".format("adicionando vertice"))
      vertice_u = str(input("informe o conteudo do vertice: "))

      if ( tipo_do_grafo == "lista" ):
         grafo.add_vertice(vertice_u)

      elif ( tipo_do_grafo == "matriz" ):
         grafo.adiciona_vertice(vertice_u)

      elif ( tipo_do_grafo == None ):
         print( "primeiro crie um grafo!" )

   elif ( entrada == 4 ):  #remove vertice
      print("{:-^40}".format("removendo vertice"))
      vertice_u = str(input("informe o conteudo do vertice: "))

      if ( tipo_do_grafo == "lista" ):
         grafo.remove_vertice(vertice_u)

      elif ( tipo_do_grafo == "matriz" ):
         grafo.remove_vertice(vertice_u)

      elif ( tipo_do_grafo == None ):
         print( "primeiro crie um grafo!" )

   
   elif ( entrada == 5 ):  #adiciona uma aresta
      print("{:-^40}".format("adicionando aresta"))
      vertice_u = str(input("informe o conteudo do vertice u: "))
      vertice_v = str(input("informe o conteudo do vertice v: "))
      custo = str(input("informe o custo da aresta: "))

      if ( tipo_do_grafo == "lista" ):
         grafo.cria_aresta(vertice_u, vertice_v, custo)

      elif ( tipo_do_grafo == "matriz" ):
         grafo.adiciona_aresta(vertice_u, vertice_v, custo)

      elif ( tipo_do_grafo == None ):
         print( "primeiro crie um grafo!" )

   elif ( entrada == 6 ):  #remove uma aresta
      print("{:-^40}".format("removendo aresta"))
      vertice_u = str(input("informe o conteudo do vertice u: "))
      vertice_v = str(input("informe o conteudo do vertice v: "))

      if ( tipo_do_grafo == "lista" ):
         grafo.remove_aresta(vertice_u, vertice_v)

      elif ( tipo_do_grafo == "matriz" ):
         grafo.remove_aresta(vertice_u, vertice_v)

      elif ( tipo_do_grafo == None ):
         print( "primeiro crie um grafo!" )
   
   elif ( entrada == 8 ):  #ver grafos prontos
      grafo, tipo_do_grafo = grafos_prontos()

   elif ( entrada == 9 ):  #mostrar grafo
      print("{:^40}".format("seu grafo:"))
      if ( tipo_do_grafo == "lista" ):
         grafo.print_grafo()
      elif ( tipo_do_grafo == "matriz" ):
         grafo.mostra_grafo()
   
   elif ( entrada == 10 ): #identifica fontes e sumidouros
      print("{:^40}".format("identificando fontes e sumidouros"))
      if ( tipo_do_grafo == "lista" ):
         grafo.indentifica_fontes_e_sumidouros()
      elif ( tipo_do_grafo == "matriz" ):
         grafo.indentifica_fontes_e_sumidouros()
   
   elif ( entrada == 11 ): #identifica grau de entrada e saida
      print("{:^40}".format("identificando graus de entrada e saida"))
      vertice = str(input("informe o conteudo do vertice: "))
      if ( tipo_do_grafo == "lista" ):
         grafo.grau_de_entrada_saida(vertice, True)
      elif ( tipo_do_grafo == "matriz" ):
         grafo.grau_de_entrada_e_saida(vertice, True)
   