import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No se encontro la API key en tu archivo .env")
client = OpenAI(api_key=api_key)
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explica que es una variable en programacion de forma sencilla.",
)
print(response.output_text)