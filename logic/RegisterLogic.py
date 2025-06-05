from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import firebase_db
from datetime import datetime
from PyQt6.QtCore import QTimer
from logic.Encrypted_utils import hash_password
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Cargar configuración
load_dotenv()

EMAIL_CONFIG = {
    'SMTP_SERVER': os.getenv('SMTP_SERVER'),
    'SMTP_PORT': int(os.getenv('SMTP_PORT')),
    'EMAIL_ADDRESS': os.getenv('EMAIL_ADDRESS'),
    'EMAIL_PASSWORD': os.getenv('EMAIL_PASSWORD'),
    'FROM_NAME': os.getenv('FROM_NAME')
}

class RegisterLogic:
    def __init__(self, ui, app_manager):
        self.ui = ui
        self.app_manager = app_manager
        self.ui.btnRegistrar.clicked.connect(self.registrar_empleado)
    
    def validar_campos(self):
        nombre = self.ui.txtNombre.text().strip()
        usuario = self.ui.txtUsuario.text().strip()
        password = self.ui.txtPasswd.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        
        if not all([nombre, usuario, password, correo]):
            QMessageBox.warning(None, "Advertencia", "Todos los campos son obligatorios")
            return False
        
        if len(password) < 10 or len(password) > 15:
            QMessageBox.warning(None, "Advertencia", "La contraseña debe tener entre 10 y 15 caracteres")
            return False
            
        return True
    
    def enviar_correo(self, destinatario, usuario, password):
        try:
            msg = MIMEMultipart()
            msg['From'] = f"{EMAIL_CONFIG['FROM_NAME']} <{EMAIL_CONFIG['EMAIL_ADDRESS']}>"
            msg['To'] = destinatario
            msg['Subject'] = "Tus credenciales de acceso"
            
            body = f"""
            <h2>Bienvenido al Sistema de Fichaje</h2>
            <p>Estos son tus datos de acceso:</p>
            <ul>
                <li><strong>Usuario:</strong> {usuario}</li>
                <li><strong>Contraseña:</strong> {password}</li>
            </ul>
            <p>Por seguridad, cambia tu contraseña después del primer acceso.</p>
            """
            
            msg.attach(MIMEText(body, 'html'))
            
            with smtplib.SMTP(EMAIL_CONFIG['SMTP_SERVER'], EMAIL_CONFIG['SMTP_PORT']) as server:
                server.starttls()
                server.login(EMAIL_CONFIG['EMAIL_ADDRESS'], EMAIL_CONFIG['EMAIL_PASSWORD'])
                server.send_message(msg)
                
            return True
        except Exception as e:
            print(f"Error enviando correo: {str(e)}")
            return False
    
    def registrar_empleado(self):
        if not self.validar_campos():
            return
            
        nombre = self.ui.txtNombre.text().strip()
        usuario = self.ui.txtUsuario.text().strip()
        password = self.ui.txtPasswd.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        
        try:
            empleados = firebase_db.read_record("Empleados") or {}
            
            # Verificar si el usuario o correo ya existen
            for emp_data in empleados.values():
                if emp_data.get('usuario') == usuario:
                    QMessageBox.warning(None, "Advertencia", "El nombre de usuario ya está en uso")
                    return
                if emp_data.get('correo') == correo:
                    QMessageBox.warning(None, "Advertencia", "El correo electrónico ya está registrado")
                    return
            
            # Crear nuevo empleado
            nuevo_id = f"emp_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            nuevo_empleado = {
                'nombre': nombre,
                'usuario': usuario,
                'contraseña_hash': hash_password(password),
                'correo': correo,
                'fecha_registro': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            firebase_db.write_record(f"Empleados/{nuevo_id}", nuevo_empleado)
            
            # Enviar correo con credenciales
            if self.enviar_correo(correo, usuario, password):
                QMessageBox.information(None, "Éxito", "Empleado registrado y correo enviado correctamente")
            else:
                QMessageBox.warning(None, "Advertencia", "Empleado registrado pero falló el envío de correo")
            
            self.limpiar_campos()
            QTimer.singleShot(1000, self.app_manager.mostrar_login)
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al registrar empleado: {str(e)}")
    
    def limpiar_campos(self):
        self.ui.txtNombre.clear()
        self.ui.txtUsuario.clear()
        self.ui.txtPasswd.clear()
        self.ui.txtCorreo.clear()