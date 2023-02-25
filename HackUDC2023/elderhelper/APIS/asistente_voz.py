import pyttsx3
from elderhelper.APIS.opanai import generar_respuesta
import speech_recognition as sr



def chat(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_text = r.record(source)  # lee el audio del archivo
    try:
        text = r.recognize_google(audio_text, language='es-ES')
        return text
    except sr.UnknownValueError:
        return "Lo siento, no pude entender lo que dijiste."
def voz(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'spanish')  # Establecer el idioma en español
    engine.setProperty('rate', 130)
    engine.setProperty('pitch', 5)
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    texto = generar_respuesta(chat())
    engine = pyttsx3.init()
    engine.setProperty('voice', 'spanish')  # Establecer el idioma en español
    engine.setProperty('rate', 130)
    engine.setProperty('pitch', 5)
    engine.say(texto)
    engine.runAndWait()