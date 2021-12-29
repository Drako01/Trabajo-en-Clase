import vista
from vista import *

import re
import sqlite3
from sqlite3 import Error


# Defino funciones para conectar y crear base de datos y tabla
def conectar():
    try:
        con = sqlite3.connect("bbdd_futbol.db")
        return con
    except Error:
        print(Error)


def crear_bbdd():
    try:
        con = sqlite3.connect("bbdd_futbol.db")
        print("Base Creada")
    except Error:
        print(Error)
    finally:
        con.close()


def crear_tabla(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS partidos( id INTEGER PRIMARY KEY AUTOINCREMENT, categoria varchar(5) NOT NULL, local VARCHAR(128) NOT NULL, visitante varchar(128) NOT NULL, goles_local integer(3) NOT NULL, goles_visitante integer(3) NOT NULL, amarillas_local varchar(128), amarillas_visitante varchar(128), rojas_local varchar(128), rojas_visitante varchar(128))"
    )
    print("Tabla Creada")
    con.commit()


# Llamo a las funciones para crear base de datos y tabla
crear_bbdd()
con = conectar()
crear_tabla(con)


# Defino función para agregar partido
def fc_insertar(con, cat, l, v, gl, gv, al, av, rl, rv):
    cadena1 = gl
    cadena2 = gv
    patron = "[0-9]"
    if re.match(patron, cadena1):
        if re.match(patron, cadena2):
            cursorObj = con.cursor()
            instruccion = "INSERT INTO partidos (categoria, local, visitante, goles_local, goles_visitante, amarillas_local, amarillas_visitante, rojas_local, rojas_visitante) VALUES (?,?,?,?,?,?,?,?,?)"
            datos = (cat, l, v, gl, gv, al, av, rl, rv)
            cursorObj.execute(instruccion, datos)
            con.commit()
            fc_consultar(con, cat)
            mensaje("Nuevo partido agregado!")
        else:
            mensaje("Ingrese un número en el campo de goles visitante")
    else:
        mensaje("Ingrese un número en el campo goles local")


# Defino función para mostrar los partidos cargados de cada categoría
def fc_consultar(con, cat):
    try:
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM partidos WHERE categoria=?", cat)
        con.commit()
        resultado = cursorObj.fetchall()
        for i in vista.tree.get_children():
            vista.tree.delete(i)
        for x in resultado:
            vista.tree.insert(
                "",
                "end",
                values=(x[0], x[1], x[2], x[3], x[4],
                        x[5], x[6], x[7], x[8], x[9]),
            )
    except:
        print("No se pudo realizar la consulta")


# Defino función para borrar registros
def fc_borrar():
    item_2 = vista.tree.focus()
    item_3 = vista.tree.item(item_2)
    if item_2:
        id_seleccionado = item_3["values"][0]
        cursorObj = con.cursor()
        instruccion = "DELETE FROM partidos WHERE id=?"
        cursorObj.execute(instruccion, (id_seleccionado,))
        con.commit()
        vista.tree.delete(item_2)
        mensaje("Partido borrado!")
    else:
        mensaje("No se seleccionó registro.")


# Defino función para editar partidos
def fc_editar(con, cat, l, v, gl, gv, al, av, rl, rv):
    item_2 = vista.tree.focus()
    item_3 = vista.tree.item(item_2)
    cadena1 = gl
    cadena2 = gv
    patron = "[0-9]"
    if re.match(patron, cadena1):
        if re.match(patron, cadena2):
            if item_2:
                id_seleccionado = item_3["values"][0]
                cursorObj = con.cursor()
                instruccion = "UPDATE partidos SET (categoria, local, visitante, goles_local, goles_visitante, amarillas_local, amarillas_visitante, rojas_local, rojas_visitante)=(?,?,?,?,?,?,?,?,?) WHERE id=?"
                datos = (cat, l, v, gl, gv, al, av, rl, rv, id_seleccionado)
                cursorObj.execute(instruccion, datos)
                con.commit()
                fc_consultar(con, cat)
                mensaje("Partido editado!")
            else:
                mensaje("No se seleccionó registro.")
        else:
            mensaje("Ingrese un número en el campo de goles visitante")
    else:
        mensaje("Ingrese un número en el campo de goles local")


# Defino función para cuando selecciono un item
def selectItem(a):
    item_2 = vista.tree.focus()
    if item_2:
        item_3 = vista.tree.item(item_2)
        vista.e1.delete(0, END)
        vista.e1.insert(0, item_3["values"][1])
        vista.e2.delete(0, END)
        vista.e2.insert(0, item_3["values"][2])
        vista.e3.delete(0, END)
        vista.e3.insert(0, item_3["values"][3])
        vista.e4.delete(0, END)
        vista.e4.insert(0, item_3["values"][4])
        vista.e5.delete(0, END)
        vista.e5.insert(0, item_3["values"][5])
        vista.e6.delete(0, END)
        vista.e6.insert(0, item_3["values"][6])
        vista.e7.delete(0, END)
        vista.e7.insert(0, item_3["values"][7])
        vista.e8.delete(0, END)
        vista.e8.insert(0, item_3["values"][8])
        vista.e9.delete(0, END)
        vista.e9.insert(0, item_3["values"][9])


# Defino función para notificaciones
def mensaje(texto):
    messagebox.showinfo("Atención!", texto)


# Defino función para filtrar búsqueda por equipo
def filtrar(con, equipo_seleccionado):
    try:
        cursorObj = con.cursor()
        cursorObj.execute(
            "SELECT * FROM partidos WHERE local=? OR visitante=?",
            (equipo_seleccionado, equipo_seleccionado),
        )
        con.commit()
        resultado = cursorObj.fetchall()
        for i in vista.tree.get_children():
            vista.tree.delete(i)
        if resultado:
            for x in resultado:
                vista.tree.insert(
                    "",
                    "end",
                    values=(x[0], x[1], x[2], x[3], x[4],
                            x[5], x[6], x[7], x[8], x[9]),
                )
        else:
            mensaje("No hay regsitros de este equipo.")
    except:
        print("No se pudo realizar la consulta")


# Defino función para salir del programa
def salir():
    vista.root.destroy()
