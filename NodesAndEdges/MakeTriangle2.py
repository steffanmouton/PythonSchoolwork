# Construct a Triangle. Points A,B,C and edges AB BC CA.

class Node:
    def __init__(self, data):
        self._value = data

class Edge:
    def __init__(self, first, second, rel):
        self._points = (first, second)
        self._val = rel


class Graph:
    '''Take in arguments: nodes and edges''' 
    def __init__(self):
        self._nodes = []
        self._edges = []

A = Node("A")
B = Node("B")
C = Node("C")
nodelist = [A, B, C]

ABedge = Edge(A, B, 5)
BCedge = Edge(B, C, 5)
CAedge = Edge(C, A, 5)
edgelist = [ABedge, BCedge, CAedge]

triangle = Graph()

# Demeter that ho
triangle._nodes = nodelist

triangle._edges = edgelist

wait = "pause"