from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import conexionDB

class RegisterLogic:
    def __init__(self, ui):
        self.ui = ui
        self.conn, self.cursor = conexionDB()
        if not self.conn:
            QMessageBox.critical(None, "Error", "No se pudo conectar a la base de datos")
            raise Exception("No se pudo conectar a la base de datos")
        
        # Conectar el botón de registrar
        self.ui.btnRegistrar.clicked.connect(self.registrar_empleado)
    
    def validar_campos(self):
        nombre = self.ui.txtNombre.text().strip()
        usuario = self.ui.txtUsuario.text().strip()
        password = self.ui.txtPasswd.text().strip()
        
        if not nombre or not usuario or not password:
            QMessageBox.warning(None, "Advertencia", "Todos los campos son obligatorios")
            return False
        
        if len(password) < 10 or len(password) > 15:
            QMessageBox.warning(None, "Advertencia", "La contraseña debe tener entre 10 y 15 caracteres")
            return False
            
        return True
    
    def registrar_empleado(self):
        if not self.validar_campos():
            return
            
        nombre = self.ui.txtNombre.text().strip()
        usuario = self.ui.txtUsuario.text().strip()
        password = self.ui.txtPasswd.text().strip()
        
        try:
            # Verificar si el usuario ya existe
            self.cursor.execute(
                "SELECT id FROM Empleados WHERE usuario = %s",
                (usuario,)
            )
            if self.cursor.fetchone():
                QMessageBox.warning(None, "Advertencia", "El nombre de usuario ya está en uso")
                return
            
            # Insertar nuevo empleado
            self.cursor.execute(
                "INSERT INTO Empleados (nombre, usuario, contraseña) "
                "VALUES (%s, %s, %s)",
                (nombre, usuario, password)
            )
            self.conn.commit()
            
            QMessageBox.information(None, "Éxito", "Empleado registrado correctamente")
            self.limpiar_campos()
            
        except Exception as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Error", f"Error al registrar empleado: {str(e)}")
    
    def limpiar_campos(self):
        self.ui.txtNombre.clear()
        self.ui.txtUsuario.clear()
        self.ui.txtPasswd.clear()
    
    def __del__(self):
        if self.conn:
            self.conn.close()