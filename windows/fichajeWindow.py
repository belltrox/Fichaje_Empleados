# Form implementation generated from reading ui file 'c:\Users\jonat\Desktop\Proyectos Python\Fichaje_Empleados\screens_ui\fichaje_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 389)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(410, 100, 321, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.lblHora = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblHora.setGeometry(QtCore.QRect(470, 65, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblHora.setFont(font)
        self.lblHora.setText("")
        self.lblHora.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblHora.setObjectName("lblHora")
        self.lblNombre = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblNombre.setGeometry(QtCore.QRect(40, 160, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lblNombre.setFont(font)
        self.lblNombre.setStyleSheet("background-color: white;\n"
"border-radius: 5px;")
        self.lblNombre.setText("")
        self.lblNombre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.btnFichar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnFichar.setGeometry(QtCore.QRect(70, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btnFichar.setFont(font)
        self.btnFichar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.btnFichar.setStyleSheet("background-color: #d9d9d9;\n"
"border-radius: 6px;\n"
"padding: 5px;\n"
"border: 2px solid rgba(0, 0, 0, 0.2);")
        self.btnFichar.setObjectName("btnFichar")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 100, 131, 16))
        self.label.setStyleSheet("color: green;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 131, 16))
        self.label_2.setStyleSheet("color: red;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 220, 131, 16))
        self.label_3.setStyleSheet("color: green;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 270, 131, 16))
        self.label_4.setStyleSheet("color: red;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lblEntrada = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblEntrada.setGeometry(QtCore.QRect(230, 120, 131, 16))
        self.lblEntrada.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblEntrada.setObjectName("lblEntrada")
        self.lblSalida = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblSalida.setGeometry(QtCore.QRect(230, 170, 131, 16))
        self.lblSalida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSalida.setObjectName("lblSalida")
        self.lblEntrada2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblEntrada2.setGeometry(QtCore.QRect(230, 240, 131, 16))
        self.lblEntrada2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblEntrada2.setObjectName("lblEntrada2")
        self.lblSalida2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblSalida2.setGeometry(QtCore.QRect(230, 290, 131, 16))
        self.lblSalida2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSalida2.setObjectName("lblSalida2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 71, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 90, 131, 111))
        self.label_6.setStyleSheet("background-color: white;\n"
"border-radius: 10px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 210, 131, 111))
        self.label_7.setStyleSheet("background-color: white;\n"
"border-radius: 10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lblFondo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblFondo.setGeometry(QtCore.QRect(-10, -10, 791, 471))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        self.lblFondo.setFont(font)
        self.lblFondo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.lblFondo.setMouseTracking(False)
        self.lblFondo.setStyleSheet("background-color: #afdce4;")
        self.lblFondo.setText("")
        self.lblFondo.setObjectName("lblFondo")
        self.btnAjustes = QtWidgets.QLabel(parent=self.centralwidget)
        self.btnAjustes.setGeometry(QtCore.QRect(700, 50, 21, 21))
        self.btnAjustes.setText("")
        self.btnAjustes.setPixmap(QtGui.QPixmap("c:\\Users\\jonat\\Desktop\\Proyectos Python\\Fichaje_Empleados\\screens_ui\\../../../../Downloads/imgSettings.png"))
        self.btnAjustes.setScaledContents(True)
        self.btnAjustes.setObjectName("btnAjustes")
        self.lblFondo.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.lblNombre.raise_()
        self.btnFichar.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.lblEntrada.raise_()
        self.label_2.raise_()
        self.lblSalida.raise_()
        self.label_3.raise_()
        self.lblEntrada2.raise_()
        self.label_4.raise_()
        self.lblSalida2.raise_()
        self.lblHora.raise_()
        self.calendarWidget.raise_()
        self.btnAjustes.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnFichar.setText(_translate("MainWindow", "FICHAR "))
        self.label.setText(_translate("MainWindow", "Entrada"))
        self.label_2.setText(_translate("MainWindow", "Salida"))
        self.label_3.setText(_translate("MainWindow", "Segunda Entrada"))
        self.label_4.setText(_translate("MainWindow", "Segunda Salida"))
        self.lblEntrada.setText(_translate("MainWindow", "00:00"))
        self.lblSalida.setText(_translate("MainWindow", "00:00"))
        self.lblEntrada2.setText(_translate("MainWindow", "00:00"))
        self.lblSalida2.setText(_translate("MainWindow", "00:00"))
        self.label_5.setText(_translate("MainWindow", "EMPLEADO:"))
