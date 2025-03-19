from PyQt6.QtWidgets import QApplication
from MainWindowExt import MainWindowEx

app = QApplication([])
main_window = MainWindowEx()
main_window.show()
app.exec()
