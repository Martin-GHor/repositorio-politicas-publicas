import networkx as nx
from pyvis.network import Network


def crear_mapa(relations):

    G = nx.DiGraph()

    lineas = relations.split("\n")

    for linea in lineas:

        if "|" in linea:

            actor, relacion, concepto = linea.split("|")

            actor = actor.strip()
            relacion = relacion.strip()
            concepto = concepto.strip()

            G.add_edge(actor, concepto, label=relacion)

    net = Network(height="600px", width="100%", directed=True)

    for nodo in G.nodes:
        net.add_node(nodo, label=nodo)

    for origen, destino, datos in G.edges(data=True):
        net.add_edge(origen, destino, label=datos["label"])

    net.save_graph("graph.html")

    return "graph.html"
    