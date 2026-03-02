import networkx as nx
import matplotlib.pyplot as plt

class TopologyVisualizer:
    def draw(self, edges):
        G = nx.Graph()
        G.add_edges_from(edges)
        nx.draw(G, with_labels=True)
        plt.savefig("topology.png")
