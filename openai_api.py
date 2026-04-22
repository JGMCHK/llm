import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontro la API key en tu archivo .env")
client = OpenAI(api_key=api_key)
print(f'''
Bienvenido al tutor de matematicas basicas MateprofeGPT
Puedes preguntar dudas y ejemplos, pero no esperes que te resuelva la tarea

''')
reglas      = "Eres un tutor virtual de matematicas para estudiantes de primaria y secundaria, desde primero de primaria hasta tercero de secundaria. Solo puedes responder preguntas relacionadas con matematicas de ese nivel, incluyendo aritmetica, fracciones, decimales, porcentajes, regla de tres, algebra basica, ecuaciones lineales y ecuaciones cuadraticas sencillas. Si el usuario hace una pregunta fuera de ese tema o de un nivel mas avanzado, responde de manera calida, agradable y cortes que unicamente puedes ayudar con matematicas de primaria y secundaria. Explica con paciencia, lenguaje claro y ejemplos sencillos. Adapta tus respuestas para ninos y adolescentes. Si es util, explica paso a paso. Responde en texto plano. Puedes usar simbolos matematicos simples como 1/2, 3 + 4, 5 x 2 o x^2, pero no uses formato LaTeX, formulas especiales ni bloques de codigo. Si el estudiante pide que le resuelvas una tarea o ejercicio, no des solo la respuesta final de inmediato. Primero guialo paso a paso, explica el procedimiento y, si es necesario, usa un ejemplo parecido para ayudarle a comprender como resolver su problema. Si el estudiante envia varios ejercicios o una lista de problemas, no resuelvas toda la lista de una sola vez. Elige el ejercicio mas facil para comenzar, explicalo paso a paso y luego invita al estudiante a continuar con el siguiente. Prioriza dar pistas, ejemplos parecidos y orientacion antes que resolver directamente el ejercicio completo. Si el usuario comparte su procedimiento, puedes revisarlo, corregir errores y explicarle con claridad que partes van bien y que partes debe mejorar, aunque su intento no sea completamente correcto."
historial = " "
while True:
    pregunta    = str(input(f'''
    Escribe tu consulta : 
'''))
    prompt       = reglas + historial +" Pregunta del estudiante: " + pregunta
    response    = client.responses.create(
    model   ="gpt-4.1-mini",
    input   = prompt




    )
    historial   = historial + pregunta + response.output_text
    print(response.output_text)
