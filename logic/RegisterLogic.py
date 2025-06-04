from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import firebase_db
from datetime import datetime
from PyQt6.QtCore import QTimer

class RegisterLogic:
    def __init__(self, ui, app_manager):
        self.ui = ui
        self.app_manager = app_manager
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
            empleados = firebase_db.read_record("Empleados") or {}
            
            # Verificar si el usuario ya existe
            for emp_id, emp_data in empleados.items():
                if emp_data.get('usuario') == usuario:
                    QMessageBox.warning(None, "Advertencia", "El nombre de usuario ya está en uso")
                    return
            
            # Crear nuevo empleado
            nuevo_id = f"emp_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            nuevo_empleado = {
                'nombre': nombre,
                'usuario': usuario,
                'contraseña': password,
                'fecha_registro': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            firebase_db.write_record(f"Empleados/{nuevo_id}", nuevo_empleado)
            
            QMessageBox.information(None, "Éxito", "Empleado registrado correctamente")
            self.limpiar_campos()
            
            # Solo volver al login después de mostrar el mensaje
            QTimer.singleShot(1000, self.app_manager.mostrar_login)
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al registrar empleado: {str(e)}")
    
    def limpiar_campos(self):
        self.ui.txtNombre.clear()
        self.ui.txtUsuario.clear()
        self.ui.txtPasswd.clear()