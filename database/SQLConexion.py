import pymysql

def conexionDB():
    try:
        miConexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="dbControlHorario",
            cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
        )
        cur = miConexion.cursor()
        print("Conexión exitosa a la base de datos")
        return miConexion, cur
    except pymysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None

def cerrarConexion(miConexion):
    if miConexion:
        miConexion.close()
        print("Conexión cerrada correctamente")
    else:
        print("No hay conexión activa para cerrar")