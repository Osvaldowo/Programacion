import sys
import json
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate # Necesario para el calendario
from interfaz_ui import Ui_ventana_principal 

class TaskMaster(QMainWindow, Ui_ventana_principal):
    """
    Controlador de TaskMaster. Implementa el ciclo CRUD completo:
    Crear, Leer, Editar y Borrar tareas.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(500, 650)
        self.archivo_datos = "usuarios_tareas.json"
        self.datos_globales = self.cargar_todo_el_json()
        self.usuario_actual = "" 
        
        # Variable para saber qué tarea estamos editando (-1 significa ninguna)
        self.indice_edicion = -1
        
        self.btn_login.clicked.connect(self.iniciar_sesion_perfil)
        self.btn_agregar_tarea.clicked.connect(self.agregar_tarea_perfil)
        self.btn_eliminar_tarea.clicked.connect(self.eliminar_tarea_perfil)
        self.tbl_tareas.cellDoubleClicked.connect(self.cargar_datos_para_editar)
        self.btn_actualizar.clicked.connect(self.guardar_cambios_edicion)
        self.btn_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.txt_busqueda.textChanged.connect(self.filtrar_tareas_usuario)

    def cargar_todo_el_json(self):
        """Lee la persistencia de datos en JSON."""
        try:
            if os.path.exists(self.archivo_datos):
                with open(self.archivo_datos, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {} 
        except Exception:
            return {}

    def guardar_todo_el_json(self):
        """Guarda los datos para que la app no inicie vacía."""
        try:
            with open(self.archivo_datos, "w", encoding="utf-8") as f:
                json.dump(self.datos_globales, f, indent=4, ensure_ascii=False)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")

    def iniciar_sesion_perfil(self):
        """Valida el perfil y permite la navegación fluida."""
        nombre = self.nombre_usuario.text().strip().lower()
        if not nombre:
            QMessageBox.warning(self, "Acceso", "Ingresa un usuario.")
            return
        self.usuario_actual = nombre
        if self.usuario_actual not in self.datos_globales:
            self.datos_globales[self.usuario_actual] = []
            self.guardar_todo_el_json()
        self.contenedor_vistas.setCurrentIndex(1)
        self.actualizar_tabla_usuario(self.datos_globales[self.usuario_actual])

    def cargar_datos_para_editar(self, fila, columna):
        """
        Carga la tarea seleccionada en los campos de entrada para editarla.
        Se activa al hacer doble clic en una celda de la tabla.
        """
        self.indice_edicion = fila
        tarea = self.datos_globales[self.usuario_actual][fila]
        
        self.txt_tarea_nueva.setText(tarea["descripcion"])
        self.cmb_prioridad.setCurrentText(tarea["prioridad"])
        
        fecha_qdate = QDate.fromString(tarea["fecha"], "dd/MM/yyyy")
        self.cal_fecha.setSelectedDate(fecha_qdate)
        
        QMessageBox.information(self, "Modo Edición", "Puedes modificar los datos arriba y presionar 'Actualizar'.")

    def guardar_cambios_edicion(self):
        """
        Aplica los cambios realizados a la tarea en edición.
        """
        if self.indice_edicion == -1:
            QMessageBox.warning(self, "Error", "Primero selecciona una tarea de la tabla con doble clic.")
            return

        self.datos_globales[self.usuario_actual][self.indice_edicion] = {
            "descripcion": self.txt_tarea_nueva.text().strip(),
            "prioridad": self.cmb_prioridad.currentText(),
            "fecha": self.cal_fecha.selectedDate().toString("dd/MM/yyyy")
        }
        
        self.guardar_todo_el_json()
        self.actualizar_tabla_usuario(self.datos_globales[self.usuario_actual])

        self.txt_tarea_nueva.clear()
        self.indice_edicion = -1
        QMessageBox.information(self, "Éxito", "Tarea actualizada correctamente.")

    def agregar_tarea_perfil(self):
        """Crea un nuevo registro de tarea."""
        texto = self.txt_tarea_nueva.text().strip()
        if not texto:
            QMessageBox.warning(self, "Error", "La descripción es obligatoria.")
            return

        nueva = {
            "descripcion": texto,
            "prioridad": self.cmb_prioridad.currentText(),
            "fecha": self.cal_fecha.selectedDate().toString("dd/MM/yyyy")
        }
        self.datos_globales[self.usuario_actual].append(nueva)
        self.guardar_todo_el_json()
        self.actualizar_tabla_usuario(self.datos_globales[self.usuario_actual])
        self.txt_tarea_nueva.clear()

    def eliminar_tarea_perfil(self):
        """Elimina el registro seleccionado."""
        fila = self.tbl_tareas.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una tarea.")
            return
        if QMessageBox.question(self, "Confirmar", "¿Borrar tarea?") == QMessageBox.StandardButton.Yes:
            self.datos_globales[self.usuario_actual].pop(fila)
            self.guardar_todo_el_json()
            self.actualizar_tabla_usuario(self.datos_globales[self.usuario_actual])

    def actualizar_tabla_usuario(self, lista):
        """Muestra los datos dinámicamente en la tabla."""
        self.tbl_tareas.setRowCount(len(lista))
        self.tbl_tareas.setColumnCount(3)
        self.tbl_tareas.setHorizontalHeaderLabels(["Descripción", "Prioridad", "Fecha"])
        for i, tarea in enumerate(lista):
            self.tbl_tareas.setItem(i, 0, QTableWidgetItem(tarea["descripcion"]))
            self.tbl_tareas.setItem(i, 1, QTableWidgetItem(tarea["prioridad"]))
            self.tbl_tareas.setItem(i, 2, QTableWidgetItem(tarea["fecha"]))

    def cerrar_sesion(self):
        """Regresa al inicio y limpia la sesión."""
        self.nombre_usuario.clear()
        self.usuario_actual = ""
        self.indice_edicion = -1
        self.contenedor_vistas.setCurrentIndex(0)

    def filtrar_tareas_usuario(self):
        """Lógica de negocio: Algoritmo de búsqueda."""
        termino = self.txt_busqueda.text().lower()
        filtradas = [t for t in self.datos_globales[self.usuario_actual] if termino in t["descripcion"].lower()]
        self.actualizar_tabla_usuario(filtradas)
        
def obtener_ruta_recurso(nombre_archivo):
    """
    Obtiene la ruta absoluta del recurso, compatible con el script .py
    y con el ejecutable .exe de PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        ruta_base = os.path.dirname(sys.executable)
    else:
        ruta_base = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(ruta_base, nombre_archivo)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ruta_estilo = obtener_ruta_recurso("estilo.css")
    
    try:
        with open(ruta_estilo, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"Advertencia: No se encontró el archivo en {ruta_estilo}")

    ventana = TaskMaster()
    ventana.show()
    sys.exit(app.exec())