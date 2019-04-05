import math

def find_distance(alpha, beta):
        '''Returns the distance between two points by pythagorean theorum'''
        return math.sqrt(pow(alpha[1]-alpha[0], 2) + pow(beta[1]-beta[0], 2))

def gen_edges(graph):
    edgeslist = []
    for node_alpha in graph.nodes:
        for node_beta in graph.nodes:
            if node_alpha == node_beta:
                continue
            edgeslist.append(Edge(node_alpha, node_beta))
    return edgeslist


def gen_nodes(size):
    node_list = []
    for i in range(0,size):
        for j in range(0,size):
            node_list.append((i,j))

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
    def __init__(self, nodes_param, edges_param = None):
        self._nodes = nodes_param
        self._edges = edges_param
        if not self.edges:
            self.edges = gen_edges(self)

    @property
    def nodes(self):
        return self._nodes
        
    @property
    def edges(self):
        return self._edges
    
    def adjacent_edges(Node n):
        
