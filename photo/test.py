from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication([])
window = QMainWindow()

# Chargez l'image
pixmap = QPixmap("coronavirus.jpg")

# Agrandissez l'image de 50%
pixmap = pixmap.scaled(pixmap.width() * 1.5, pixmap.height() * 1.5)

# Créez un label pour afficher l'image
label = QLabel(window)
label.setPixmap(pixmap)

# Redimensionnez le label pour qu'il prenne toute la fenêtre
label.resize(window.size())

# Affichez la fenêtre
window.show()

app.exec_()

