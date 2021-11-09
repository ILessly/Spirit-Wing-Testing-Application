import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class window(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.resize(200,50)
        self.setWindowTitle("PyQt5")
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hellow World!")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(40,15)
        layout = QtWidgets.QVBoxLayout()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
