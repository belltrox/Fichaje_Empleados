# Form implementation generated from reading ui file 'c:\Users\jonat\Desktop\Proyectos Python\Fichaje_Empleados\screens_ui\Register_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(307, 412)
        MainWindow.setStyleSheet("background-color: #afdce4;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 150, 151, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 151, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.txtNombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(70, 110, 151, 31))
        self.txtNombre.setStyleSheet("background-color: white;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.txtNombre.setObjectName("txtNombre")
        self.txtUsuario = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(70, 170, 151, 31))
        self.txtUsuario.setStyleSheet("background-color: white;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.txtUsuario.setObjectName("txtUsuario")
        self.txtPasswd = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtPasswd.setGeometry(QtCore.QRect(70, 290, 151, 31))
        self.txtPasswd.setStyleSheet("background-color: white;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.txtPasswd.setObjectName("txtPasswd")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.btnRegistrar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(110, 360, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet("background-color: #d9d9d9;\n"
"border-radius: 8px;\n"
"padding: 5px;")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 210, 151, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.txtCorreo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtCorreo.setGeometry(QtCore.QRect(70, 230, 151, 31))
        self.txtCorreo.setStyleSheet("background-color: white;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.txtCorreo.setObjectName("txtCorreo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre empleado"))
        self.label_2.setText(_translate("MainWindow", "Nombre usuario"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))
        self.label_4.setText(_translate("MainWindow", "PANEL DE REGISTRO"))
        self.label_5.setText(_translate("MainWindow", "La contreseña debe tener entre 10 y 15 caracteres"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))
        self.label_6.setText(_translate("MainWindow", "Correo"))
