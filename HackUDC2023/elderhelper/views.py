from django.http import HttpResponse
from django.shortcuts import render
import openai
import speech_recognition as sr

openai.api_key = "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"
model_engine = "text-davinci-003"


def index(request):
    return render(request, 'index.html', {})


def chat_hub(request):
    return render(request, 'chat_hub.html', {})


def generate_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=input_text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.57,
        )
        generated_text = completion.choices[0].text
        texto = generated_text
        return render(request, 'output.html', {'generated_text': generated_text})
    return render(request, 'input.html')


def generate_voice(request):
    if request.method == 'POST':
        audio = request.FILES['audio']
        text = ""
        r = sr.Recognizer()
        input_audio = sr.AudioFile(audio)
        with input_audio as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language='es-ES')
        except sr.UnknownValueError:
            return ""

        completion = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.57,
        )
        generated_text = completion.choices[0].text
        return render(request, 'output.html', {'generated_text': generated_text})
    return render(request, 'input_voice.html')
