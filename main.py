from tracker import TaintTracker
from visualization import plot_taint_graph

if __name__ == "__main__":
    initial_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    tracker = TaintTracker(initial_address)

    taint_graph = tracker.analyze_taint()
    if taint_graph:
        suspicious_nodes = tracker.detect_mixing_services(taint_graph)
        plot_taint_graph(taint_graph, suspicious_nodes)

