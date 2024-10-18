# ========== Menggunakan QMainWindow =============
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
#label = Qlabel("Label", window) # Cara 1
label = QLabel(window)
label.setText("Label1")
label.move(200, 0)

#button = QPushButton("Mybutton", window) # Cara 2
button = QPushButton(window)
button.setText("Button1")

window.show()
app.exec_()