import pyttsx3
from django.http import JsonResponse

from elderhelper.APIS.asistente_voz import voz, chat
from elderhelper.APIS.opanai import generar_respuesta
from elderhelper.APIS.reconocimiento_fotos import recognize_image
import speech_recognition as sr
import requests




if __name__ == "__main__":
    voz(generar_respuesta("Dime una descripción usando estas caracterísrticas en español"+ recognize_image('paella-mixta-800x477.jpg')))
    #voz(generar_respuesta(chat('audio.wav')))

