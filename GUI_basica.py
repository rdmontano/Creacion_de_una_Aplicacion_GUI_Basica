import tkinter as tk
from tkinter import ttk, messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("APLICACION DE GUI BASICA")
root.geometry("400x400")

# Función para agregar datos a la tabla
def agregar_dato():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    if nombre and edad.isdigit():  # Verificar que la edad sea un número
        tree.insert("", tk.END, values=(nombre, edad))
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("ADVERTENCIA", "INGRESE UN NOMBRE VALIDO Y UNA EDAD NUMERICA")

# Función para eliminar un dato seleccionado
def eliminar_dato():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("ADVERTENCIA", "SELECCIONE UN ELEMENTO PARA ELIMINAR")

# Función para editar un dato seleccionado
def editar_dato():
    selected_item = tree.selection()
    if selected_item:
        nombre = entry_nombre.get()
        edad = entry_edad.get()

        if nombre and edad.isdigit():
            tree.item(selected_item, values=(nombre, edad))
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
        else:
            messagebox.showwarning("ADVERTENCIA", "INGRESE UN NOMBRE VALIDO Y UNA EDAD NUMERICA")
    else:
        messagebox.showwarning("ADVERTENCIA", "SELECCIONE UN ELEMENTO PARA EDITAR")

# Crear etiquetas y campos de entrada
label_nombre = tk.Label(root, text="NOMBRE:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

label_edad = tk.Label(root, text="EDAD:")
label_edad.pack(pady=5)
entry_edad = tk.Entry(root)
entry_edad.pack(pady=5)

# Botones de funcionalidad
agregar_button = tk.Button(root, text="AGREGAR", command=agregar_dato)
agregar_button.pack(pady=5)

eliminar_button = tk.Button(root, text="ELIMINAR", command=eliminar_dato)
eliminar_button.pack(pady=5)

editar_button = tk.Button(root, text="EDITAR", command=editar_dato)
editar_button.pack(pady=5)

# Crear el Treeview (tabla) para mostrar los datos
tree = ttk.Treeview(root, columns=("NOMBRE", "EDAD"), show='headings', height=6)
tree.heading("NOMBRE", text="NOMBRE")
tree.heading("EDAD", text="EDAD")
tree.pack(pady=5)

# Iniciar la ventana
root.mainloop()
