import openai
openai.api_key = "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"

def generar_respuesta(pregunta):
    model_engine = "text-davinci-002"
    prompt = f"Q: {pregunta}\nA:"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    print(message)
    return message
