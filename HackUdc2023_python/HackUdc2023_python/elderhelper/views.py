from django.shortcuts import render

# Create your views here.
import openai
import os

# Configura la API key
openai.api_key = "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";

# Define el modelo y el prompt
model_engine = "text-davinci-002"
prompt = "Write a short story about a man who discovers a mysterious object in his backyard."

# Realiza la petición al API
completions = openai.Completion.create(
    engine=model_engine,
    prompt="cristiano ronaldo es guapo",
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.5,
)

# Obtiene el texto generado por el modelo
generated_text = completions.choices[0].text

print(generated_text)