# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ventana_principal(object):
    def setupUi(self, ventana_principal):
        if not ventana_principal.objectName():
            ventana_principal.setObjectName(u"ventana_principal")
        ventana_principal.resize(809, 649)
        self.centralwidget = QWidget(ventana_principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contenedor_vistas = QStackedWidget(self.centralwidget)
        self.contenedor_vistas.setObjectName(u"contenedor_vistas")
        self.pagina_login = QWidget()
        self.pagina_login.setObjectName(u"pagina_login")
        self.verticalLayout_4 = QVBoxLayout(self.pagina_login)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 247, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(770, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.lbl_titulo_login = QLabel(self.pagina_login)
        self.lbl_titulo_login.setObjectName(u"lbl_titulo_login")

        self.verticalLayout_2.addWidget(self.lbl_titulo_login)

        self.lbl_instruccion_usuario = QLabel(self.pagina_login)
        self.lbl_instruccion_usuario.setObjectName(u"lbl_instruccion_usuario")

        self.verticalLayout_2.addWidget(self.lbl_instruccion_usuario)

        self.nombre_usuario = QLineEdit(self.pagina_login)
        self.nombre_usuario.setObjectName(u"nombre_usuario")

        self.verticalLayout_2.addWidget(self.nombre_usuario)

        self.btn_login = QPushButton(self.pagina_login)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout_2.addWidget(self.btn_login)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(770, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 247, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.contenedor_vistas.addWidget(self.pagina_login)
        self.pagina_dashboard = QWidget()
        self.pagina_dashboard.setObjectName(u"pagina_dashboard")
        self.verticalLayout_3 = QVBoxLayout(self.pagina_dashboard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.pagina_dashboard)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.txt_busqueda = QLineEdit(self.pagina_dashboard)
        self.txt_busqueda.setObjectName(u"txt_busqueda")

        self.verticalLayout_3.addWidget(self.txt_busqueda)

        self.tbl_tareas = QTableWidget(self.pagina_dashboard)
        self.tbl_tareas.setObjectName(u"tbl_tareas")

        self.verticalLayout_3.addWidget(self.tbl_tareas)

        self.txt_prioridad = QLabel(self.pagina_dashboard)
        self.txt_prioridad.setObjectName(u"txt_prioridad")

        self.verticalLayout_3.addWidget(self.txt_prioridad)

        self.cmb_prioridad = QComboBox(self.pagina_dashboard)
        self.cmb_prioridad.addItem("")
        self.cmb_prioridad.addItem("")
        self.cmb_prioridad.addItem("")
        self.cmb_prioridad.setObjectName(u"cmb_prioridad")

        self.verticalLayout_3.addWidget(self.cmb_prioridad)

        self.cal_fecha = QCalendarWidget(self.pagina_dashboard)
        self.cal_fecha.setObjectName(u"cal_fecha")

        self.verticalLayout_3.addWidget(self.cal_fecha)

        self.txt_tarea_nueva = QLineEdit(self.pagina_dashboard)
        self.txt_tarea_nueva.setObjectName(u"txt_tarea_nueva")

        self.verticalLayout_3.addWidget(self.txt_tarea_nueva)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_agregar_tarea = QPushButton(self.pagina_dashboard)
        self.btn_agregar_tarea.setObjectName(u"btn_agregar_tarea")

        self.horizontalLayout.addWidget(self.btn_agregar_tarea)

        self.btn_eliminar_tarea = QPushButton(self.pagina_dashboard)
        self.btn_eliminar_tarea.setObjectName(u"btn_eliminar_tarea")

        self.horizontalLayout.addWidget(self.btn_eliminar_tarea)

        self.btn_actualizar = QPushButton(self.pagina_dashboard)
        self.btn_actualizar.setObjectName(u"btn_actualizar")

        self.horizontalLayout.addWidget(self.btn_actualizar)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.btn_cerrar_sesion = QPushButton(self.pagina_dashboard)
        self.btn_cerrar_sesion.setObjectName(u"btn_cerrar_sesion")

        self.verticalLayout_3.addWidget(self.btn_cerrar_sesion)

        self.contenedor_vistas.addWidget(self.pagina_dashboard)

        self.verticalLayout.addWidget(self.contenedor_vistas)

        ventana_principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventana_principal)

        QMetaObject.connectSlotsByName(ventana_principal)
    # setupUi

    def retranslateUi(self, ventana_principal):
        ventana_principal.setWindowTitle(QCoreApplication.translate("ventana_principal", u"MainWindow", None))
        self.lbl_titulo_login.setText(QCoreApplication.translate("ventana_principal", u"Iniciar sesi\u00f3n", None))
        self.lbl_instruccion_usuario.setText(QCoreApplication.translate("ventana_principal", u"Nombre de Usuario", None))
        self.btn_login.setText(QCoreApplication.translate("ventana_principal", u"Ingresar", None))
        self.label.setText(QCoreApplication.translate("ventana_principal", u"Buscador", None))
        self.txt_prioridad.setText(QCoreApplication.translate("ventana_principal", u"Prioridad", None))
        self.cmb_prioridad.setItemText(0, QCoreApplication.translate("ventana_principal", u"Alta", None))
        self.cmb_prioridad.setItemText(1, QCoreApplication.translate("ventana_principal", u"Media", None))
        self.cmb_prioridad.setItemText(2, QCoreApplication.translate("ventana_principal", u"Baja", None))

        self.btn_agregar_tarea.setText(QCoreApplication.translate("ventana_principal", u"Agregar", None))
        self.btn_eliminar_tarea.setText(QCoreApplication.translate("ventana_principal", u"Eliminar", None))
        self.btn_actualizar.setText(QCoreApplication.translate("ventana_principal", u"Actualizar", None))
        self.btn_cerrar_sesion.setText(QCoreApplication.translate("ventana_principal", u"Salir", None))
    # retranslateUi

