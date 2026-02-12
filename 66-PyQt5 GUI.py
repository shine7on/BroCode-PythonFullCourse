# PyQt5 = GUI
# GUI: Graphical User Interface

import sys # module of system = acess to vars maintained by interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI")
        self.setGeometry(500, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.jpg"))


def main():
    # app object
    app = QApplication(sys.argv) # sys.argv = pass args to python script
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


