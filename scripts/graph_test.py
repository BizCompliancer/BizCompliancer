import sys

sys.path.append("../..")

from PyGenericGraph.src.vertex import Vertex
from PyGenericGraph.src.edge import Edge
from PyGenericGraph.src.graph import Graph

graph = Graph()

#creating vertex for graph
node1 = Vertex("Node1")
node2 = Vertex("Node2")
node3 = Vertex("Node2")

# starting edge and ending edge

node1_node2 = Edge(node1, node2)
node1_node3 = Edge(node1, node3)
node2_node3 = Edge(node2, node3)


# adding vertex to graph

graph.add_vertex(node1)
graph.add_vertex(node2)
graph.add_vertex(node3)

# Creating edges to join all the vertex

graph.add_edge(node1, node2, node1_node2)
graph.add_edge(node1, node3, node1_node3)
graph.add_edge(node2, node3, node2_node3)

# print Graph

print(graph)

root_vertex = graph.root_vertex

for vertex_label, vertex in root_vertex.get_outbound_vertices().items():
    print(vertex_label, vertex)


