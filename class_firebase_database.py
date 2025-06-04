import firebase_admin
from firebase_admin import credentials, db

class FirebaseDB:
    def __init__(self, credential_path, database_url):
        # Inicializa Firebase con las credenciales de servicio
        cred = credentials.Certificate(credential_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': database_url
        })

    def write_record(self, path, data):
        # Escribe datos en la base de datos en la ruta especificada
        ref = db.reference(path)
        ref.set(data)

    def read_record(self, path):
        # Lee datos de la ruta especificada en la base de datos
        ref = db.reference(path)
        return ref.get()

    def update_record(self, path, data):
        # Actualiza datos en la ruta especificada
        ref = db.reference(path)
        ref.update(data)

    def delete_record(self, path):
        # Elimina los datos de la ruta especificada
        ref = db.reference(path)
        ref.delete()
