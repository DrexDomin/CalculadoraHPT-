
class CalculadoraHPT:

    # CALCULO DEL INDICE DE MASA CORPORAL

    def calcular_imc(self, usuario):

        imc = usuario.peso / (usuario.altura ** 2)
        return imc

    def clasificar_imc(self, imc):

        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"

    # CLASIFICACION DE LA PRESION ARTERIAL

    def clasificar_presion(self, usuario):

        sistolica = usuario.sistolica
        diastolica = usuario.diastolica

        if sistolica > 180 or diastolica > 120:
            return "Presion arterial muy elevada"

        elif sistolica >= 140 or diastolica >= 90:
            return "Hipertension etapa 2"

        elif sistolica >= 130 or diastolica >= 80:
            return "Hipertension etapa 1"

        elif sistolica >= 120 and diastolica < 80:
            return "Presion arterial elevada"

        else:
            return "Presion arterial normal"

    # RECOMENDACION SOBRE EL SODIO

    def recomendacion_sodio(self, usuario):

        if usuario.sodio > 2000:

            return (
                "El consumo registrado supera la referencia general "
                "de 2000 mg diarios. Se recomienda revisar las "
                "etiquetas nutricionales y reducir alimentos "
                "procesados, embutidos y productos con exceso de sal."
            )

        else:

            return (
                "El consumo registrado no supera la referencia "
                "general de 2000 mg diarios. Se recomienda mantener "
                "una alimentacion equilibrada y moderar el uso de sal."
            )

    # RECOMENDACIONES ALIMENTICIAS

    def generar_recomendaciones(self, usuario, imc):

        recomendaciones = []

        # RECOMENDACIONES GENERALES DE LA DIETA DASH

        recomendaciones.append(
            "Priorizar frutas y verduras frescas durante la "
            "alimentacion diaria."
        )

        recomendaciones.append(
            "Incluir cereales integrales como avena, arroz integral "
            "y pan integral."
        )

        recomendaciones.append(
            "Consumir legumbres como frijoles, lentejas y garbanzos."
        )

        recomendaciones.append(
            "Preferir frutos secos y semillas sin sal anadida."
        )

        recomendaciones.append(
            "Elegir preparaciones hervidas, asadas o al vapor "
            "en lugar de frituras."
        )

        # RECOMENDACIONES SEGUN EL CONSUMO DE SODIO

        if usuario.sodio > 2000:

            recomendaciones.append(
                "Reducir el consumo de embutidos, enlatados, "
                "comidas rapidas y productos con alto contenido "
                "de sodio."
            )

            recomendaciones.append(
                "Revisar las etiquetas nutricionales para comparar "
                "la cantidad de sodio de los alimentos."
            )

        # RECOMENDACIONES SEGUN EL IMC

        if imc < 18.5:

            recomendaciones.append(
                "Consultar con un profesional de salud para recibir "
                "orientacion sobre una alimentacion suficiente "
                "y equilibrada."
            )

        elif imc >= 25:

            recomendaciones.append(
                "Procurar mantener un peso saludable mediante "
                "una alimentacion equilibrada y actividad fisica "
                "adaptada a las condiciones personales."
            )

        # RECOMENDACIONES SEGUN LA PRESION ARTERIAL

        if usuario.sistolica >= 130 or usuario.diastolica >= 80:

            recomendaciones.append(
                "Mantener un seguimiento de la presion arterial "
                "y consultar con un profesional de salud."
            )

        # RECOMENDACIONES GENERALES

        recomendaciones.append(
            "Moderar el consumo de alimentos con exceso de "
            "grasas saturadas y azucares anadidos."
        )

        recomendaciones.append(
            "Utilizar hierbas y especias naturales para dar sabor "
            "a las comidas en lugar de agregar demasiada sal."
        )

        return recomendaciones

    # ADVERTENCIAS SOBRE LA PRESION ARTERIAL

    def advertencia_presion(self, usuario):

        sistolica = usuario.sistolica
        diastolica = usuario.diastolica

        if sistolica > 180 or diastolica > 120:

            return (
                "ATENCION: La lectura es muy elevada. Repite la "
                "medicion despues de al menos un minuto y contacta "
                "inmediatamente a un profesional de salud. Si "
                "presentas dolor en el pecho, dificultad para "
                "respirar, debilidad, alteraciones de la vision "
                "o dificultad para hablar, busca atencion de "
                "emergencia de inmediato."
            )

        elif sistolica >= 140 or diastolica >= 90:

            return (
                "La lectura se encuentra en un rango de "
                "hipertension etapa 2. Se recomienda consultar "
                "con un profesional de salud para su valoracion."
            )

        elif sistolica >= 130 or diastolica >= 80:

            return (
                "La lectura se encuentra en un rango de "
                "hipertension etapa 1. Es importante realizar "
                "seguimiento y consultar con un profesional."
            )

        elif sistolica >= 120 and diastolica < 80:

            return (
                "La lectura se encuentra en un rango elevado. "
                "Se recomienda mantener habitos saludables "
                "y realizar seguimiento."
            )

        else:

            return (
                "La lectura se encuentra dentro del rango "
                "normal de referencia."
            )

    # EVALUACION GENERAL

    def evaluar(self, usuario):

        imc = self.calcular_imc(usuario)

        clasificacion_imc = self.clasificar_imc(imc)

        clasificacion_presion = self.clasificar_presion(usuario)
        print("SISTOLICA:", usuario.sistolica)
        print("DIASTOLICA:", usuario.diastolica)
        print("CLASIFICACION:", clasificacion_presion)

        recomendacion_sodio = self.recomendacion_sodio(usuario)

        recomendaciones = self.generar_recomendaciones(
            usuario, imc
        )

        advertencia = self.advertencia_presion(usuario)

        return {

            "imc": imc,

            "clasificacion_imc": clasificacion_imc,

            "clasificacion_presion": clasificacion_presion,

            "recomendacion_sodio": recomendacion_sodio,

            "recomendaciones": recomendaciones,

            "advertencia_presion": advertencia

        }
