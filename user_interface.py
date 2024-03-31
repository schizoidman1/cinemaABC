from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QMovie
from PyQt5.QtCore import Qt
from asyncqt import asyncSlot
from cinema_lanches import CinemaLanches

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motta Lanches")
        self.setGeometry(100, 100, 400, 200)
        self.setWindowIcon(QIcon("assets/cinema_lanches.png"))

        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap("assets/logo.png"))
        self.logo.setAlignment(Qt.AlignCenter)

        self.label_status = QLabel("Aguardando preparo do lanche...")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.btn_iniciar = QPushButton("Iniciar Preparo")
        self.btn_iniciar.clicked.connect(self.iniciarPreparo)

        self.animacao_preparo = QLabel(self)
        self.animacao_preparo_movie = QMovie("assets/animacao_preparo.gif")
        self.animacao_preparo.setMovie(self.animacao_preparo_movie)
        self.animacao_preparo_movie.start()
        self.animacao_preparo.setAlignment(Qt.AlignCenter)
        self.animacao_preparo.hide()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.animacao_preparo)
        self.layout.addWidget(self.label_status)
        self.layout.addWidget(self.btn_iniciar)

        self.setLayout(self.layout)

        self.cinema = CinemaLanches()

    @asyncSlot()
    async def iniciarPreparo(self):
        self.btn_iniciar.setEnabled(False)
        self.label_status.setText("Preparando pipoca e refrigerante...")
        self.animacao_preparo.show()
        self.btn_iniciar.setText("Preparando...")
        await self.cinema.lanchePronto()
        self.animacao_preparo.hide()
        self.btn_iniciar.setText("Iniciar Preparo Novamente")
        self.btn_iniciar.setEnabled(True)

        if self.cinema.isLanchePronto():
            self.label_status.setText("Lanche Pronto! Aproveite!")
