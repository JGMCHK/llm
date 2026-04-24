
class Tutor():
    def __init__(self,cliente,reglas,model):
        self.cliente    = cliente  
        self.reglas     = reglas
        self.model      = model
        self.historial  = ""
        self.histTemp   = ""
        self.contador   = 0

    def _Prompt(self,pregunta):
        consulta    = f'{self.reglas}\n{self.historial}\nPregunta del estudiante: {pregunta}\n' 
        return consulta
    def _Respuesta(self,pregunta):
        client              = self.cliente
        prompt              = self._Prompt(pregunta)
        response            = client.responses.create(
            model           = self.model,
            input           = prompt
        )
        respuestaTutor  = response.output_text
        self.historial  = f"{self.historial}\nUsuario: {pregunta}\nTutor: {respuestaTutor}\n"
        self.histTemp   = f"Usuario: {pregunta}\nTutor: {respuestaTutor}\n"
        return respuestaTutor
    def Tutoria(self,pregunta):
        resultante    = self._Respuesta(pregunta)
        if self.contador >= 0 and self.contador <= 14:
            self.contador += 1
        elif self.contador == 15:
            self.historial  = self.histTemp
            self.contador   = 0
        return resultante
