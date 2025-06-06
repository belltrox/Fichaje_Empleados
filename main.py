import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer, Qt
from windows.fichajeWindow import Ui_MainWindow as FichajeUI
from windows.RegisterWindow import Ui_MainWindow as RegisterUI
from windows.loginWindow import Ui_MainWindow as LoginUI
from windows.SettingsWindow import Ui_MainWindow as SettingsUI
from logic.FichajeLogic import FichajeLogic
from logic.RegisterLogic import RegisterLogic
from logic.LoginLogic import LoginLogic
from logic.SettingsLogic import SettingsLogic


class FichajeWindow(QMainWindow):
    def __init__(self, empleado_nombre, empleado_id, app_manager):
        super().__init__()
        self.ui = FichajeUI()
        self.ui.setupUi(self)
        self.empleado_id = empleado_id
        self.empleado_nombre = empleado_nombre
        self.app_manager = app_manager
        
        self.fichaje_logic = FichajeLogic(self.ui, empleado_nombre, empleado_id)
        self.ui.btnFichar.clicked.connect(self.fichaje_logic.registrar_fichaje)
        self.ui.btnFichar.clicked.connect(self.cerrar_con_retraso)
        self.ui.btnAjustes.mousePressEvent = self.on_btnAjustes_clicked
        self.fichaje_logic.cargar_datos_fichaje()
    
    def on_btnAjustes_clicked(self, event):
        self.app_manager.mostrar_ajustes(self.empleado_nombre, self.empleado_id)
        event.accept()
    
    def cerrar_con_retraso(self):
        QTimer.singleShot(2000, self.close)

class SettingsWindow(QMainWindow):
    def __init__(self, empleado_nombre, empleado_id, app_manager):
        super().__init__()
        self.ui = SettingsUI()
        self.ui.setupUi(self)
        self.app_manager = app_manager
        self.empleado_nombre = empleado_nombre  # Guardar atributos
        self.empleado_id = empleado_id          # Guardar atributos
        
        # Configurar campos
        self.ui.lblNombre.setText(empleado_nombre)
        self.ui.lblUsuario.setText(f"ID: {empleado_id}")
        
        # Inyectar lógica
        self.settings_logic = SettingsLogic(self.ui, empleado_id)
        self.ui.btnVolver.clicked.connect(self.volver_a_fichaje)

    def volver_a_fichaje(self):
        self.close()
        self.app_manager.mostrar_fichaje(self.empleado_nombre, self.empleado_id)

class RegisterWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.ui = RegisterUI()
        self.ui.setupUi(self)
        self.app_manager = app_manager
        
        # Inicializar la lógica de registro
        self.register_logic = RegisterLogic(self.ui, self.app_manager)
        
        # Conectar el botón de registro para volver al login después
        self.ui.btnRegistrar.clicked.connect(self.volver_al_login)
    
    def volver_al_login(self):
        self.close()
        self.app_manager.mostrar_login()

class LoginWindow(QMainWindow):
    def __init__(self, app_manager):
        super().__init__()
        self.ui = LoginUI()
        self.ui.setupUi(self)
        self.app_manager = app_manager
        
        # Inicializar la lógica de login
        self.login_logic = LoginLogic(self.ui, app_manager)

class AppManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow(self)
        self.register_window = None
        self.fichaje_window = None
        self.settings_window = None
        self.mostrar_login()
    
    def mostrar_login(self):
        if self.fichaje_window:
            self.fichaje_window.close()
            self.fichaje_window = None
        if self.register_window:
            self.register_window.close()
            self.register_window = None
        
        self.login_window = LoginWindow(self)
        self.login_window.show()
    
    def mostrar_registro(self):
        self.login_window.close()
        self.register_window = RegisterWindow(self)
        self.register_window.show()
    
    def mostrar_fichaje(self, empleado_nombre, empleado_id):
        self.login_window.close()
        if self.register_window:
            self.register_window.close()
        if self.settings_window:
            self.settings_window.close()
        
        self.fichaje_window = FichajeWindow(empleado_nombre, empleado_id, self)
        self.fichaje_window.show()
    
    def mostrar_ajustes(self, empleado_nombre, empleado_id):
        if self.fichaje_window:
            self.fichaje_window.hide()
        if self.settings_window:
            self.settings_window.close()
        
        self.settings_window = SettingsWindow(empleado_nombre, empleado_id, self)
        self.settings_window.show()
    
    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app_manager = AppManager()
    app_manager.run()