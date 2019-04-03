# Construct a Triangle. Points A,B,C and edges AB BC CA.

class node:
    def __init__(self, data):
        self.value = data

class edge:
    def __init__(self, first, second, rel):
        self.alpha = first
        self.beta = second
        self.val = rel

class graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

A = node("A")
B = node("B")
C = node("C")
nodelist = [A, B, C]

ABedge = edge(A, B, 5)
BCedge = edge(B, C, 5)
CAedge = edge(C, A, 5)
edgelist = [ABedge, BCedge, CAedge]

Triangle = graph()

Triangle.nodes = nodelist

Triangle.edges = edgelist

wait = "pause"