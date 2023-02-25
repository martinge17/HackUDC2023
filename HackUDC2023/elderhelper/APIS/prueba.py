from elderhelper.APIS.opanai import generar_respuesta
from elderhelper.APIS.reconocimiento_fotos import recognize_image

if __name__ == "__main__":
    image_path = '/home/danielmoura/Descargas/paella-mixta-800x477.jpg' # Reemplaza con la ruta y nombre de tu imagen
    texto = recognize_image(image_path)
    print(generar_respuesta("hazme una descripción breve con estos datos en español" + texto))