# Create graph and traverse it using BFS from Wiki
# Searching Demonstration in Class: Node goes into bucket. Node gets taken out of bucket.
# Node that was removed is added to discovered list. It's edges grab neighboring nodes and add them
# to bucket. Take next node out of bucket, repeat.

def BFS(G, start):
    '''Sort through an entire graph using the breadth-first method. Returns a list of discovered nodes.
        Could add a goal check within.'''
    discovered_nodes = []
    Q = []
    Q.append(start)

    while Q:
        current = Q.pop(0)
        # Could do a goal check here
        for edge in G.adjacent_edges(current):
            for node in edge.points:
                if node not in discovered_nodes:
                    discovered_nodes.append(node)
                    node.parent = current
                    Q.append(node)

    return discovered_nodes
