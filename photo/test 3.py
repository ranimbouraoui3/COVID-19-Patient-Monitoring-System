
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class Ui_Form(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        """Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))"""
        
        # Chargez l'image d'arrière-plan
        pixmap = QPixmap("coronavirus.jpg")

# Agrandissez l'image d'arrière-plan pour qu'elle ait la même taille que la fenêtre principale
        pixmap = pixmap.scaled(Dialog.size())
    
# Créez un label pour afficher l'image d'arrière-plan
        label = QLabel(Dialog)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, Dialog.width(), Dialog.height())
        
        
# create a widget to hold the widgets
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setStyleSheet("background-image: url(:/newPrefix/mer800-600.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layout.addWidget(label)
        """self.texttouspersonne = QtWidgets.QTextEdit(Dialog)
        self.texttouspersonne.setGeometry(QtCore.QRect(20, 110, 761, 481))
        self.texttouspersonne.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.texttouspersonne.setObjectName("texttouspersonne")"""
        self.layout.setAlignment(Qt.AlignCenter)

        
            
        #table
        self.table = QTableWidget(Dialog)
        self.table.setGeometry(10 , 100 , 780 , 490)
        self.table.resize(1300, 500)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 500, 31))
        self.label_5.setStyleSheet("font: 8pt \"Nirmala UI\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"\n")

        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 550, 41))
        self.label_2.setStyleSheet("font: 8pt \"Nirmala UI\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Recherche maladies de chaque personne"))
        self.label_2.setText(_translate("Dialog", "les personnes avec les maladies :"))
        
    def getTable(self):
        return self.table



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
