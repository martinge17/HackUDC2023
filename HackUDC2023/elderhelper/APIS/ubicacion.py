import googlemaps
import requests
import sys
import telebot



def enviar_ubicacion():
    # Configurar la API de Telegram con tu token de bot
    bot_token = "6239438265:AAGMtgtO9_6CXtw4tKgUhonc3DIKII70xQc"
    bot_chatID = "-1561488933"
    bot = telebot.TeleBot('6239438265:AAGMtgtO9_6CXtw4tKgUhonc3DIKII70xQc')
    url = "https://api.telegram.org/bot" + bot_token + "/sendMessage"
    params = {
        'chat_id': bot_chatID,

        'text': str("HOLA")
    }
    bot.send_message(bot_chatID, "HOLA")

    #requests.post(url, params=params)
    # # Configurar la API de Google Maps con tu clave de API
    # gmaps = googlemaps.Client(key='AIzaSyDi5DU5F6hiBVd-o89laebT6Q8Oo1SLHvk')
    #
    # # Obtener tu ubicación actual usando la API de Google Maps
    # geocode_result = gmaps.geocode('TU_DIRECCION')
    # location = geocode_result[0]['geometry']['location']
    # latitude = location['lat']
    # longitude = location['lng']
    #
    # # Generar el enlace de Google Maps con tus coordenadas
    # map_link = f'https://www.google.com/maps/place/{latitude},{longitude}'
    #
    # # Enviar el mensaje con el enlace al grupo de Telegram
    # bot.send_message(chat_id=bot_chatID, text=f"Aquí estoy: {map_link}")


def enviar_ubicacion_telegram(token_telegram, chat_id):
    # Definir la clave de la API de Google Maps
    gmaps = googlemaps.Client(key='TU_CLAVE_DE_API_DE_GOOGLE_MAPS')

    # Obtener la ubicación actual
    location = gmaps.geolocate()
    lat, lon = location['location']['lat'], location['location']['lng']

    # Generar el enlace a Google Maps
    url = f'https://www.google.com/maps/search/?api=1&query={lat},{lon}'

    # Enviar el mensaje con el enlace a un chat grupal de Telegram
    bot = telegram.Bot(token=token_telegram)
    bot.send_message(chat_id=chat_id, text=f'Mi ubicación actual: {url}')


if __name__ == "__main__":
    enviar_ubicacion()
