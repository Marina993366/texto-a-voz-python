from newspaper import Article

def obtener_texto(url):
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    return articulo.text


def main():
    url = input("Ingresá la URL del artículo: ")
    texto = obtener_texto(url)

    print("\n--- TEXTO DEL ARTÍCULO ---\n")
    print(texto[:1000])  # mostramos solo una parte


if __name__ == "__main__":
    main()