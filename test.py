from database.SQLConexion import firebase_db
from datetime import datetime

test_data = {
    "nombre": "TEST",
    "usuario": "test_user",
    "fecha_registro": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}
firebase_db.write_record("Empleados/emp_TEST", test_data)
print("Dato de prueba escrito. Verifica Firebase Console.")