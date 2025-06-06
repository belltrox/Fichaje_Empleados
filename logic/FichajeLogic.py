from datetime import datetime, time, timedelta
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QTimer, QTime
import sys

class FichajeLogic:
    def __init__(self, ui, empleado_nombre, empleado_id):
        self.ui = ui
        self.empleado_id = empleado_id
        self.empleado_nombre = empleado_nombre
        
        # Configurar el timer para la hora actual
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)
        
        # Establecer el nombre del empleado
        self.ui.lblNombre.setText(empleado_nombre)
    
    def actualizar_hora(self):
        """Actualiza el label con la hora actual"""
        hora_actual = QTime.currentTime().toString('hh:mm:ss')
        self.ui.lblHora.setText("Hora actual: " + hora_actual)

    def obtener_empleado_id(self):
        return self.empleado_id
    
    def cargar_datos_fichaje(self):
        empleado_id = self.obtener_empleado_id()
        if not empleado_id:
            QMessageBox.warning(None, "Error", "Empleado no identificado")
            return
        
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        
        try:
            from database.ConexionFirebase import firebase_db
            path = f"RegistrosHoras/{empleado_id}/{fecha_actual}"
            resultado = firebase_db.read_record(path)
            
            def formatear_hora(hora_str):
                if hora_str:
                    return hora_str[:5] if len(hora_str) >= 5 else "--:--"
                return "--:--"
            
            if resultado:
                self.ui.lblEntrada.setText(formatear_hora(resultado.get('hora_entrada', '')))
                self.ui.lblSalida.setText(formatear_hora(resultado.get('hora_salida', '')))
                self.ui.lblEntrada2.setText(formatear_hora(resultado.get('hora_entrada2', '')))
                self.ui.lblSalida2.setText(formatear_hora(resultado.get('hora_salida2', '')))
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
            from database.ConexionFirebase import firebase_db
            path = f"RegistrosHoras/{empleado_id}/{fecha_actual}"
            registro_actual = firebase_db.read_record(path) or {}
            
            hora_entrada = registro_actual.get('hora_entrada')
            hora_salida = registro_actual.get('hora_salida')
            hora_entrada2 = registro_actual.get('hora_entrada2')
            hora_salida2 = registro_actual.get('hora_salida2')
            
            if not hora_entrada:
                # Primer fichaje del día
                data = {
                    'hora_entrada': ahora,
                    'empleado_id': empleado_id,
                    'empleado_nombre': self.empleado_nombre,
                    'fecha': fecha_actual
                }
                firebase_db.write_record(path, data)
                self.ui.lblEntrada.setText(ahora[:5])
                mensaje = "Entrada registrada"
            
            elif hora_entrada and not hora_salida:
                data = {'hora_salida': ahora}
                firebase_db.update_record(path, data)
                self.ui.lblSalida.setText(ahora[:5])
                mensaje = "Salida registrada"
                self.actualizar_total_horas(empleado_id)
            
            elif hora_salida and not hora_entrada2:
                data = {'hora_entrada2': ahora}
                firebase_db.update_record(path, data)
                self.ui.lblEntrada2.setText(ahora[:5])
                mensaje = "Segunda entrada registrada"
            
            elif hora_entrada2 and not hora_salida2:
                data = {'hora_salida2': ahora}
                firebase_db.update_record(path, data)
                self.ui.lblSalida2.setText(ahora[:5])
                self.actualizar_total_horas(empleado_id)
                mensaje = "Segunda salida registrada"
            
            else:
                QMessageBox.warning(None, "Aviso", "Ya completó todos los fichajes hoy")
                return
            
            QMessageBox.information(None, "Éxito", mensaje)
            self.cargar_datos_fichaje()
        
        except Exception as e:
            error_msg = f"Error al registrar: {str(e)}" if str(e) != "0" else "Error en formato de tiempos"
            QMessageBox.critical(None, "Error", error_msg)
            print(f"Error detallado: {e.__class__.__name__}: {str(e)}")
    
    def actualizar_total_horas(self, empleado_id):
        """Calcula y actualiza el total de horas trabajadas"""
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        
        try:
            from database.ConexionFirebase import firebase_db
            path = f"RegistrosHoras/{empleado_id}/{fecha_actual}"
            registro = firebase_db.read_record(path)
            
            if not registro:
                return
                
            total_horas = 0.0
            
            # Calcular primera jornada
            if registro.get('hora_entrada') and registro.get('hora_salida'):
                he = datetime.strptime(registro['hora_entrada'], '%H:%M:%S')
                hs = datetime.strptime(registro['hora_salida'], '%H:%M:%S')
                total_horas += (hs - he).total_seconds() / 3600
            
            # Calcular segunda jornada (si existe)
            if registro.get('hora_entrada2') and registro.get('hora_salida2'):
                he2 = datetime.strptime(registro['hora_entrada2'], '%H:%M:%S')
                hs2 = datetime.strptime(registro['hora_salida2'], '%H:%M:%S')
                total_horas += (hs2 - he2).total_seconds() / 3600
            
            # Actualizar en Firebase
            firebase_db.update_record(path, {'total_horas': round(total_horas, 2)})
            
        except Exception as e:
            print(f"Error al calcular horas: {str(e)}")
            QMessageBox.warning(None, "Error", f"No se pudieron calcular las horas: {str(e)}")
    
    def __del__(self):
        try:
            self.timer.stop()
        except Exception as e:
            print(f"Error al detener el timer: {str(e)}")