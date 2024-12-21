from PySide6.QtWidgets import QApplication
from frontPage import MyMainWindow
import sys

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = MyMainWindow()
window.show()
sys.exit(app.exec())
