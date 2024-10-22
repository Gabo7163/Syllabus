from PyQt5.QtCore import QObject, pyqtSignal


class Logica(QObject):

    senal_dormir = pyqtSignal()

    def __init__(self):
        super().__init__()

    def revisar_hora(self, hora):
        separado = hora.split(":")
        hora_numerica = int(separado[0]) * 100 + int(separado[1])

        if hora_numerica >= 2000 or hora_numerica <= 500:
            self.senal_dormir.emit()
