from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget
import matplotlib.pyplot as plt
from networkx import draw_networkx
from file_manager import FileManager
from graph_log import GraphLogic

class GraphVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graph_logic = GraphLogic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Visualizador de Grafos')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Carga o guarda un archivo con grafos")
        layout.addWidget(self.label)

        # Botones
        btn_load = QPushButton("Cargar Grafo")
        btn_load.clicked.connect(self.load_graph)
        layout.addWidget(btn_load)

        btn_save = QPushButton("Guardar Grafo")
        btn_save.clicked.connect(self.save_graph)
        layout.addWidget(btn_save)

        btn_draw = QPushButton("Dibujar Grafo")
        btn_draw.clicked.connect(self.draw_graph)
        layout.addWidget(btn_draw)

        # Entrada para los nodos de partida y destino
        path_layout = QHBoxLayout()
        self.start_node_input = QLineEdit(self)
        self.start_node_input.setPlaceholderText("Nodo de partida")
        path_layout.addWidget(self.start_node_input)

        self.end_node_input = QLineEdit(self)
        self.end_node_input.setPlaceholderText("Nodo de destino")
        path_layout.addWidget(self.end_node_input)

        btn_find_path = QPushButton("Calcular Camino Más Corto")
        btn_find_path.clicked.connect(self.find_shortest_path)
        path_layout.addWidget(btn_find_path)

        layout.addLayout(path_layout)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_graph(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=options)
        if filename:
            self.graph_logic.graph = FileManager.load_graph_from_file(filename)
            self.label.setText(f"Grafo cargado desde: {filename}")

    def save_graph(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=options)
        if filename:
            FileManager.save_graph_to_file(self.graph_logic.graph, filename)
            self.label.setText(f"Grafo guardado en: {filename}")

    def draw_graph(self):
        plt.figure(figsize=(8, 6))
        draw_networkx(self.graph_logic.graph, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

    def find_shortest_path(self):
        start = self.start_node_input.text().strip()
        end = self.end_node_input.text().strip()

        if start and end:
            path = self.graph_logic.shortest_path(start, end)
            if path:
                self.result_label.setText(f"Camino más corto: {' -> '.join(path)}")
            else:
                self.result_label.setText("No hay camino entre los nodos.")
        else:
            self.result_label.setText("Por favor, ingresa ambos nodos.")
