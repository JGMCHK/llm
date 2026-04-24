# Proyecto 8: Tutor Virtual de Matematicas Basicas

Este proyecto consiste en un tutor virtual desarrollado con la API de OpenAI, orientado a estudiantes de primaria y secundaria. El sistema responde preguntas de matematicas basicas, explica conceptos con lenguaje sencillo, da ejemplos y busca guiar al estudiante paso a paso en lugar de limitarse a entregar respuestas directas.

El tutor esta disenado para:

- explicar temas de matematicas de forma clara y amigable
- responder solo dentro del dominio de matematicas de primaria a tercero de secundaria
- evitar resolver tareas completas sin explicacion
- mantener un historial basico de conversacion para dar continuidad al chat
- rechazar consultas de otras materias y redirigir al usuario a un tema matematico

## Tecnologias utilizadas

- Python
- OpenAI API
- python-dotenv

## Requisitos

- Python 3.10 o superior
- una API key de OpenAI
- entorno virtual recomendado

## Instalacion

1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.
3. Crea un entorno virtual.

En Windows PowerShell:

```powershell
python -m venv .venv
```

En Linux o macOS:

```bash
python3 -m venv .venv
```

4. Activa el entorno virtual.

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

5. Instala las dependencias.

En Windows PowerShell:

```powershell
pip install -r requirements.txt
```

En Linux o macOS:

```bash
pip install -r requirements.txt
```

## Configuracion de la API key

Crea un archivo llamado `.env` en la raiz del proyecto con el siguiente contenido:

```env
OPENAI_API_KEY=tu_api_key_aqui
```

Importante:

- no subas tu archivo `.env` al repositorio
- no coloques tu API key directamente en el codigo

## Ejecucion

El proyecto se ejecuta desde `main.py` y funciona como un tutor conversacional en consola.

Para ejecutar la version actual:

En Windows PowerShell:

```powershell
python main.py
```

En Linux o macOS:

```bash
python3 main.py
```

## Estructura del proyecto

- `main.py`: punto de entrada del programa en consola
- `openAI_API.py`: clase `Tutor`, encargada de construir el prompt, consultar la API y guardar historial
- `reglas.py`: instrucciones que delimitan el comportamiento pedagogico y tematico del tutor

## Comportamiento del tutor

El tutor esta disenado para responder como un profesor paciente y cercano para alumnos de primaria y secundaria. Su comportamiento actual incluye:

- explicar conceptos de matematicas con lenguaje sencillo
- resolver dudas de aritmetica, fracciones, porcentajes, geometria basica, algebra y ecuaciones sencillas
- responder paso a paso cuando sea conveniente para el aprendizaje
- rechazar preguntas de otras materias como fisica, historia, geografia, ingles, programacion o gramatica
- evitar dar solo el resultado cuando el usuario pide que le resuelvan la tarea
- indicar cuando un problema no tiene informacion suficiente para obtener una respuesta unica
- validar entradas vacias en consola y permitir salir del chat escribiendo `Salir`

## Ejemplos de comportamiento

Consultas que el tutor debe aceptar:

- `Explicame como dividir fracciones`
- `Resuelve 2x + 5 = 15`
- `Que es un porcentaje`

Consultas que el tutor debe rechazar amablemente:

- `Explicame las leyes de Newton`
- `Que es el acento diacritico`
- `Como se dice perro en ingles`
- `Cual es la capital de Rusia`

Cuando el usuario pide solo el resultado de una tarea, el tutor intenta mantener un enfoque pedagogico y ofrecer ayuda paso a paso o una pista inicial en lugar de entregar la respuesta sin explicacion.

## Estado actual del proyecto

Hasta el momento, el proyecto ya incluye:

- conexion funcional con la API de OpenAI
- definicion del rol del tutor matematico
- restricciones para mantener el enfoque pedagogico
- manejo basico de historial conversacional con memoria corta
- una implementacion orientada a objetos mediante la clase `Tutor`
- una interfaz de consola funcional en `main.py`

## Objetivo academico

El objetivo del proyecto es demostrar el uso de modelos de lenguaje para construir un tutor virtual educativo capaz de apoyar a estudiantes de primaria y secundaria en temas de matematicas basicas, fomentando la comprension antes que la respuesta inmediata.
