from graph import *
# Create graph and traverse it using BFS from Wiki

def BFS(Graph G, Node start):
    discovered_nodes = []
    Q = []
    Q.append(start)

    while len(Q) > 0:
        current = Q.pop(0)
        # Could do a goal check here