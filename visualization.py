import matplotlib.pyplot as plt
import networkx as nx

def plot_taint_graph(taint_graph, suspicious_nodes=None):
    pos = nx.spring_layout(taint_graph)
    plt.figure(figsize=(12, 8))

    node_color = []
    for node in taint_graph.nodes:
        if suspicious_nodes and node in suspicious_nodes:
            node_color.append('red')
        else:
            node_color.append('skyblue')

    nx.draw(taint_graph, pos, with_labels=True, node_size=500, node_color=node_color, font_size=10, font_weight="bold")
    edge_labels = nx.get_edge_attributes(taint_graph, 'taint')
    nx.draw_networkx_edge_labels(taint_graph, pos, edge_labels=edge_labels)

    plt.title("Taint Analysis Graph")
    plt.show()
