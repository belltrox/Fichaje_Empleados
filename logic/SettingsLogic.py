from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import firebase_db
from logic.Encrypted_utils import verify_password, hash_password

class SettingsLogic:
    def __init__(self, ui, user_id):
        self.ui = ui
        self.user_id = user_id
        self.ui.btnCambiarContrasena.clicked.connect(self.cambiar_contrasena)
    
    def cambiar_contrasena(self):
        contrasena_actual = self.ui.txtContrasenaActual.text()
        nueva_contrasena = self.ui.txtNuevaContrasena.text()
        confirmacion = self.ui.txtConfirmarContrasena.text()
        
        # Validaciones
        if not all([contrasena_actual, nueva_contrasena, confirmacion]):
            QMessageBox.warning(None, "Error", "Todos los campos son obligatorios")
            return
            
        if nueva_contrasena != confirmacion:
            QMessageBox.warning(None, "Error", "Las contraseñas no coinciden")
            return
            
        if len(nueva_contrasena) < 10 or len(nueva_contrasena) > 15:
            QMessageBox.warning(None, "Error", "La contraseña debe tener entre 10 y 15 caracteres")
            return
            
        try:
            # Obtener usuario de Firebase
            user_data = firebase_db.read_record(f"Empleados/{self.user_id}")
            
            # Verificar contraseña actual
            if not verify_password(user_data['contraseña_hash'], contrasena_actual):
                QMessageBox.warning(None, "Error", "Contraseña actual incorrecta")
                return
                
            # Actualizar contraseña
            firebase_db.update_record(f"Empleados/{self.user_id}", {
                'contraseña_hash': hash_password(nueva_contrasena)
            })
            
            QMessageBox.information(None, "Éxito", "Contraseña cambiada correctamente")
            self.limpiar_campos()
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"No se pudo cambiar la contraseña: {str(e)}")
    
    def limpiar_campos(self):
        self.ui.txtContrasenaActual.clear()
        self.ui.txtNuevaContrasena.clear()
        self.ui.txtConfirmarContrasena.clear()