from openai import OpenAI
from openai_api import Tutor
from reglas     import reglas
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontro la API key en tu archivo .env")
client = OpenAI(api_key=api_key)

print(f'''
Bienvenido al tutor de matematicas basicas MateprofeGPT
Puedes preguntar dudas y ejemplos, pero no esperes que te resuelva la tarea

''')
tutorMatematicas    = Tutor(client,reglas,"gpt-4.1-mini")
while True:
    pregunta    = str(input(f'''
    Escribe tu consulta : 
    Escribe "Salir" para terminar la aplicación
    '''))
    if pregunta.lower() == "salir":
        print("Vuelve pronto, te estare esperando para seguir aprendiendo!!! :)")
        break
    elif pregunta.strip()  == "" :
        print("Consulta en invalida, ingrese un tema ")
    else:
        respuesta   = tutorMatematicas.Tutoria(pregunta)
        print(respuesta)