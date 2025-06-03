
from datetime import datetime, time, timedelta  # Añade timedelta
from PyQt6.QtWidgets import QMessageBox
from database.SQLConexion import conexionDB
from PyQt6.QtCore import QTimer, QTime
import sys

class FichajeLogic:
    def __init__(self, ui, empleado_nombre, empleado_id):
        self.ui = ui
        self.empleado_id = empleado_id
        self.conn = None
        self.cursor = None

         # Configurar el timer para la hora actual
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)  # Actualizar cada 1000ms (1 segundo)
        
        try:
            self.conn, self.cursor = conexionDB()
            if not self.conn:
                QMessageBox.critical(None, "Error", "No se pudo conectar a la base de datos")
                sys.exit(1)
            # Establecer el nombre del empleado
            self.ui.lblNombre.setText(empleado_nombre)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error al inicializar: {str(e)}")
            sys.exit(1)
        
    
    def actualizar_hora(self):
        """Actualiza el label con la hora actual"""
        hora_actual = QTime.currentTime().toString('hh:mm:ss') # Formato 12 horas 
        self.ui.lblHora.setText("Hora actual: " + hora_actual)

    def obtener_empleado_id(self):
        # Obtener el ID del empleado almacenado
        return self.empleado_id
    
    def cargar_datos_fichaje(self):
        
        empleado_id = self.obtener_empleado_id()
        if not empleado_id:
            QMessageBox.warning(None, "Error", "Empleado no identificado")
            return
    
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
        try:
            # Consulta modificada para obtener tiempos directamente
            self.cursor.execute(
                "SELECT hora_entrada, hora_salida, hora_entrada2, hora_salida2 "
                "FROM RegistrosHoras "
                "WHERE empleado_id = %s AND fecha = %s",(empleado_id, fecha_actual)
            )
            resultado = self.cursor.fetchone()
        
            # Función auxiliar para formatear tiempos
            def formatear_hora(hora):
                if hora:
                    if isinstance(hora, str):  # Si ya viene como string
                        return hora[:5] if len(hora) >= 5 else "--:--"
                    elif isinstance(hora, time):  # Si es datetime.time
                        return hora.strftime('%H:%M')
                    elif isinstance(hora, timedelta):  # Si es timedelta
                        total_seconds = hora.total_seconds()
                        hours = int(total_seconds // 3600)
                        minutes = int((total_seconds % 3600) // 60)
                        return f"{hours:02d}:{minutes:02d}"
                return "--:--"
        
            # Actualizar interfaz
            if resultado:
                self.ui.lblEntrada.setText(formatear_hora(resultado['hora_entrada']))
                self.ui.lblSalida.setText(formatear_hora(resultado['hora_salida']))
                self.ui.lblEntrada2.setText(formatear_hora(resultado['hora_entrada2']))
                self.ui.lblSalida2.setText(formatear_hora(resultado['hora_salida2']))
            else:
                self.resetear_labels()
            
        except Exception as e:
            print(f"Error cargando datos: {str(e)}")
            self.resetear_labels()
    
    def resetear_labels(self):
        self.ui.lblEntrada.setText("--:--")
        self.ui.lblSalida.setText("--:--")
        self.ui.lblEntrada2.setText("--:--")
        self.ui.lblSalida2.setText("--:--")

    def registrar_fichaje(self):
        empleado_id = self.obtener_empleado_id()
        if not empleado_id:
            QMessageBox.warning(None, "Advertencia", "No se ha podido identificar al empleado")
            return
        
        ahora = datetime.now().strftime('%H:%M:%S')
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
        try:
            # Verificar estado actual con manejo explícito de NULLs
            self.cursor.execute(
                "SELECT "
                "hora_entrada IS NOT NULL as tiene_entrada, "
                "hora_salida IS NOT NULL as tiene_salida, "
                "hora_entrada2 IS NOT NULL as tiene_entrada2, "
                "hora_salida2 IS NOT NULL as tiene_salida2 "
                "FROM RegistrosHoras "
                "WHERE empleado_id = %s AND fecha = %s",(empleado_id, fecha_actual)
            )
            estado = self.cursor.fetchone()
        
            if not estado:
                # Primer fichaje del día
                self.cursor.execute(
                    "INSERT INTO RegistrosHoras (empleado_id, fecha, hora_entrada) "
                    "VALUES (%s, %s, %s)",(empleado_id, fecha_actual, ahora)
                )
                self.ui.lblEntrada.setText(ahora[:5])
                mensaje = "Entrada registrada"
            
            elif estado['tiene_entrada'] and not estado['tiene_salida']:
                self.cursor.execute(
                    "UPDATE RegistrosHoras SET hora_salida = %s "
                    "WHERE empleado_id = %s AND fecha = %s ",(ahora, empleado_id, fecha_actual)
                )
                self.ui.lblSalida.setText(ahora[:5])
                mensaje = "Salida registrada"
                self.actualizar_total_horas(empleado_id) # actualizar total horas primer turno

            elif estado['tiene_salida'] and not estado['tiene_entrada2']:
                self.cursor.execute(
                    "UPDATE RegistrosHoras SET hora_entrada2 = %s "
                    "WHERE empleado_id = %s AND fecha = %s AND hora_entrada2 IS NULL",(ahora, empleado_id, fecha_actual)
                )
                self.ui.lblEntrada2.setText(ahora[:5])
                mensaje = "Segunda entrada registrada"
            
            elif estado['tiene_entrada2'] and not estado['tiene_salida2']:
                self.cursor.execute(
                "UPDATE RegistrosHoras SET hora_salida2 = %s "
                "WHERE empleado_id = %s AND fecha = %s",(ahora, empleado_id, fecha_actual)
            )
                self.ui.lblSalida2.setText(ahora[:5])
                self.actualizar_total_horas(empleado_id)
                mensaje = "Segunda salida registrada"
            
            else:
                QMessageBox.warning(None, "Aviso", "Ya completó todos los fichajes hoy")
                return
            
            self.conn.commit()
            QMessageBox.information(None, "Éxito", mensaje)
            self.cargar_datos_fichaje()  # Actualizar vista de las horas
        
        except Exception as e:
            self.conn.rollback()
            error_msg = f"Error al registrar: {str(e)}" if str(e) != "0" else "Error en formato de tiempos"
            QMessageBox.critical(None, "Error", error_msg)
            print(f"Error detallado: {e.__class__.__name__}: {str(e)}")
    
    def actualizar_total_horas(self, empleado_id):
        """Calcula y actualiza el total de horas trabajadas"""
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
    
        try:
            # Obtener todos los tiempos registrados como timedelta
            self.cursor.execute(
                "SELECT hora_entrada as he, hora_salida as hs, "
                "hora_entrada2 as he2, hora_salida2 as hs2 "
                "FROM RegistrosHoras "
                "WHERE empleado_id = %s AND fecha = %s",(empleado_id, fecha_actual)
            )
            tiempos = self.cursor.fetchone()
        
            total_horas = 0.0
        
            # Calcular diferencia primera jornada
            if tiempos['he'] and tiempos['hs']:
                if isinstance(tiempos['he'], timedelta) and isinstance(tiempos['hs'], timedelta):
                    total_horas += (tiempos['hs'] - tiempos['he']).total_seconds() / 3600
                else:
                    # Convertir a timedelta si es necesario
                    h_entrada = tiempos['he'].total_seconds() if isinstance(tiempos['he'], timedelta) else 0
                    h_salida = tiempos['hs'].total_seconds() if isinstance(tiempos['hs'], timedelta) else 0
                    total_horas += (h_salida - h_entrada) / 3600
        
            # Calcular diferencia segunda jornada (si existe)
            if tiempos['he2'] and tiempos['hs2']:
                if isinstance(tiempos['he2'], timedelta) and isinstance(tiempos['hs2'], timedelta):
                    total_horas += (tiempos['hs2'] - tiempos['he2']).total_seconds() / 3600
                else:
                    # Convertir a timedelta si es necesario
                    h_entrada2 = tiempos['he2'].total_seconds() if isinstance(tiempos['he2'], timedelta) else 0
                    h_salida2 = tiempos['hs2'].total_seconds() if isinstance(tiempos['hs2'], timedelta) else 0
                    total_horas += (h_salida2 - h_entrada2) / 3600
        
            # Actualizar en la base de datos
            self.cursor.execute(
                "UPDATE RegistrosHoras SET total_horas = %s "
                "WHERE empleado_id = %s AND fecha = %s",(round(total_horas, 2), empleado_id, fecha_actual)
            )
            self.conn.commit()
        
        except Exception as e:
            self.conn.rollback()
            print(f"Error al calcular horas: {str(e)}")
            QMessageBox.warning(None, "Error", f"No se pudieron calcular las horas: {str(e)}")
    
    def __del__(self):
        try:
            self.timer.stop() # Detener Timer de lblHora
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Error al cerrar la conexión: {str(e)}")