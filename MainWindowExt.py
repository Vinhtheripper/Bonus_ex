from PyQt6 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from LoadFile import load_file, generate_chart


class MainWindowEx(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonLoadFile.clicked.connect(lambda: load_file(self))
        self.pushButton.clicked.connect(lambda: generate_chart(self))
        self.pushButtonSaveChart.clicked.connect(self.save_chart)

    def save_chart(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save chart", "", "HTML Files (*.html)")

        if file_path:
            if hasattr(self, 'fig'):
                self.fig.write_html(file_path)
                QtWidgets.QMessageBox.information(self, 'Notification', 'Chart saved successfully!')
            else:
                QtWidgets.QMessageBox.warning(self, 'Notification', 'Chart saved failed!')
