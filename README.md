# Proyecto 8: Tutor Virtual de Matematicas Basicas

Este proyecto consiste en un tutor virtual desarrollado con la API de OpenAI, orientado a estudiantes de primaria y secundaria. El sistema responde preguntas de matematicas basicas, explica conceptos con lenguaje sencillo, da ejemplos y busca guiar al estudiante paso a paso en lugar de limitarse a entregar respuestas directas.

El tutor esta disenado para:

- explicar temas de matematicas de forma clara y amigable
- responder solo dentro del dominio de matematicas de primaria a tercero de secundaria
- evitar resolver tareas completas sin explicacion
- mantener un historial basico de conversacion para dar continuidad al chat

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
3. Crea un entorno virtual:

```powershell
python -m venv .venv
```

4. Activa el entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

5. Instala las dependencias:

```powershell
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

Actualmente el proyecto cuenta con una implementacion en progreso de un tutor conversacional en consola.

Para ejecutar una version de prueba:

```powershell
python openai_apiTEST.py
```

## Estado actual del proyecto

Hasta el momento, el proyecto ya incluye:

- conexion funcional con la API de OpenAI
- definicion del rol del tutor matematico
- restricciones para mantener el enfoque pedagogico
- manejo basico de historial conversacional
- una version inicial orientada a clases en `openAI_API.py`

## Objetivo academico

El objetivo del proyecto es demostrar el uso de modelos de lenguaje para construir un tutor virtual educativo capaz de apoyar a estudiantes de primaria y secundaria en temas de matematicas basicas, fomentando la comprension antes que la respuesta inmediata.
