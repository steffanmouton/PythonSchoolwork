import graph
import search
#Create a square, all nodes connected
n1 = graph.Node(1)
n2 = graph.Node(2)
n3 = graph.Node(3)
n4 = graph.Node(4)

node_test_list = [n1, n2, n3, n4]

chart = graph.Graph(node_test_list)

test = search.BFS(chart, chart.nodes[0])

a = 10
