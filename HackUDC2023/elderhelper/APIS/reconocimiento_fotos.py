import base64
import requests
import json
from io import BytesIO
from PIL import Image

def recognize_image(image_path):
    # Define la URL de la API de Clarifai
    url = 'https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs'

    # Define los encabezados de la solicitud
    headers = {
        'Authorization': "Key 2282a5854a274e9c9dd13ca7d3f56ccc",
        'Content-Type': 'application/json'
    }

    # Abre la imagen que se desea analizar y la comprime
    image = Image.open(image_path)
    image = image.resize((256, 256)) # ajusta el tamaño a 256x256 píxeles
    buffered = BytesIO()
    image.save(buffered, format="JPEG", quality=50)
    img_str = base64.b64encode(buffered.getvalue()).decode('ascii')

    # Define la carga útil de la solicitud con la imagen comprimida
    payload = {
        "inputs": [
            {
                "data": {
                    "image": {
                        "base64": img_str
                    }
                }
            }
        ]
    }

    # Envía la solicitud a la API
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Procesa la respuesta de la API
    texto =""
    if response.status_code == requests.codes.ok:
        response_json = json.loads(response.text)
        concepts = response_json['outputs'][0]['data']['concepts']
        for concept in concepts:
            texto += concept['name'] + ","
            print(concept['name'], concept['value'])
        print(texto)
        return texto
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    image_path = 'ruta_foto' # Reemplaza con la ruta y nombre de tu imagen
    recognize_image(image_path)
