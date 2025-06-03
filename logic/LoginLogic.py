from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import conexionDB

class LoginLogic:
    def __init__(self, ui, app_manager):
        self.ui = ui
        self.app_manager = app_manager
        self.conn, self.cursor = conexionDB()
        if not self.conn:
            QMessageBox.critical(None, "Error", "No se pudo conectar a la base de datos")
            raise Exception("No se pudo conectar a la base de datos")
        
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
            self.cursor.execute(
                "SELECT id, nombre FROM Empleados WHERE usuario = %s AND contraseña = %s",
                (usuario, password)
            )
            empleado = self.cursor.fetchone()
        
            if empleado:
                # Pasar tanto el nombre como el ID del empleado
                self.app_manager.mostrar_fichaje(empleado['nombre'], empleado['id'])
            else:
                QMessageBox.warning(None, "Error", "Usuario no registrado o credenciales incorrectas")
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al validar credenciales: {str(e)}")
    
    def ir_a_registro(self):
        self.app_manager.mostrar_registro()
    
    def __del__(self):
        if self.conn:
            self.conn.close()