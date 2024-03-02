import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G = nx.DiGraph()
G.add_nodes_from(['A','B'])
G.add_edges_from([('A','B'),('A','C'),('B','C')])

pagerank1 = nx.pagerank(G, personalization={node: 1.0 for node in G.nodes()})
for node, score in pagerank1.items():
    print(f"The Page rank of node {node} is {score}")


density = nx.density(G)
actual_connection = G.number_of_edges()
connectivity = nx.node_connectivity(G)
page_rank = nx.pagerank(G)

print("The page rank of this graph is", page_rank)
print('The actual connection of this graph is', actual_connection)
print('The network density is', density)
print('The connectivity of this graph is', connectivity)
print("This graph has these nodes",G.nodes())
print("This graph has these edges",G.edges())
print("The node A has these adjacent",G.adj['A'])
print("The node B has these adjacent",G.adj['B'])
print("The node C has these adjacent",G.adj['C'])
print("The node A degree is: ",G.degree['A'])
nx.draw(G, with_labels=True)
plt.show()

