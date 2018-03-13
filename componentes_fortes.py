#!/usr/bin/env python

import sys
import os
from pygraphviz import *


class Tree(object):

    def __init__(self):
        self.data = None
        self.children = []
        self.gone = 0
    
    def add_node(self, obj):
        self.data = obj

    def add_child(self, obj):
        self.children.append(obj)
    


# Definir arvore T
T = Tree()
T.data = "root"

global t


def superBuscaProfundidade( G, r ):
    global t

    t += 1
    r.attr['pre'] = t
    r.attr['estado'] = 1 

    # Vizinhos de r in G
    for i in G.iterneighbors(r):
        v = G.get_node(i)
        if ( int(v.attr['estado']) == 0 ):
            v.pai = r
            superBuscaProfundidade( G, v )
    
    # processe r
    r.attr['estado'] = 2
    t += 1
    r.attr['pos'] = t
            


def buscaProfundidade( G ):
    global t
    
    for i in G:
        n = G.get_node(i)
        n.attr['estado'] = 0;

    t = 0 

    for i in G:
        v = G.get_node(i)
        if ( int(v.attr['estado']) == 0 ):
            v.attr['pai'] = 'raiz' # raiz ?
            nem_to_usando = superBuscaProfundidade( G, v )



# Com arvore T 
def masterBuscaProfundidade( G, r ):
    r.attr['estado'] = 1 

    T = Tree()
    T.add_node(r)

    # Vizinhos de r in G
    #for i in G.iterneighbors(r):
    for i in G.itersucc(r):
        v = G.get_node(i)
        
        if ( int(v.attr['estado']) == 1 and v != r.attr['pai'] ):
            # Adicione {r, v} na arvore T ?
            p = Tree()
            p.add_node(v)
            T.add_child( p )
        
        elif ( int(v.attr['estado']) == 0 ):
            v.pai = r
            # Adicione {r, v} na arvore T ?
            p = masterBuscaProfundidade( G, v )
            T.add_child( p )
    
    # processe r
    r.attr['estado'] = 2
            
    return T



# Transpose graph G
def transpose( G ):
    hue = AGraph()
    hue = G.copy()
    for e in G.iteredges():
        hue.add_edge( list(reversed(e)) )
        hue.delete_edge(e)
    
    return hue


def inversaPosOrdem( G ):
    li = []
    for i in G:
        n = G.get_node(i)
        tmp = [ n.attr['pos'], n ]
        li.append(tmp)

    #li.sort(key=lambda x:int(x[0]), reverse=True)
    li.sort(key=lambda x:int(x[0]))

    new = [x[1] for x in li]
    return new


def decompoe( G ):
    
    G_tmp = transpose( G )
    buscaProfundidade( G_tmp )
    l = inversaPosOrdem( G_tmp )

    for i in G:
        n = G.get_node(i)
        n.attr['estado'] = 0;
   
    x = 1
    for i in l:
        if ( G.has_node(i) ):
            v = G.get_node(i)
            if ( int(v.attr['estado']) == 0 ):
                T = Tree()
                T.data = 0
                T = masterBuscaProfundidade( G, v )

            if( T.data ):
                pr = ("\tsubgraph cluster" + str(x) + " {").expandtabs(2)
                print pr
                printaArvre( T, G )
                print ("\t}").expandtabs(2)
                x += 1



# --- Prints ---

# acrescenta em Cluster C
def printaArvre( T, G ):

    for i in T.children:
        printaArvre( i, G )
    
    if ( G.has_node(T.data) ):
        G.delete_node(T.data)
        print ("\t\t" + T.data + ";").expandtabs(2)
    

def printaNomeGrafo( G ):
    s = G.string().expandtabs(2)
    name = ""
    for i in s:
        name = name + i
        if ( i == '{' ):
            break;
    print name


def printaRetiraNomeGrafo( G ):
    s = G.string().expandtabs(2)
    
    ate = 0
    name = ""
    for i in s:
        name = name + i
        ate += 1
        if ( i == '{' ):
            break;

    print ""
    print s[ate+1:]


def printaGrafo( G ):
    print ''
    s = G.string().expandtabs(2)
    print s




# **************************** Main ***************************** #
input_string = ''
for line in sys.stdin:
    input_string = input_string + line

A = AGraph()
G = A.from_string(input_string)
G_ori = G.copy()

printaNomeGrafo( G_ori )

while ( G ):
    decompoe( G )

printaRetiraNomeGrafo( G_ori )
#printaGrafo( G_ori )

