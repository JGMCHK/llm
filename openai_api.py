import os
from dotenv import load_dotenv
from openai import OpenAI

class Tutor():
    def __init__(self,cliente,reglas,model):
        self.cliente    = cliente  
        self.reglas     = reglas
        self.model      = model
        self.historial  = ""

    def _Prompt(self,pregunta):
        consulta    = f'{self.historial}\n{self.reglas}\n{pregunta}\n' 
        return consulta
    def _Respuesta(self,pregunta):
        client              = self.cliente
        prompt              = self._Prompt(pregunta)
        response            = client.responses.create(
            model           = self.model,
            input           = f'''
            {prompt}
            '''
        )
        respuestaTutor  = response.output_text
        self.historial  = f"{self.historial}\nUsuario: {pregunta}\nTutor: {respuestaTutor}\n"
        return respuestaTutor
    def Tutoria(self,pregunta):
        resultante    = self._Respuesta(pregunta)
        return resultante
