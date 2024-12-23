import networkx as nx

class FileManager:
    @staticmethod
    def load_graph_from_file(filename):
        graph = nx.Graph()
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if len(data) == 3:  # Nodo1 Nodo2 Peso
                    graph.add_edge(data[0], data[1], weight=float(data[2]))
        return graph

    @staticmethod
    def save_graph_to_file(graph, filename):
        with open(filename, 'w') as file:
            for edge in graph.edges(data=True):
                file.write(f"{edge[0]} {edge[1]} {edge[2]['weight']}\n")
