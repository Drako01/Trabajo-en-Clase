from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

import modulo


# Líneas para la imagen de fondo
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = STATIC_ROOT = os.path.join(BASE_DIR, "img" , "futbol.jpg")



# Defino la ventana principal de la aplicación con su fondo
root = Tk()
image2 = Image.open(ruta)
image1 = ImageTk.PhotoImage(image2)
background_label = ttk.Label(root, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=0.4)

# Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title("Centro de Estadísticas del Fútbol Argentino")



# Defino las variables que voy a usar
id = StringVar()
cat = ["A", "B"]
eq_a = [
    "Boca Juniors",
    "River Plate",
    "Independiente",
    "Racing",
    "San Lorenzo",
    "Estudiantes LP",
    "Gimnasia LP",
    "Newell's",
    "Rosario Central",
    "Talleres",
    "Banfield",
    "Lanús",
    "Arsenal",
    "Central Córdoba",
    "Defensa y Justicia",
    "Platense",
    "Patronato",
    "Unión",
    "Atl. Tucumán",
    "Argentinos Jrs.",
    "Colón",
    "Sarmiento",
    "Vélez",
    "Aldosivi",
    "Godoy Cruz",
    "Huracán",
]
l = StringVar()
v = StringVar()
gl = StringVar()
gv = StringVar()
al = StringVar()
av = StringVar()
rl = StringVar()
rv = StringVar()


# Creo las etiquetas, las entradas y los botones
l_cat = ttk.Label(root, text="Categoría: ")
l_l = ttk.Label(root, text="Equipo Local: ")
l_v = ttk.Label(root, text="Equipo Visitante: ")
l_gl = ttk.Label(root, text="Goles Local: ")
l_gv = ttk.Label(root, text="Goles Visitante: ")
l_al = ttk.Label(root, text="Amarillas Local: ")
l_av = ttk.Label(root, text="Amarillas Visitante: ")
l_rl = ttk.Label(root, text="Rojas Local: ")
l_rv = ttk.Label(root, text="Rojas Visitante: ")
l_x = ttk.Label(root, text="Buscar por equipo: ")

e1 = ttk.Combobox(root, values=cat, width=2)
e1.current(0)

e2 = ttk.Combobox(root, values=eq_a, width=15)
e3 = ttk.Combobox(root, values=eq_a, width=15)
e4 = ttk.Entry(root, textvariable=gl, width=2)
e5 = ttk.Entry(root, textvariable=gv, width=2)
e6 = ttk.Entry(root, textvariable=al, width=15)
e7 = ttk.Entry(root, textvariable=av, width=15)
e8 = ttk.Entry(root, textvariable=rl, width=15)
e9 = ttk.Entry(root, textvariable=rv, width=15)

ex = ttk.Combobox(root, values=eq_a, width=15)



# Posiciono etiquetas, botones y controles
l_cat.grid(column=1, row=1)
l_l.grid(column=3, row=1)
l_v.grid(column=5, row=1)
l_gl.grid(column=3, row=2)
l_gv.grid(column=5, row=2)
l_al.grid(column=3, row=3)
l_av.grid(column=5, row=3)
l_rl.grid(column=3, row=4)
l_rv.grid(column=5, row=4)
l_x.grid(column=7, row=7)

e1.grid(column=2, row=1)
e2.grid(column=4, row=1)
e3.grid(column=6, row=1)
e4.grid(column=4, row=2)
e5.grid(column=6, row=2)
e6.grid(column=4, row=3)
e7.grid(column=6, row=3)
e8.grid(column=4, row=4)
e9.grid(column=6, row=4)
ex.grid(column=8, row=7)

tree = ttk.Treeview(root)


tree["columns"] = ("id", "cat", "l", "v", "gl", "gv", "al", "av", "rl", "rv")
tree.column("#0", width=1, minwidth=1, anchor=W)
tree.column("id", width=30, minwidth=30)
tree.column("cat", width=100, minwidth=100, anchor=CENTER)
tree.column("l", width=120, minwidth=120)
tree.column("v", width=120, minwidth=120)
tree.column("gl", width=40, minwidth=40, anchor=CENTER)
tree.column("gv", width=40, minwidth=40, anchor=CENTER)
tree.column("al", width=100, minwidth=100)
tree.column("av", width=100, minwidth=100)
tree.column("rl", width=80, minwidth=80)
tree.column("rv", width=100, minwidth=100)

tree.heading("id", text="ID")
tree.heading("cat", text="Categoría")
tree.heading("l", text="Local")
tree.heading("v", text="Visitante")
tree.heading("gl", text="Goles Local")
tree.heading("gv", text="Goles Visita")
tree.heading("al", text="Amarillas Local")
tree.heading("av", text="Amarillas Visita")
tree.heading("rl", text="Rojas Local")
tree.heading("rv", text="Rojas Visita")





# Creo el treeview

style = ttk.Style(root)
style.theme_use("clam")
style.configure(
    "Treeview", background="#267830", fieldbackground="#5FE884", foreground="white"
)
style.configure(
    "Treeview.Heading",
    background="#215227",
    fieldbackground="#5FE884",
    foreground="white",
    font=("Calibri", 10, "bold"),
)
style.configure(
    "Treeview.Heading.#3",
    background="yellow",
    fieldbackground="yellow",
    foreground="black",
)

tree.grid(column=0, row=9, columnspan=15)

b_agregar = ttk.Button(
    root,
    text="Insertar",
    command=lambda: modulo.fc_insertar(
        modulo.con,
        e1.get(),
        e2.get(),
        e3.get(),
        gl.get(),
        gv.get(),
        al.get(),
        av.get(),
        rl.get(),
        rv.get(),
    ),
)
b_borrar = ttk.Button(root, text="Borrar", command=modulo.fc_borrar)
b_consulta_a = ttk.Button(
    root, text="Datos Cat. A", command=lambda: modulo.fc_consultar(modulo.con, cat[0])
)
b_consulta_b = ttk.Button(
    root, text="Datos Cat. B", command=lambda: modulo.fc_consultar(modulo.con, cat[1])
)
b_editar = ttk.Button(
    root,
    text="Editar",
    command=lambda: modulo.fc_editar(
        modulo.con,
        e1.get(),
        e2.get(),
        e3.get(),
        gl.get(),
        gv.get(),
        al.get(),
        av.get(),
        rl.get(),
        rv.get(),
    ),
)



b_filtrar = ttk.Button(root, text="Buscar", command=lambda: modulo.filtrar(modulo.con, ex.get()))
b_salir = ttk.Button(root, text="Salir", command=modulo.salir)


b_agregar.grid(column=2, row=5, pady=10)
b_borrar.grid(column=3, row=5)
b_editar.grid(column=4, row=5)
b_consulta_a.grid(column=2, row=7)
b_consulta_b.grid(column=4, row=7)
b_filtrar.grid(column=9, row=7)
b_salir.grid(column=9, row=11)



mainloop()