import sys
from PyQt5.QtWidgets import QApplication
from interfazGrafica import GraphVisualizer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphVisualizer()
    window.show()
    sys.exit(app.exec_())
