from database.class_firebase_database import FirebaseDB
import os

# Configuración de Firebase
CREDENTIAL_PATH = "fichajeempleados_credentials.json"
DATABASE_URL = "https://fichajeempleados-5b9b1-default-rtdb.europe-west1.firebasedatabase.app/"

# Instancia global de FirebaseDB
firebase_db = FirebaseDB(CREDENTIAL_PATH, DATABASE_URL)

def conexionDB():
    """Función de compatibilidad para mantener la interfaz existente"""
    try:
        print("Conexión exitosa a Firebase")
        return firebase_db, None  # Devuelve la instancia de FirebaseDB y None para el cursor
    except Exception as e:
        print(f"Error al conectar a Firebase: {e}")
        return None, None

def cerrarConexion(miConexion):
    """Función de compatibilidad, no es necesaria para Firebase"""
    print("Firebase no requiere cierre explícito de conexión")