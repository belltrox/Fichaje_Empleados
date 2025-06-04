from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import firebase_db

class LoginLogic:
    def __init__(self, ui, app_manager):
        self.ui = ui
        self.app_manager = app_manager
        
        # Conectar los botones
        self.ui.btnEntrar.clicked.connect(self.validar_login)
        self.ui.btnIrRegister.clicked.connect(self.ir_a_registro)
    
    def validar_login(self):
        usuario = self.ui.txtUsuario.text().strip()
        password = self.ui.txtPasswd.text().strip()
    
        if not usuario or not password:
            QMessageBox.warning(None, "Advertencia", "Usuario y contraseña son obligatorios")
            return
    
        try:
            empleados = firebase_db.read_record("Empleados") or {}
            empleado_encontrado = None
            
            for emp_id, emp_data in empleados.items():
                if emp_data.get('usuario') == usuario and emp_data.get('contraseña') == password:
                    empleado_encontrado = {
                        'id': emp_id,
                        'nombre': emp_data.get('nombre', '')
                    }
                    break
            
            if empleado_encontrado:
                self.app_manager.mostrar_fichaje(empleado_encontrado['nombre'], empleado_encontrado['id'])
            else:
                QMessageBox.warning(None, "Error", "Usuario no registrado o credenciales incorrectas")
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al validar credenciales: {str(e)}")
    
    def ir_a_registro(self):
        self.app_manager.mostrar_registro()