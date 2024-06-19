from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

app = QApplication([])

# create a main window
main_window = QMainWindow()

# create a widget to hold the widgets
widget = QWidget()
layout = QVBoxLayout()
widget.setLayout(layout)

# create some widgets and add them to the layout
label = QLabel("This is a label")
layout.addWidget(label)

button = QPushButton("This is a button")
layout.addWidget(button)

# set the widget as the central widget of the main window
main_window.setCentralWidget(widget)

# set the layout to center the widgets horizontally and vertically
layout.setAlignment(Qt.AlignCenter)

# show the main window
main_window.show()
app.exec()
