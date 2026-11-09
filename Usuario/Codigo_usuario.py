class Usuario:

    def __init__(self, nombre, peso, altura, sistolica, diastolica, sodio):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.sistolica = sistolica
        self.diastolica = diastolica
        self.sodio = sodio

    def obtener_datos(self):

        return {
            "nombre": self.nombre,
            "peso": self.peso,
            "altura": self.altura,
            "sistolica": self.sistolica,
            "diastolica": self.diastolica,
            "sodio": self.sodio
        }
