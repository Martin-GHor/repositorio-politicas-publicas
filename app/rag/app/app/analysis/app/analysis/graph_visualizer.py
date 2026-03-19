import networkx as nx
from pyvis.network import Network


def build_graph(relations):

    G = nx.DiGraph()

    lines = relations.split("\n")

    for line in lines:

        if "|" in line:

            actor, rel, concept = line.split("|")

            actor = actor.strip()
            rel = rel.strip()
            concept = concept.strip()

            G.add_edge(actor, concept, label=rel)

    net = Network(height="600px", width="100%", directed=True)

    for node in G.nodes:
        net.add_node(node, label=node)

    for edge in G.edges(data=True):
        net.add_edge(edge[0], edge[1], label=edge[2]["label"])

    net.save_graph("graph.html")

    return "graph.html"
    