from pyvis.network import Network


def crear_mapa(relations):

    if not relations:
        return None

    net = Network(height="700px", width="100%", directed=True)

    for rel in relations:

        if len(rel) != 3:
            continue

        source, relation, target = rel

        net.add_node(source)
        net.add_node(target)

        net.add_edge(source, target, label=relation)

    output_file = "knowledge_graph.html"

    net.write_html(output_file)

    return output_file

