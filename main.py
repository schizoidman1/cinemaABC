import sys
import asyncio
from style import stylesheet
from asyncqt import QEventLoop
from user_interface import MainWindow
from PyQt5.QtWidgets import QApplication



def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(stylesheet)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()

if __name__ == "__main__":
    main()
