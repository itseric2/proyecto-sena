import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import turtle
import time
import random
import string
from datetime import datetime
from tkinter import filedialog
from PIL import Image, ImageTk



def mostrar_ventana_principal():
    
    ventana = tk.Tk()
    ventana.title("Programas")
    ventana_secundaria.withdraw()



    morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  
}

    def cl():
        num = simpledialog.askfloat("Ingresar número", "Por favor, ingresa un número:")
        if num is not None:
            logaritmo = math.log(num)
            messagebox.showinfo("Resultado", f"El logaritmo de {num} es {logaritmo:.2f}")

    def sct():
        def calcular_trigonometria():
            numero = float(entrada_numero.get())
            operacion = operacion_var.get()

            if operacion == "Seno":
                resultado = math.sin(math.radians(numero))
            elif operacion == "Coseno":
                resultado = math.cos(math.radians(numero))
            elif operacion == "Tangente":
                resultado = math.tan(math.radians(numero))
            else:
                resultado = "Seleccione una operación válida"

            resultado_label.config(text=f'{operacion}({numero}): {resultado:.4f}')

        ventana = tk.Tk()
        ventana.title("Calculadora Trigonométrica")

        etiqueta_numero = tk.Label(ventana, text="Ingrese un número:")
        etiqueta_numero.pack(pady=10)

        entrada_numero = tk.Entry(ventana)
        entrada_numero.pack()

        operaciones = ["Seno", "Coseno", "Tangente"]
        operacion_var = tk.StringVar()
        operacion_var.set(operaciones[0])

        etiqueta_operacion = tk.Label(ventana, text="Seleccione la operación:")
        etiqueta_operacion.pack()

        operacion_menu = tk.OptionMenu(ventana, operacion_var, *operaciones)
        operacion_menu.pack()

        boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_trigonometria)
        boton_calcular.pack(pady=10)

        resultado_label = tk.Label(ventana, text="")
        resultado_label.pack()

        ventana.mainloop()

    def cf():
        messagebox.showinfo("Información","Factorial Normal: Es un programa el cual al ingresar un número se multiplica por los números anteriores a el número ingresado")
        num = simpledialog.askinteger("Ingresar número", "Por favor, ingresa un número:")
        if num is not None:
            r = 1
            i = 2
            while i <= num:
                r *= i
                i += 1
            messagebox.showinfo("Resultado", f"El factorial de {num} es {r:.2f}")

    def cm():
        messagebox.showinfo("Información","Código Morse: Es un programa el cual al ingresar una palabra convierte cada letra a código morse el cual se basa apartir de puntos y rayas")
        def texto_a_morse(texto):
            texto = texto.upper()
            morse = []
            for letra in texto:
                if letra in morse_code:
                    morse.append(morse_code[letra])
                else:
                    morse.append(' ')
            return ' '.join(morse)

        texto = simpledialog.askstring("Ingresar texto", "Por favor, ingresa un texto:")
        if texto is not None:
            codigo_morse = texto_a_morse(texto)
            messagebox.showinfo("Resultado", f"El código Morse de '{texto}' es: {codigo_morse}")

    def cboh():

        messagebox.showinfo("Información","Códigos(Binario,Octadecimal,Hexadecimal) : Es un programa el cual al ingresar un número se puede elegir a que convertir ya sea binario, octadecimal o hexadecimal    ")

        def convertir_numero():
            numero = int(entrada_numero.get())
            base = base_var.get()

            if base == "Binario":
                resultado = bin(numero)
            elif base == "Octal":
                resultado = oct(numero)
            elif base == "Hexadecimal":
                resultado = hex(numero)
            else:
                resultado = "Seleccione una base válida"

            resultado_label.config(text=f'{base}: {resultado}')

        ventana = tk.Tk()
        ventana.title("Conversor de Números")

        etiqueta_numero = tk.Label(ventana, text="Ingrese un número:")
        etiqueta_numero.pack(pady=10)

        entrada_numero = tk.Entry(ventana)
        entrada_numero.pack()

        bases = ["Binario", "Octal", "Hexadecimal"]
        base_var = tk.StringVar()
        base_var.set(bases[0])  # Establecer el valor predeterminado

        etiqueta_base = tk.Label(ventana, text="Seleccione la base:")
        etiqueta_base.pack()

        base_menu = tk.OptionMenu(ventana, base_var, *bases)
        base_menu.pack()

        boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_numero)
        boton_convertir.pack(pady=10)

        resultado_label = tk.Label(ventana, text="")
        resultado_label.pack()

        ventana.mainloop()

    def gr():
        messagebox.showinfo("Información","Ruleta: Este programa usa Turtle para dibujar un circulo y un boton de girar, al darle click mostrara dentro de la ruleta el número que se halla elegido de manera aleatoria")
        ventana_ruleta = turtle.Screen()
        ventana_ruleta.title("Ruleta de 10 números")
        ruleta = turtle.Turtle()
        ruleta.speed(0)

        def girar_ruleta():
            ruleta.penup()
            ruleta.goto(0, 0)
            ruleta.pendown()
            for i in range(30):
                ruleta.clear()
                numero = random.randint(1, 30)
                ruleta.write(f"Número: {numero}", align="center", font=("Arial", 20, "normal"))
                ventana_ruleta.update()
                time.sleep(0.1)
            ruleta.clear()
            ruleta.write(f"Número: {numero}", align="center", font=("Arial", 20, "normal"))

        ruleta.penup()
        ruleta.goto(0, -200)
        ruleta.pendown()
        ruleta.circle(200)

        boton_girar = turtle.Turtle()
        boton_girar.penup()
        boton_girar.goto(0, -250)
        boton_girar.pendown()
        boton_girar.write("Girar", align="center", font=("Arial", 16, "normal"))

        def clic_girar(x, y):
            if -50 < x < 50 and -260 < y < -240:
                girar_ruleta()

        ventana_ruleta.onclick(clic_girar)
        ventana_ruleta.mainloop()

    def agr():
        gr()

    def cp():

        messagebox.showinfo("Información","Propina: Es un programa el cual al ingresar dos números saca la cantidad de propina que se deberia dar deacuerdo a un porcentaje de el total a pagar")
        monto_factura = simpledialog.askfloat("Monto de la Factura", "Ingrese el monto de la factura:")
        if monto_factura is None:
            return "No se a ingresado el valor"
    

        porcentaje_propina = simpledialog.askfloat("Porcentaje de Propina", "Ingrese el porcentaje de propina:")
        if porcentaje_propina is None:
            return "No se a ingresado el valor"
        propina = (monto_factura * porcentaje_propina) / 100
    
    
        total = monto_factura + propina
    
    
        mensaje = f"Subtotal: ${monto_factura:.2f}\nPropina ({porcentaje_propina}%): ${propina:.2f}\nTotal a pagar: ${total:.2f}"
        messagebox.showinfo("Resultado", mensaje)

    def t():

        messagebox.showinfo("Información","Temporizador: Es un programa el cual al ingresar una cantidad de tiempo en segundos empieza un conteo hacia atras")
        segundos = simpledialog.askinteger("Configurar Temporizador", "Ingresa la duración del temporizador (segundos):")
        if segundos is None:
            return

        ventana_temporizador = tk.Toplevel()
        ventana_temporizador.title("Temporizador")

        tiempo_restante_label = tk.Label(ventana_temporizador, text=f"Tiempo restante: {segundos} segundos", font=("Arial", 16))
        tiempo_restante_label.pack(padx=20, pady=20)

        for i in range(segundos, -1, -1):
            minutos_restantes = i // 60 
            segundos_restantes = i % 60
            mensaje = f"Tiempo restante: {minutos_restantes} minutos {segundos_restantes} segundos"
            tiempo_restante_label.config(text=mensaje)
            ventana_temporizador.update()
            time.sleep(1)

        mensaje = "¡Tiempo agotado!"
        tiempo_restante_label.config(text=mensaje)
        ventana_temporizador.update()
        time.sleep(2)
        ventana_temporizador.destroy()

    def gc():

        messagebox.showinfo("Información","Contraseña: Es un programa el cual al ingresar la longitud que se desea para la contraseña, se genera automaticamente con simbolos, números y letras")
        longitud = simpledialog.askinteger("tamaño de la contraseña", "Ingrese la longitud de la contraseña:")
        if longitud is not None:
            contrasena = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud))
            messagebox.showinfo("Contraseña generada", f"Contraseña generada: {contrasena}")

    def p():

        messagebox.showinfo("Información","Palindromo: Es un programa el cual al ingresar una palabra, lo que hace es devolver la palabra alrevez y revisa si la palabra que se ingreso es igual a cuando se devolvio y con eso nos dice si es palindromo o no es.                                             Curiosidad: Existe una fobia a este tipo de palabras la cual se llama Aibofobia")
        def es_palindromo(palabra):
            palabra = palabra.lower()
            return palabra == palabra[::-1]

        palabra = simpledialog.askstring("Palabra", "Ingrese la palabra:")

        if es_palindromo(palabra):
            messagebox.showinfo("Palabra",f"La palabra {palabra} es palindromo")
        else:
            messagebox.showinfo("Palabra",f"La palabra {palabra} no es palindromo")


    def cdm():

        messagebox.showinfo("Información","Longitudes: Es un programa el cual al ingresar un número pide con un boton desde que se quiere convertir y con otro hacia que se quiere convertir ( por ejemplo de metros a pulgadas )")
        def convertir_longitud():
            try:
                valor = float(entrada_valor.get())
                unidad_desde = variable_desde.get()
                unidad_hacia = variable_hacia.get()

                if unidad_desde == unidad_hacia:
                    resultado = valor
                elif unidad_desde == "Metros":
                    if unidad_hacia == "Centímetros":
                        resultado = valor * 100
                    elif unidad_hacia == "Kilómetros":
                        resultado = valor / 1000
                    elif unidad_hacia == "Pulgadas":
                        resultado = valor * 39.3701
                elif unidad_desde == "Centímetros":
                    if unidad_hacia == "Metros":
                        resultado = valor / 100
                    elif unidad_hacia == "Kilómetros":
                        resultado = valor / 100000
                    elif unidad_hacia == "Pulgadas":
                        resultado = valor / 2.54
                elif unidad_desde == "Kilómetros":
                    if unidad_hacia == "Metros":
                        resultado = valor * 1000
                    elif unidad_hacia == "Centímetros":
                        resultado = valor * 100000
                    elif unidad_hacia == "Pulgadas":
                        resultado = valor * 39370.1
                elif unidad_desde == "Pulgadas":
                    if unidad_hacia == "Metros":
                        resultado = valor / 39.3701
                    elif unidad_hacia == "Centímetros":
                        resultado = valor * 2.54
                    elif unidad_hacia == "Kilómetros":
                        resultado = valor / 39370.1

                etiqueta_resultado.config(text=f"{valor} {unidad_desde} son {resultado} {unidad_hacia}")
            except ValueError:
                etiqueta_resultado.config(text="Ingrese un valor válido")

        raiz = tk.Tk()
        raiz.title("Conversor de Longitud")

        marco = tk.Frame(raiz)
        marco.pack(padx=20, pady=20)

        etiqueta_valor = tk.Label(marco, text="Valor:")
        etiqueta_valor.pack()

        entrada_valor = tk.Entry(marco)
        entrada_valor.pack()

        unidades = ["Metros", "Centímetros", "Kilómetros", "Pulgadas"]

        variable_desde = tk.StringVar()
        variable_desde.set("Metros")
        desde = tk.OptionMenu(marco, variable_desde, *unidades)
        desde.pack()

        variable_hacia = tk.StringVar()
        variable_hacia.set("Centímetros")
        hacia = tk.OptionMenu(marco, variable_hacia, *unidades)
        hacia.pack()

        boton_convertir = tk.Button(marco, text="Convertir", command=convertir_longitud)
        boton_convertir.pack()

        etiqueta_resultado = tk.Label(marco, text="")
        etiqueta_resultado.pack()

        raiz.mainloop()


    def cde():

        messagebox.showinfo("Información","Nacimiento: Es un programa el cual al ingresar el año de nacimiento muestra un mensaje con tu edad ")
        year_actual = datetime.now().year

        while True:
            try:
                year_nacimiento = simpledialog.askinteger("Ingrese año de nacimiento","Por favor, ingresa tu año de nacimiento (ejemplo: 1990): ")
                break
            except ValueError:
                messagebox.showinfo("Entrada no válida","Ingresa un año válido.")

        edad = year_actual - year_nacimiento
        messagebox.showinfo("edad",f"Tienes {edad} años.")

    
    lista = "Elige una opción:\n1. Piedra\n2. Papel\n3. Tijera"

    def get_user_choice():
        user_choice = simpledialog.askinteger("Elige una opción", lista)
        return user_choice

    def get_computer_choice():
        return random.randint(1, 3)

    def play_game():

        messagebox.showinfo("Información","Piedra, Papel, Tijera: Es un programa el cual da a elegir entre 3 opciones al elegir una de esas hace que se elija aleatoriamente para la maquina y nos muestra un mensaje de ganaste-perdiste-empate")
        user_choice = get_user_choice()
        if user_choice is not None and 1 <= user_choice <= 3:
            options = ["piedra", "papel", "tijera"]
            User = options[user_choice - 1]

            computer_choice = get_computer_choice()
            Computer = options[computer_choice - 1]

            messagebox.showinfo("Elecciones", f"Tú eliges: {User}\nPC eligió: {Computer}\n...")

            if User == Computer:
                messagebox.showinfo("Resultado", "Empate")
            elif (User == "piedra" and Computer == "tijera") or (User == "papel" and Computer == "piedra") or (User == "tijera" and Computer == "papel"):
                messagebox.showinfo("Resultado", "Ganaste")
            else:
                messagebox.showinfo("Resultado", "Perdiste")
        else:
            messagebox.showwarning("Error", "Debes elegir una opción válida (1, 2 o 3)")

    def calcular_imc(peso, altura):


        try:
            altura_metros = altura / 100
            imc = peso / (altura_metros ** 2)
            return imc
        except ZeroDivisionError:
            return "Altura no válida"

    def calcular():

        messagebox.showinfo("Información","IMC: Este programa pide ciertos datos y con esos datos calcula el Indice de Masa Corporal")
        try:
            peso = simpledialog.askfloat("Calcular IMC", "Ingrese su peso en kilogramos:")
            altura = simpledialog.askfloat("Calcular IMC", "Ingrese su altura en centímetros:")
            imc = calcular_imc(peso, altura)

            if isinstance(imc, float):
                messagebox.showinfo("Resultado", "Su índice de masa corporal (IMC) es {:.2f}".format(imc))
            else:
                messagebox.showwarning("Resultado", imc)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para peso y altura.")



    AHORCADO = ['''
  +---+
  |     |
        |
        |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
        |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
  |     |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
 /|     |
        |
        |
========='''
'''
  +---+
  O     |
 /|\    |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
 /|\    |
 /      |
        |
=========''',
'''
  +---+
  |     |
  O     |
 /|\    |
 / \    |
        |
=========''']

    palabras = 'valoracion aprenderpython pneumonoultramicroscopicsilicovolcanoconiosis comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()

    def buscarPalabraAleat(listaPalabras):
        palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
        return listaPalabras[palabraAleatoria]

    def displayBoard(palabraSecreta, letraIncorrecta, letraCorrecta):
        ahorcado_idx = min(len(letraIncorrecta), len(AHORCADO) - 1)
        ahorcado = AHORCADO[ahorcado_idx]

        display = ahorcado + "\n\n"
        display += f"Letras incorrectas: {' '.join(letraIncorrecta)}\n\n"

        for letra in palabraSecreta:
            if letra in letraCorrecta:
                display += letra + ' '
            else:
                display += '_ '

        return display

    def elijeLetra(letrasElegidas):
        while True:
            letra = simpledialog.askstring("Adivina una letra", "Elige una letra:")
            letra = letra.lower()

            if len(letra) != 1:
                messagebox.showwarning("Error", "Por favor, ingresa una sola letra.")
            elif letra in letrasElegidas:
                messagebox.showwarning("Error", "Ya has elegido esa letra. Intenta con otra.")
            elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                messagebox.showwarning("Error", "Por favor, elige una letra del alfabeto.")
            else:
                return letra

    def jugar():

        messagebox.showinfo("Información","Ahorcado: El programa pide unas letras y en lo que escribes una letra se colocara en lugar de las rayas si es correcta, si no es correcta se empezara dibujando una persona ahorcada")
        palabraSecreta = buscarPalabraAleat(palabras)
        letraIncorrecta = ""
        letraCorrecta = ""
        finJuego = False

        while True:
            display = displayBoard(palabraSecreta, letraIncorrecta, letraCorrecta)
            messagebox.showinfo("Ahorcado", display)

            letra = elijeLetra(letraIncorrecta + letraCorrecta)

            if letra in palabraSecreta:
                letraCorrecta += letra
                letrasEncontradas = all(letra in letraCorrecta for letra in palabraSecreta)

                if letrasEncontradas:
                    mensaje = f"¡Muy bien! La palabra secreta es '{palabraSecreta}'. ¡Has ganado!"
                    messagebox.showinfo("Ahorcado", mensaje)
                    finJuego = True
            else:
                letraIncorrecta += letra

                if len(letraIncorrecta) == len(AHORCADO) - 1:
                    display = displayBoard(palabraSecreta, letraIncorrecta, letraCorrecta)
                    messagebox.showinfo("Ahorcado", display)
                    mensaje = f"¡Te has quedado sin letras! La palabra era '{palabraSecreta}'."
                    messagebox.showinfo("Ahorcado", mensaje)
                    finJuego = True

            if finJuego:
                respuesta = messagebox.askyesno("Ahorcado", "¿Quieres jugar de nuevo?")
                if respuesta:
                    palabraSecreta = buscarPalabraAleat(palabras)
                    letraIncorrecta = ""
                    letraCorrecta = ""
                    finJuego = False
                else:
                    break

    def bdn():

        messagebox.showinfo("Información","Bloc de Notas: Este programa crea un cuadro en el que se puede escribir nos da 2 botones uno para guardar y otro para abrir archivos, esto permite como dice sus nombres guardar lo que se escribio y asi mismo abrirlo cuando la persona desee")
        def guardar_archivo():
            contenido = texto.get("1.0", "end-1c")
            archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

            if archivo:
                with open(archivo, "w") as file:
                    file.write(contenido)

        def abrir_archivo():
            archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

            if archivo:
                with open(archivo, "r") as file:
                    contenido = file.read()
                    texto.delete("1.0", tk.END)
                    texto.insert(tk.END, contenido)

        v = tk.Tk()
        v.title("Bloc de Notas")

        texto = tk.Text(v)
        texto.pack()

        gby = tk.Button(v, text="Guardar", command=guardar_archivo)
        gby.pack()

        aby = tk.Button(v, text="Abrir", command=abrir_archivo)
        aby.pack()

        v.mainloop()

    def cdt():

        messagebox.showinfo("Información","Temperatura: Este programa asi como el de longitud pide un valor y con dos botones se puede elegir desde que temperatura se quiere pasar, por ejemplo Kelvin a Celsius")
        def convertir():
            try:
                valor = float(ev.get())
                unidad_origen = cuo.get()
                unidad_destino = cud.get()

                if unidad_origen == unidad_destino:
                    resultado = valor
                elif unidad_origen == "Celsius" and unidad_destino == "Fahrenheit":
                    resultado = (valor * 9/5) + 32
                elif unidad_origen == "Celsius" and unidad_destino == "Kelvin":
                    resultado = valor + 273.15
                elif unidad_origen == "Fahrenheit" and unidad_destino == "Celsius":
                    resultado = (valor - 32) * 5/9
                elif unidad_origen == "Fahrenheit" and unidad_destino == "Kelvin":
                    resultado = (valor + 459.67) * 5/9
                elif unidad_origen == "Kelvin" and unidad_destino == "Celsius":
                    resultado = valor - 273.15
                elif unidad_origen == "Kelvin" and unidad_destino == "Fahrenheit":
                    resultado = (valor * 9/5) - 459.67
                else:
                    lr.config(text="Seleccione unidades válidas")

                lr.config(text=f"{valor} {unidad_origen} son {resultado} {unidad_destino}")
            except ValueError:
                lr.config(text="Ingrese un valor válido")

        v = tk.Tk()
        v.title("Conversor de Temperatura")

        f = tk.Frame(v)
        f.pack(padx=20, pady=20)

        lv = tk.Label(f, text="Valor:")
        lv.pack()

        ev = tk.Entry(f)
        ev.pack()

        cuo = tk.StringVar()
        cuo.set("Celsius")

        cud = tk.StringVar()
        cud.set("Fahrenheit")

        o = ["Celsius", "Fahrenheit", "Kelvin"]
        mdo = tk.OptionMenu(f, cuo, *o)
        mdo.pack()

        mdd = tk.OptionMenu(f, cud, *o)
        mdd.pack()

        bc = tk.Button(f, text="Convertir", command=convertir)
        bc.pack()

        lr = tk.Label(f, text="")
        lr.pack()

        v.mainloop()

    def ldt():

        messagebox.showinfo("Información","Lista de Tareas: Este crea un pequeño rectangulo en el cual se puede escribir cualquier cosa y dos botones uno para agregar una tarea esta con lo que se halla escrito, el otro para eliminar una tarea para este se tiene que seleccionar en un cuadro la tarea y despues darle al boton ")
        def agregar_tarea():
            tarea = entry_tarea.get()
            if tarea:
                lista_tareas.insert(tk.END, tarea)
                entry_tarea.delete(0, tk.END)

        def eliminar_tarea():
            seleccion = lista_tareas.curselection()
            if seleccion:
                lista_tareas.delete(seleccion)

        v = tk.Tk()
        v.title("Gestión de Tareas")

        frame = tk.Frame(v)
        frame.pack(padx=20, pady=20)

        entry_tarea = tk.Entry(frame, width=30)
        entry_tarea.grid(row=0, column=0, padx=5, pady=5)

        boton_agregar = tk.Button(frame, text="Agregar Tarea", command=agregar_tarea)
        boton_agregar.grid(row=0, column=1, padx=5, pady=5)

        boton_eliminar = tk.Button(frame, text="Eliminar Tarea", command=eliminar_tarea)
        boton_eliminar.grid(row=0, column=2, padx=5, pady=5)

        lista_tareas = tk.Listbox(frame, width=40, height=10)
        lista_tareas.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        v.mainloop()

    def cps():

        messagebox.showinfo("Información","Tipo de palabra: En este programa se tiene que ingresar una palabra y deacuerdo a unas condiciones se decide que tipo de palabra es, por ejemplo (perro) es una palabra Grave(llana)")
        def clasificar_palabra():
            palabra = entrada_palabra.get().strip().lower()
            num_silabas = contar_silabas(palabra)

            if num_silabas > 3:
                resultado.config(text="Sobreesdrújula")
            elif num_silabas == 3:
                resultado.config(text="Esdrújula")
            elif num_silabas == 2 and palabra[-1] in "aeiouáéíóú":
                resultado.config(text="Grave (Llana)")
            elif num_silabas == 1 and (palabra[-1] in "nrs" or palabra[-2:] in ["st", "sp", "ck"]):
                resultado.config(text="Aguda")
            else:
                resultado.config(text="Grave (Llana)")

        def contar_silabas(palabra):
            vocales = "aeiouáéíóú"
            silabas = 0
            i = 0

            while i < len(palabra):
                if palabra[i] in vocales:
                    silabas += 1
                    while i < len(palabra) and palabra[i] in vocales:
                        i += 1
                else:
                    i += 1

            return silabas

        ventana = tk.Tk()
        ventana.title("Clasificador de Palabras")

        etiqueta = tk.Label(ventana, text="Ingrese una palabra:")
        etiqueta.pack()

        entrada_palabra = tk.Entry(ventana)
        entrada_palabra.pack()

        boton_clasificar = tk.Button(ventana, text="Clasificar", command=clasificar_palabra)
        boton_clasificar.pack()

        resultado = tk.Label(ventana, text="")
        resultado.pack()

        ventana.mainloop()

    def ctt():

        messagebox.showinfo("Información","Tipo de triangulo: En este programa se pide que se ingrese 3 datos y con este se decide bajo ciertas condiciones que tipo de triangulo, por ejemplo se ingresa (60 40 80) sera un triangulo escaleno")
        def calcular_tipo_triangulo():
            angulo1 = float(angulo1_entry.get())
            angulo2 = float(angulo2_entry.get())
            angulo3 = float(angulo3_entry.get())
    
            if angulo1 + angulo2 + angulo3 == 180:
                if angulo1 == angulo2 == angulo3:
                    resultado_label.config(text="Es un triángulo equilátero")
                elif angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3:
                    resultado_label.config(text="Es un triángulo isósceles")
                else:
                    resultado_label.config(text="Es un triángulo escaleno")
            else:
                resultado_label.config(text="No es un triángulo válido")

        ventana = tk.Tk()
        ventana.title("Tipo de Triángulo")

        angulo1_label = tk.Label(ventana, text="Ángulo 1:")
        angulo1_label.pack()
        angulo1_entry = tk.Entry(ventana)
        angulo1_entry.pack()

        angulo2_label = tk.Label(ventana, text="Ángulo 2:")
        angulo2_label.pack()
        angulo2_entry = tk.Entry(ventana)
        angulo2_entry.pack()

        angulo3_label = tk.Label(ventana, text="Ángulo 3:")
        angulo3_label.pack()
        angulo3_entry = tk.Entry(ventana)
        angulo3_entry.pack()

        calcular_button = tk.Button(ventana, text="Calcular", command=calcular_tipo_triangulo)
        calcular_button.pack()

        resultado_label = tk.Label(ventana, text="")
        resultado_label.pack()

        ventana.mainloop()

    def nose():

        messagebox.showinfo("Información","km/h: Este programa calcula la velocidad de un objeto con unos datos ingresados")
        def calcular_velocidad():
            try:
                distancia = float(distancia_entry.get())
                tiempo = float(tiempo_entry.get())

                velocidad = distancia / tiempo

                resultado_label.config(text=f"Velocidad: {velocidad} km/h")
            except ValueError:
                resultado_label.config(text="Error: Ingresa valores numéricos válidos.")

        ventana = tk.Tk()
        ventana.title("Calculadora de Velocidad")
        ventana.geometry("300x150")

        distancia_label = tk.Label(ventana,text="Distancia (km):")
        distancia_label.pack()
        distancia_entry = tk.Entry(ventana)
        distancia_entry.pack()

        tiempo_label = tk.Label(ventana, text="Tiempo (h):")
        tiempo_label.pack()
        tiempo_entry = tk.Entry(ventana)
        tiempo_entry.pack()
        calcular_button = tk.Button(ventana, text="Calcular Velocidad", command=calcular_velocidad)
        calcular_button.pack()
        resultado_label = tk.Label(ventana, text="")
        resultado_label.pack()
        ventana.mainloop()


    ventana.geometry("1359x900")

    marco_botones = tk.Frame(ventana)
    marco_botones.pack(expand=True)

    mensajes = [
    "Programa aleatorio",
    "Logaritmo",
    "Calcular trigonomia",
    "Factorial",
    "Código Morse",
    "Convertir B-o-H",
    
    "Calcular Propina",
    "Temporarizador",
    "Generador-contraseña",
    "Palindromo",
    "Conversor de longitud",
    "Conversor de edad",
    "Piedra, papel o tijera",
    "Calcular IMC",
    "Ahorcado",
    "Bloc de notas",
    "Conversor de temperatura",
    "Lista de Tareas",
    "Clasificador de palabras",
    "Calcular tipo de triangulo",
    "Calcular velocidad por hora"
    

]

    funciones = [
    agr,
    cl,
    sct,
    cf,
    cm,
    cboh,
    
    cp,
    t,
    gc,
    p,
    cdm,
    cde,
    play_game,
    calcular,
    jugar,
    bdn,
    cdt,
    ldt,
    cps,
    ctt,
    nose,

]

    fila_actual = 0
    columna_actual = 0

    for mensaje, funcion in zip(mensajes, funciones):
        boton = tk.Button(marco_botones, text=mensaje, font=("Arial", 14), command=funcion)
        boton.grid(row=fila_actual, column=columna_actual, padx=10, pady=10)
        columna_actual += 1
        if columna_actual == 3:
            columna_actual = 0
            fila_actual += 1

    def cerrar_ventana():
        ventana.destroy()

    cerrar_button = tk.Button(ventana, text="Cerrar", font=("Arial",14) , command=cerrar_ventana)
    cerrar_button.pack(side="bottom", anchor="sw", padx=10, pady=10)

    def rv():
        ventana.withdraw()
        ventana_secundaria.deiconify()

    bdr = tk.Button(ventana,text="Regresar a Presentación", font=("Arial",14) , command=rv)
    bdr.place(x=1115,y=650)





ventana_secundaria = tk.Tk()
ventana_secundaria.title("Grupo #1")
ventana_secundaria.geometry("400x300")

grupo_label1 = tk.Label(ventana_secundaria, text=" ")
grupo_label1.pack()

grupo_label2 = tk.Label(ventana_secundaria, text=" ")
grupo_label2.pack()

grupo_label3 = tk.Label(ventana_secundaria, text=" ")
grupo_label3.pack()

grupo_label4 = tk.Label(ventana_secundaria, text=" ")
grupo_label4.pack()

grupo_label5 = tk.Label(ventana_secundaria, text=" ")
grupo_label5.pack()

grupo_label6 = tk.Label(ventana_secundaria, text=" ")
grupo_label6.pack()

grupo_label7 = tk.Label(ventana_secundaria, text=" ")
grupo_label7.pack()

grupo_label = tk.Label(ventana_secundaria, text="Grupo #1", font=("Arial", 20, "bold"))
grupo_label.pack()

nombres_label = tk.Label(ventana_secundaria, text="Conformado por: ", font=("Arial", 15, "bold"))
nombres_label.pack()

nombres = ["Jin Almejas", "Jhon Salazar", "Sofia Bautista", "Santiago Romero"]

for nombre in nombres:
    nombre_label = tk.Label(ventana_secundaria, text=nombre, font=("Arial", 13, "bold"))
    nombre_label.pack()

institucion_label = tk.Label(ventana_secundaria, text="Institución Educativa Moderna De Tuluá", font=("Arial", 16))
institucion_label.pack()

año_label = tk.Label(ventana_secundaria, text="2023", font=("Arial", 21))
año_label.pack()

boton_principal = tk.Button(ventana_secundaria, text="Ir a programas", command=mostrar_ventana_principal)
boton_principal.place(x=649,y=650)

imagen = Image.open("downloads/imagen/proyecto sena/iemdt.jpg")
imagen = imagen.resize((300, 300))

imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(ventana_secundaria, image=imagen_tk)
label_imagen.place(x=0,y=0)

imagen2 = Image.open("downloads/imagen/proyecto sena/abjita.jpg")
imagen2 = imagen2.resize((300, 300))

imagen_tk2 = ImageTk.PhotoImage(imagen2)

label_imagen2 = tk.Label(ventana_secundaria, image=imagen_tk2)
label_imagen2.place(x=1060,y=400)

ventana_secundaria.mainloop()