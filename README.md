**********************************
CI065 

Algoritmos e Teoria dos Grafos  

Primeiro semestre de 2017  

### 3º trabalho - Componentes Fortes ### 
**********************************

**Descrição:**
  - http://www.inf.ufpr.br/renato/ci065/trabalho-3.html


**Algoritmo:**
  - Python
  - Biblioteca pygraphviz (AGraph)


**Lógica:**
  - Decomposição como apresentado em sala: Kosaraju

  * Roda Decompoe( G ), deletando os componentes fortemente conexos que encontrar, até o grafo G estar vazio

> # Decompoe baseado no apresentado em sala
>
>  Decompoe( G ):
>    l <- inversoPosOrdem( G )  
>    Para cada v pertencente a V(G):
>      v.estado <- 0
>    Para cada v pertencente a l:
>      Se v.estado == 0
>        T <- arborescência resultante de uma busca em G a partir de v
>        Imprime G[V(T)] e deleta de G
>
>    inversoPosOrdem( G ):
>      Retorna reverso da pós-ordem da floresta resultante de uma busca em profundidade em G_transposto
    


OBS.: Não funcionou para o exemplo velha.dot
------> Profundidade excedida na recursão.

