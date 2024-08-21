import networkx as nx
from blockchain import Blockchain

class TaintTracker:
    def __init__(self, initial_address):
        self.blockchain = Blockchain()
        self.initial_address = initial_address
        self.tainted_addresses = {initial_address: 100}  # 100% taint

    def analyze_taint(self):
        transactions = self.blockchain.get_address_transactions(self.initial_address)
        if not transactions:
            print("No transactions found.")
            return None

        taint_graph = nx.DiGraph()
        for tx in transactions.get('txs', []):  # Safely access the transactions list
            inputs = tx.get('inputs', [])
            outputs = tx.get('outputs', [])

            total_input_value = sum([input_tx.get('output_value', 0) for input_tx in inputs])
            for input_tx in inputs:
                input_address = input_tx.get('addresses', [None])[0]
                taint_percentage = self.tainted_addresses.get(input_address, 0)
                for output_tx in outputs:
                    if output_tx and isinstance(output_tx, dict):  # Check if output_tx is a valid dictionary
                        output_address = output_tx.get('addresses', [])
                        if output_address and isinstance(output_address, list) and len(output_address) > 0:
                            output_address = output_address[0]  # Safely access the first address
                            output_value = output_tx.get('value', 0)
                            taint_value = (output_value / total_input_value) * taint_percentage if total_input_value else 0
                            self.tainted_addresses[output_address] = taint_value
                            taint_graph.add_edge(input_address, output_address, taint=taint_value)

        return taint_graph

    def detect_mixing_services(self, taint_graph):
        suspicious_tx = []
        for node in taint_graph.nodes:
            out_edges = taint_graph.out_edges(node, data=True)
            if len(out_edges) > 5:  # Simple heuristic for mixers
                suspicious_tx.append(node)
        return suspicious_tx
