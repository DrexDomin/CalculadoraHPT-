
import tkinter as tk
from tkinter import ttk, messagebox

from Usuario.Codigo_usuario import Usuario
from CalculadoraHPT.Codigo_sistema import CalculadoraHPT


class Interfaz:

    def __init__(self):

        self.calculadora = CalculadoraHPT()

        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Alimenticia - Hipertensión")
        self.ventana.geometry("780x800")
        self.ventana.minsize(700, 720)
        self.ventana.configure(bg="#F3F7F5")

        self.configurar_estilos()
        self.crear_interfaz()

    def configurar_estilos(self):

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "TFrame",
            background="#F3F7F5"
        )

        estilo.configure(
            "Titulo.TLabel",
            background="#F3F7F5",
            foreground="#174C3C",
            font=("Arial", 20, "bold")
        )

        estilo.configure(
            "Subtitulo.TLabel",
            background="#F3F7F5",
            foreground="#53665E",
            font=("Arial", 10)
        )

        estilo.configure(
            "Campo.TLabel",
            background="#FFFFFF",
            foreground="#263B32",
            font=("Arial", 10, "bold")
        )

        estilo.configure(
            "Ayuda.TLabel",
            background="#FFFFFF",
            foreground="#718078",
            font=("Arial", 9)
        )

        estilo.configure(
            "TButton",
            font=("Arial", 10, "bold"),
            padding=9
        )

        estilo.configure(
            "Calcular.TButton",
            background="#267653",
            foreground="white",
            padding=12
        )

        estilo.map(
            "Calcular.TButton",
            background=[("active", "#1D6042")]
        )

    def crear_interfaz(self):

        contenedor = ttk.Frame(
            self.ventana,
            padding=22
        )
        contenedor.pack(fill="both", expand=True)

        # ENCABEZADO

        ttk.Label(
            contenedor,
            text="Calculadora Alimenticia",
            style="Titulo.TLabel"
        ).pack(anchor="center", pady=(5, 3))

        ttk.Label(
            contenedor,
            text="Herramienta de orientación para personas con hipertensión",
            style="Subtitulo.TLabel"
        ).pack(anchor="center", pady=(0, 18))

        # FORMULARIO

        formulario = ttk.LabelFrame(
            contenedor,
            text=" Datos del usuario ",
            padding=15
        )
        formulario.pack(fill="x", pady=5)

        formulario.columnconfigure(0, weight=1)
        formulario.columnconfigure(1, weight=1)

        self.nombre = self.crear_campo(
            formulario,
            "Nombre",
            "Ejemplo: Andrés",
            0, 0
        )

        self.peso = self.crear_campo(
            formulario,
            "Peso (kg)",
            "Ejemplo: 55,5",
            0, 1
        )

        self.altura = self.crear_campo(
            formulario,
            "Estatura (metros)",
            "Ejemplo: 1,65",
            1, 0
        )

        self.sistolica = self.crear_campo(
            formulario,
            "Presión sistólica (mmHg)",
            "Ejemplo: 120",
            1, 1
        )

        self.diastolica = self.crear_campo(
            formulario,
            "Presión diastólica (mmHg)",
            "Ejemplo: 80",
            2, 0
        )

        self.sodio = self.crear_campo(
            formulario,
            "Sodio diario (mg)",
            "Ejemplo: 1800",
            2, 1
        )

        # AYUDAS

        ayudas = ttk.LabelFrame(
            contenedor,
            text=" Ayuda para ingresar los datos ",
            padding=12
        )
        ayudas.pack(fill="x", pady=12)

        ttk.Button(
            ayudas,
            text="¿Cómo medir mi presión?",
            command=self.ayuda_presion
        ).pack(side="left", padx=5)

        ttk.Button(
            ayudas,
            text="¿Cómo calcular el sodio?",
            command=self.ayuda_sodio
        ).pack(side="left", padx=5)

        ttk.Button(
            ayudas,
            text="Consejos alimenticios",
            command=self.consejos_alimenticios
        ).pack(side="left", padx=5)

        # BOTONES PRINCIPALES

        botones = ttk.Frame(contenedor)
        botones.pack(pady=8)

        ttk.Button(
            botones,
            text="CALCULAR",
            style="Calcular.TButton",
            command=self.calcular
        ).pack(side="left", padx=6)

        ttk.Button(
            botones,
            text="LIMPIAR",
            command=self.limpiar
        ).pack(side="left", padx=6)

        # RESULTADOS

        marco_resultados = ttk.LabelFrame(
            contenedor,
            text=" Resultados y recomendaciones ",
            padding=10
        )
        marco_resultados.pack(
            fill="both",
            expand=True,
            pady=5
        )

        self.resultado = tk.Text(
            marco_resultados,
            height=12,
            font=("Arial", 10),
            wrap="word",
            bg="#FFFFFF",
            fg="#263B32",
            relief="flat",
            padx=12,
            pady=10,
            state="disabled"
        )

        self.resultado.pack(
            fill="both",
            expand=True
        )

        # AVISO

        ttk.Label(
            contenedor,
            text=(
                "Información orientativa. No reemplaza el diagnóstico "
                "ni las recomendaciones de un profesional de salud."
            ),
            style="Subtitulo.TLabel",
            wraplength=700
        ).pack(pady=(10, 0))

    def crear_campo(self, marco, titulo, ejemplo, fila, columna):

        grupo = ttk.Frame(
            marco,
            padding=7
        )
        grupo.grid(
            row=fila,
            column=columna,
            sticky="ew",
            padx=5,
            pady=5
        )

        ttk.Label(
            grupo,
            text=titulo,
            style="Campo.TLabel"
        ).pack(anchor="w")

        entrada = ttk.Entry(
            grupo,
            font=("Arial", 11)
        )
        entrada.pack(
            fill="x",
            pady=(5, 2)
        )

        ttk.Label(
            grupo,
            text=ejemplo,
            style="Ayuda.TLabel"
        ).pack(anchor="w")

        return entrada

    def ayuda_presion(self):

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Cómo medir la presión arterial")
        ventana.geometry("480x400")
        ventana.configure(bg="#F3F7F5")

        texto = (
            "RECOMENDACIONES PARA MEDIR LA PRESIÓN\n\n"
            "1. Evita fumar, consumir cafeína o hacer ejercicio "
            "durante los 30 minutos anteriores.\n\n"
            "2. Siéntate y descansa durante al menos cinco minutos.\n\n"
            "3. Mantén la espalda apoyada y los pies sobre el suelo, "
            "sin cruzar las piernas.\n\n"
            "4. Coloca el brazalete sobre el brazo descubierto, "
            "siguiendo las instrucciones del tensiómetro.\n\n"
            "5. Apoya el brazo a la altura del corazón.\n\n"
            "6. No hables durante la medición.\n\n"
            "7. Realiza dos mediciones separadas por un minuto "
            "y registra los resultados.\n\n"
            "La presión sistólica es el número superior y la "
            "diastólica es el número inferior."
        )

        self.mostrar_ayuda(ventana, texto)

    def ayuda_sodio(self):

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Cómo estimar el consumo de sodio")
        ventana.geometry("480x350")
        ventana.configure(bg="#F3F7F5")

        texto = (
            "¿CÓMO ESTIMAR EL SODIO QUE CONSUMES?\n\n"
            "1. Revisa la tabla nutricional de los alimentos "
            "envasados.\n\n"
            "2. Busca el apartado que indica la cantidad de sodio "
            "en miligramos (mg) por porción.\n\n"
            "3. Multiplica esa cantidad por el número de porciones "
            "que consumiste.\n\n"
            "4. Suma los valores de los diferentes alimentos "
            "consumidos durante el día.\n\n"
            "Ejemplo:\n"
            "350 mg por porción x 2 porciones = 700 mg.\n\n"
            "La referencia general para adultos es consumir "
            "menos de 2000 mg de sodio al día.\n\n"
            "Si no conoces tu consumo exacto, utiliza una estimación. "
            "No ingreses la cantidad de sal en gramos en este campo."
        )

        self.mostrar_ayuda(ventana, texto)

    def consejos_alimenticios(self):

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Consejos de alimentación")
        ventana.geometry("520x480")
        ventana.configure(bg="#F3F7F5")

        texto = (
            "ORIENTACIONES DE LA DIETA DASH\n\n"
            "ALIMENTOS QUE SE PUEDEN PRIORIZAR:\n"
            "- Frutas y verduras frescas.\n"
            "- Avena, arroz integral y cereales integrales.\n"
            "- Fríjoles, lentejas y garbanzos.\n"
            "- Frutos secos y semillas sin sal añadida.\n"
            "- Pescado, pollo sin piel y otras proteínas bajas en grasa.\n"
            "- Leche y yogur bajos en grasa y sin azúcar añadida.\n\n"
            "ALIMENTOS QUE SE DEBEN LIMITAR:\n"
            "- Embutidos y carnes procesadas.\n"
            "- Enlatados y comidas rápidas.\n"
            "- Productos con alto contenido de sodio.\n"
            "- Fritos y alimentos con exceso de grasas saturadas.\n"
            "- Productos con exceso de azúcar añadida.\n\n"
            "OTRAS RECOMENDACIONES:\n"
            "- Preferir preparaciones hervidas, asadas o al vapor.\n"
            "- Revisar las etiquetas nutricionales.\n"
            "- Utilizar hierbas y especias para dar sabor.\n\n"
            "IMPORTANTE:\n"
            "Las personas con enfermedad renal o que toman ciertos "
            "medicamentos deben consultar con un profesional antes "
            "de aumentar el potasio o utilizar sustitutos de sal."
        )

        self.mostrar_ayuda(ventana, texto)

    def mostrar_ayuda(self, ventana, contenido):

        marco = tk.Frame(
            ventana,
            bg="#FFFFFF",
            padx=18,
            pady=15
        )
        marco.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        texto = tk.Text(
            marco,
            wrap="word",
            font=("Arial", 10),
            bg="#FFFFFF",
            fg="#263B32",
            relief="flat"
        )
        texto.pack(
            fill="both",
            expand=True
        )

        texto.insert("1.0", contenido)
        texto.config(state="disabled")

    
    def calcular(self):

        try:
            nombre = self.nombre.get().strip()

            peso = float(self.peso.get().strip().replace(",", "."))
            altura = float(self.altura.get().strip().replace(",", "."))

            sistolica = int(self.sistolica.get().strip())
            diastolica = int(self.diastolica.get().strip())
            sodio = int(self.sodio.get().strip())

            if not nombre:
                nombre = "Usuario"

            # Validar peso y estatura
            if not (20 <= peso <= 400):
                messagebox.showwarning(
                    "Peso incorrecto",
                    "El peso debe estar entre 20 y 400 kg."
                )
                return

            if not (0.5 <= altura <= 2.5):
                messagebox.showwarning(
                    "Estatura incorrecta",
                    "La estatura debe estar entre 0.5 y 2.5 metros."
                )
                return

            # Validar presión arterial
            if not (40 <= sistolica <= 300):
                messagebox.showwarning(
                    "Presión incorrecta",
                    "La presión sistólica debe estar entre 40 y 300."
                )
                return

            if not (30 <= diastolica <= 200):
                messagebox.showwarning(
                    "Presión incorrecta",
                    "La presión diastólica debe estar entre 30 y 200."
                )
                return

            if sistolica <= diastolica:
                messagebox.showwarning(
                    "Presión incorrecta",
                    "La presión sistólica debe ser mayor "
                    "que la presión diastólica."
                )
                return

            # Validar sodio
            if sodio < 0:
                messagebox.showwarning(
                    "Sodio incorrecto",
                    "El consumo de sodio no puede ser negativo."
                )
                return

            # Crear usuario y evaluar sus datos
            usuario = Usuario(
                nombre,
                peso,
                altura,
                sistolica,
                diastolica,
                sodio
            )

            resultados = self.calculadora.evaluar(usuario)

            texto = (
                f"USUARIO: {nombre}\n\n"
                f"ÍNDICE DE MASA CORPORAL\n"
                f"IMC: {resultados['imc']:.2f}\n"
                f"Clasificación: {resultados['clasificacion_imc']}\n\n"
                f"PRESIÓN ARTERIAL\n"
                f"{sistolica}/{diastolica} mmHg\n"
                f"Clasificación: {resultados['clasificacion_presion']}\n\n"
                f"AVISO: {resultados['advertencia_presion']}\n\n"
                f"CONSUMO DE SODIO\n"
                f"{sodio} mg diarios\n"
                f"{resultados['recomendacion_sodio']}\n\n"
                f"RECOMENDACIONES\n"
            )

            for recomendacion in resultados["recomendaciones"]:
                texto += f"• {recomendacion}\n"

            self.resultado.config(state="normal")
            self.resultado.delete("1.0", tk.END)
            self.resultado.insert(tk.END, texto)
            self.resultado.config(state="disabled")

        except ValueError:
            messagebox.showerror(
                "Datos incorrectos",
                "Hay campos vacíos o datos que no son válidos.\n\n"
                "Usa coma o punto para los decimales.\n"
                "Ejemplo de peso: 55,5\n"
                "Ejemplo de estatura: 1,65\n"
                "La presión y el sodio deben ser números enteros."
            )


    def limpiar(self):

        campos = [
            self.nombre,
            self.peso,
            self.altura,
            self.sistolica,
            self.diastolica,
            self.sodio
        ]

        for campo in campos:
            campo.delete(0, tk.END)

        self.resultado.config(state="normal")
        self.resultado.delete("1.0", tk.END)
        self.resultado.config(state="disabled")

    def ejecutar(self):

        self.ventana.mainloop()
