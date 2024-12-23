import networkx as nx

class GraphLogic:
    def __init__(self):
        self.graph = nx.Graph()  # Grafo no dirigido

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight=1):
        self.graph.add_edge(node1, node2, weight=weight)

    def get_nodes(self):
        return list(self.graph.nodes)

    def get_edges(self):
        return list(self.graph.edges(data=True))

    def get_degree(self, node):
        return self.graph.degree[node]
    def shortest_path(self, start, end):
            # Usando Dijkstra para obtener el camino más corto
            try:
                path = nx.dijkstra_path(self.graph, start, end)
                return path
            except nx.NetworkXNoPath:
                return None  # No hay camino entre los nodos