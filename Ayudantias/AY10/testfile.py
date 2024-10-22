import sys
import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QHBoxLayout, QLineEdit)

# Usa este archivo para correr los ejemplos!

# Pega aquí la definición de las clases


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instanciar clases/Conectar señales

    sys.exit(app.exec())
