import tkinter as tk

# Crea una ventana
ventana = tk.Tk()
ventana.title("Texto en el Centro")


# Obtiene las dimensiones de la ventana
ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()

# Crea un widget Label con el texto que desees mostrar
texto = "Texto en el centro"
label = tk.Label(ventana, text=texto)

# Coloca el widget Label en el centro de la ventana
label.place(x=(ancho_ventana - label.winfo_reqwidth()) / 2, y=(alto_ventana - label.winfo_reqheight()) / 2)

# Inicia el bucle principal de tkinter
ventana.mainloop()
