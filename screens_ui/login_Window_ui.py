# Form implementation generated from reading ui file 'c:\Users\jonat\Desktop\Proyectos Python\Fichaje_Empleados\screens\login_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 322)
        MainWindow.setStyleSheet("background-color:#afdce4;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 150, 81, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.txtUsuario = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(250, 110, 191, 31))
        self.txtUsuario.setStyleSheet("background-color:#d9d9d9 ;\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtPasswd = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtPasswd.setGeometry(QtCore.QRect(250, 170, 191, 31))
        self.txtPasswd.setStyleSheet("background-color:#d9d9d9 ;\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.txtPasswd.setObjectName("txtPasswd")
        self.btnEntrar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEntrar.setGeometry(QtCore.QRect(300, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btnEntrar.setFont(font)
        self.btnEntrar.setStyleSheet("background-color:#d9d9d9 ;\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.btnEntrar.setObjectName("btnEntrar")
        self.btnIrRegister = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnIrRegister.setGeometry(QtCore.QRect(300, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.btnIrRegister.setFont(font)
        self.btnIrRegister.setStyleSheet("background-color:#d9d9d9 ;\n"
"border-radius: 10px;\n"
"padding: 5px;")
        self.btnIrRegister.setObjectName("btnIrRegister")
        self.lblImagen = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblImagen.setGeometry(QtCore.QRect(-10, -10, 241, 341))
        self.lblImagen.setText("")
        self.lblImagen.setObjectName("lblImagen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))
        self.btnEntrar.setText(_translate("MainWindow", "ENTRAR"))
        self.btnIrRegister.setText(_translate("MainWindow", "REGISTRAR"))
