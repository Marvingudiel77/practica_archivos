import tkinter as tk
from tkinter import ttk
from model.inventario_dao import crear_tabla, borrar_tabla
from model.inventario_dao import Inventario, guardar


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_inicio.add_command(
        label="Crear nuevo registro en la base de datos", command=crear_tabla)
    menu_inicio.add_command(
        label="Eliminar registro en la base de datos", command=borrar_tabla)
    menu_inicio.add_command(
        label="Salir de la base de datos", command=root.destroy)

    barra_menu.add_cascade(label="Consultas")
    barra_menu.add_cascade(label="Configuracion")
    barra_menu.add_cascade(label="Ayuda")


class Frame (tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        # self.config(bg="black")
        self.codigo_inventario = None
        self.campos_de_control_inventario()
        self.desabilitar_campos()
        self.tabla_control()

    def campos_de_control_inventario(self):
        # Textos para que indican que debemos ingresar

        self.label_nombre = tk.Label(self, text="Nombre del producto")
        self.label_nombre.config(font=("Arial", 12, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5)

        self.label_existencia = tk.Label(self, text="Existencia")
        self.label_existencia.config(font=("Arial", 12, "bold"))
        self.label_existencia.grid(row=1, column=0, padx=5, pady=5)

        self.label_proveedor = tk.Label(self, text="Proveedor")
        self.label_proveedor.config(font=("Arial", 12, "bold"))
        self.label_proveedor.grid(row=2, column=0, padx=5, pady=5)

        self.label_precio = tk.Label(self, text="Precio")
        self.label_precio.config(font=("Arial", 12, "bold"))
        self.label_precio.grid(row=3, column=0, padx=5, pady=5)

        # cuadros para ingresar los datos

        self.mi_nombre = tk.StringVar()

        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(
            width=50, font=("Arial", 12))
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        self.mi_existencia = tk.StringVar()

        self.entry_existencia = tk.Entry(self, textvariable=self.mi_existencia)
        self.entry_existencia.config(
            width=50, font=("Arial", 12))
        self.entry_existencia.grid(
            row=1, column=1, padx=5, pady=5, columnspan=2)

        self.mi_proveedor = tk.StringVar()

        self.entry_proveedor = tk.Entry(self, textvariable=self.mi_proveedor)
        self.entry_proveedor.config(
            width=50, font=("Arial", 12))
        self.entry_proveedor.grid(
            row=2, column=1, padx=5, pady=5, columnspan=2)

        self.mi_precio = tk.StringVar()

        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio)
        self.entry_precio.config(
            width=50, font=("Arial", 12))
        self.entry_precio.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

        # creacion de los botones

        self.boton_nuevo = tk.Button(
            self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=(
            "Arial", 12, "bold"), fg="yellow", bg="black", cursor="hand2", activebackground="blue")
        self.boton_nuevo.grid(row=5, column=0, padx=2, pady=5)

        self.boton_guardar = tk.Button(
            self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=(
            "Arial", 12, "bold"), fg="sky blue", bg="black", cursor="hand2", activebackground="blue")
        self.boton_guardar.grid(row=5, column=1, padx=2, pady=5)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.desabilitar_campos)
        self.boton_cancelar.config(width=20, font=(
            "Arial", 12, "bold"), fg="yellow", bg="black", cursor="hand2", activebackground="blue")
        self.boton_cancelar.grid(row=5, column=2, padx=2, pady=5)

    def habilitar_campos(self):
        self.mi_nombre.set("")
        self.mi_existencia.set("")
        self.mi_proveedor.set("")
        self.mi_precio.set("")

        self.entry_nombre.config(state="normal")
        self.entry_existencia.config(state="normal")
        self.entry_proveedor.config(state="normal")
        self.entry_precio.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def desabilitar_campos(self):
        self.codigo_inventario = None
        self.mi_nombre.set("")
        self.mi_existencia.set("")
        self.mi_proveedor.set("")
        self.mi_precio.set("")

        self.entry_nombre.config(state="disabled")
        self.entry_existencia.config(state="disabled")
        self.entry_proveedor.config(state="disabled")
        self.entry_precio.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        inventario = Inventario(
            self.mi_nombre.get(),
            self.mi_existencia.get(),
            self.mi_proveedor.get(),
            self.mi_precio.get(),
        )

        guardar(inventario)

        self.desabilitar_campos()

    def tabla_control(self):
        self.tabla = ttk.Treeview(self, column=(
            "Nombre", "Existencia", "Proveedor", "Precio"))
        self.tabla.grid(row=6, column=0, columnspan=4)

        self.tabla.heading("#0", text="Codigo")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Existencia")
        self.tabla.heading("#3", text="Proveedor")
        self.tabla.heading("#4", text="Precio")

        self.tabla.insert("", 0, text="1", values=(
            "Hierro", "2kg", "F.Paz", "2000"))

        # boton Editar

        self.boton_editar = tk.Button(
            self, text="Editar")
        self.boton_editar.config(width=20, font=(
            "Arial", 12, "bold"), fg="yellow", bg="black", cursor="hand2", activebackground="blue")
        self.boton_editar.grid(row=8, column=0, padx=2, pady=5)

        # Boton Eliminar
        self.boton_eliminar = tk.Button(
            self, text="Eliminar")
        self.boton_eliminar.config(width=20, font=(
            "Arial", 12, "bold"), fg="yellow", bg="black", cursor="hand2", activebackground="blue")
        self.boton_eliminar.grid(row=8, column=1, padx=2, pady=5)
