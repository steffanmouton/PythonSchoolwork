# Construct a box with 4 nodes, all nodes connected. Box with X in middle. 6 edges. Use position tuples for node data
import math

def find_distance(alpha, beta):
        '''Returns the distance between two points by pythagorean theorum'''
        return math.sqrt(pow(alpha[1]-alpha[0], 2) + pow(beta[1]-beta[0], 2))

def gen_edges(graph):
    edgeslist: []
    for node in 


def gen_nodes(size):
    node_list = []
    for i in range(0,size):
        for j in range(0,size):
            nodelist.append((i,j))

class Node:
    '''Contains data'''
    def __init__(self, value):
        self._data = value

class Edge:
    '''Connection between two nodes'''
    def __init__(self, alpha, beta, relation = None):
        self._points = (alpha, beta)

        if relation:
            self._relation = relation(alpha,beta)

class Graph:
    '''Take in arguments: nodes and edges''' 
    def __init__(self, nodes, edges = None):
        self._nodes = nodes
        self._edges = edges

        @property
        def nodes(self):
            return _nodes
        
        @property
        def edges(self):
            return _edges



# Construct a list of nodes w/ loops and use that list to construct a list of edges -> graph
'''
size = 2
nodelist = gen_nodes(size)
'''
a = Node((0,0))
b = Node((1,1))

eAB = Edge(a, b, find_distance)

math.