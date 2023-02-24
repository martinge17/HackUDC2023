import os
import requests
import json
from datetime import datetime
def obtener_tiempo(ciudad):
    api_key = 'API AQUÍ'
    # Primero, obtenemos el código de la estación meteorológica de la ciudad
    url_ciudad = f'https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{ciudad}'
    parametros = {'api_key': api_key}
    response = requests.get(url_ciudad, params=parametros)
    url_datos = response.json()['datos']

    # A continuación, descargamos los datos meteorológicos de la estación
    response = requests.get(url_datos)
    if response.status_code == 200:
        hora = datetime.now().hour
        if 0 < hora < 6:
            i = 3
        elif 6 <= hora < 12:
            i = 4
        elif 12 <= hora < 18:
            i = 5
        else:
            i = 6
        ciudad = response.json()[0]['nombre']

        # Extraemos los datos relevantes de la predicción meteorológica
        prediccion = response.json()[0]['prediccion']['dia'][0]  # solo el primer día

        # Estado del cielo
        estado_cielo = prediccion['estadoCielo'][i]['descripcion']

        # Temperaturas máximas y mínimas
        temperatura_max = prediccion['temperatura']['maxima']
        temperatura_min = prediccion['temperatura']['minima']

        # Probabilidad de precipitación
        prob_precipitacion = prediccion['probPrecipitacion'][i]['value']

        # Porcentaje de humedad
        humedad_relativa_max = prediccion['humedadRelativa']['maxima']
        humedad_relativa_min = prediccion['humedadRelativa']['minima']

        # Velocidad del viento
        velocidad_viento_max = prediccion['viento'][i]['velocidad']
        direccion_viento = prediccion['viento'][i]['direccion']

        # Creamos un diccionario con los datos relevantes
        resultado = {'ciudad': ciudad, 'estado_cielo': estado_cielo, 'temperatura_max': temperatura_max,
                     'temperatura_min': temperatura_min,
                     'prob_precipitacion': prob_precipitacion, 'humedad_relativa_max': humedad_relativa_max,
                     'humedad_relativa_min': humedad_relativa_min,
                     'velocidad_viento_max': velocidad_viento_max, 'direccion_viento': direccion_viento}

        return resultado
    else:
        return None


if __name__ == '__main__':
    # Definimos el código de la ciudad de la que queremos obtener la predicción meteorológica
    codigo_ciudad = '15030'  # código para A Coruña

    # Obtenemos la predicción meteorológica para la ciudad especificada
    prediccion = obtener_tiempo(codigo_ciudad)

    # Si la función ha devuelto un resultado, lo imprimimos en pantalla
    if prediccion is not None:
        print(f'Predicción meteorológica para el día de hoy en la ciudad \"{prediccion["ciudad"]}\" con código {codigo_ciudad}:')
        print(f'Estado del cielo: {prediccion["estado_cielo"]}')
        print(f'Temperatura máxima: {prediccion["temperatura_max"]}°C')
        print(f'Temperatura mínima: {prediccion["temperatura_min"]}°C')
        print(f'Probabilidad de precipitación: {prediccion["prob_precipitacion"]}%')
        print(f'Humedad relativa máxima: {prediccion["humedad_relativa_max"]}%')
        print(f'Humedad relativa mínima: {prediccion["humedad_relativa_min"]}%')
        print(f'Velocidad máxima del viento: {prediccion["velocidad_viento_max"]} km/h')
        print(f'Dirección del viento: {prediccion["direccion_viento"]}')
    else:
        print('No se ha podido obtener la predicción meteorológica.')