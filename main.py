# importar las librerías necesarias
from newspaper import Article
from gtts import gTTS

# función para obtener el texto del artículo
def obtener_texto(url):
    try:
        articulo = Article(url)
        articulo.download()
        articulo.parse()

        if not articulo.text.strip():
            raise ValueError("No se pudo extraer texto del artículo")

        return articulo.text

    except Exception as e:
        print("Error al obtener el artículo")
        print(e)
        return None

# función para convertir texto a voz
def texto_a_voz(texto, nombre_archivo="articulo.mp3"):
    tts = gTTS(text=texto, lang='es')
    tts.save(nombre_archivo)
    print(f"Archivo de audio guardado como {nombre_archivo}")

# función principal
def main():
    url = input("Ingresá la URL del artículo: ")
    texto = obtener_texto(url)
    if texto is None:
        print("No se pudo continuar con la conversión.")
        return

    print("\n--- TEXTO DEL ARTÍCULO ---\n")
    print(f"{texto[:500]}...")  # mostramos solo una parte
    print("\n--- CONVIRTIENDO A VOZ ---\n")
    nombre_archivo = input("Ingresá el nombre del archivo de audio (con .mp3): ")
    if not nombre_archivo.endswith('.mp3'):
        nombre_archivo += '.mp3'
    texto_a_voz(texto, nombre_archivo)


if __name__ == "__main__":
    main()