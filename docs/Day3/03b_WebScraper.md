# Construir el Web Scraper de IA

Empecemos con la construcción del **raspador web de IA**. Vamos a crear un **script** de Python que:

- Busque en sitios web.

- Extraiga y limpie texto.

- Use IA para resumir el contenido.

## Script de Python

Así que vamos a crear nuestro archivo de código. Volvemos a la terminal:

*C:\Users\alumno\Desktop\AIAgents>*

Ya hemos creado nuestra carpeta "Day3", así que nos desplazaremos a esa carpeta donde crearemos nuestro archivo:

```bash
cd Day3
```

Dentro crearemos nuestro archivo y lo guardamos como nombre "ai_web_scraper.py".

## Importación de bibliotecas instaladas

Una vez creado, ya podemos empezar a escribir código. Empezaremos por *importar las bibliotecas* que hemos instalado anteriormente:

```py
import requests
from bs4 import BeautifulSoup
import streamlit as st
from langchain_ollama import OllamaLLM
```

## Repaso rápido de bibliotecas

- **request**: se utiliza para hacer solicitudes HTTP para obetener páginas web.

- **beautifulsoup4**: analiza HTML y extrae texto de páginas web.

- **streamlit**: construye aplicaciones web interactivas como interfaces web de usuario (Web UI).

- **langchain_ollama**: se utiliza para interactuar con un modelo de lenguaje de IA (*mistral*, *llama3*, *deepseek*...).

## Cargar Modelo LLM

Ahora procederemos a cargar el modelo de IA y usaré el modelo "Mistral":

```py
# Load AI Model
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model
```

Esta instancia de LLM se utilizará para generar respuestas de texto, como resumir el contenido de sitios web en este contexto particular.

Puedes reemplazar el modelo "mistral" con la matriz "deepseek", "llama3" o cualquier otro modelo que Ollama soporte y que pueda usarse junto con Ollama LLM.

## Función para extraer datos de un sitio web

A continuación, vamos a escribir una función para extraer datos de un sitio web:

```py
# Function to scrape a website
def scrape_website(url): #1
    try: #2
        st.write(f"🌍 Scraping website: {url}") #3
        headers = {"User-Agent": "Mozilla/5.0"} #4
        response = requests.get(url, headers=headers) #5

        if response.status_code != 200: #6
            return f"☣️ Failed to fetch {url}" #7

        # Extract text content #8
        soup = BeautifulSoup(response.text, "html.parser") #9
        paragraphs = soup.find_all("p") #10
        text = " ".join([p.get_text() for p in paragraphs]) #11

        return text[:2000] #12
    except Exception as e: #13
        return f"❌ Error: {str(e)}" #14
```

1. Esta función se llama "scrape_website", que sirve para tomar una URL como entrada y extrae su contenido.

2. Intentaremos ejecutar un código si no nos produce un error.

3. Esto muestra un mensaje en la interfaz de usuario de Streamlit para informar al usuario que se está extrayendo el sitio web.

4. Establecen un encabezado de agente de usuario para imitar una solicitud de navegador real.

5. El "requests.get()" envía una solicitud GET para obtener la página web de esa url o vino especificada.

6. Si verificas si la solicitud fue exitosa, el statuscode 200 significa que fue exitoso. Si no es 200, eso significa que algo no salió bien.

7. Entonces se devuelve la respuesta de que no se pudo obtener la URL especificada.

8. Se procede a extraer el contenido del texto.

9. Esto analiza el contenido HTML que obtuvimos de la página web usando *BeautifulSoup*.

10. Lo que hace es encontrar todas las etiquetas HTML o etiquetas de párrafo "p" en la página web.

11. La variable "text" hace que se unan todos los párrafos juntos separados por un espacio. Nuevamente, "text" extrae el texto de cada párrafo y los une una sola cadena.

12. Devuelve el texto anterior, pero lo limita a 2000 caracteres (*:2000*) para evitar que sobrecargue el modelo de IA. Si se quiere aumentar más, puedes aumentar más si lo deseas.

13. Verificamos las excepciones.

14. Si ocurre un error, captura la excepción y devuelve un mensaje de error.

## Función para resumir contenido usando IA

A continuación, voy a proceder a escribir una función para resumir contenido con IA:

```py
# Function to summarize content using AI
def summarize_content(content): #1
    st.write("🖊️ Summarizing content...") #2
    return llm.invoke(f"Summarize the following content:\n\n{content[:1000]}") #3
```

1. Esta función se llama "summarize_content", que sirve para generar un resumen del texto extraído.

2. Esto muestra un mensaje resumiendo el contenido en la interfaz de usuario de Streamlit.

3. Lo que hace es llamar al modelo de IA para resumir el texto. El texto de entreada está limitado a 1000 caracteres para evitar sobrecargar de nuevo la IA. 

## Steamlit Web UI

A continuación, vamos a hacer el diseño de la interfaz:

```py
# Streamlit Web UI
st.title("🤖 AI-Powered Web Scraper")
st.write("Enter a website URL below and get a summarized version!")
```

Establecemos primero el título de la aplicación Streamlit "st.title" como el raspador web impulsado por IA. Luego muestra instrucciones "st.write" sobre cómo usar la aplicación.

## Entrada del usuario

A continuación creamos la entrada del usuario. Tomaré la entrada del usuario para la URL del sitio web:

```py
# User input
url = st.text_input("⛓️‍💥 Enter Website URL:")
```

Esto crea nuevamente un cuadro de entrada donde el usuario puede ingresar una URL de sitio web. Después crearemos la siguiente condición "if":

```py
if url:
    content = scrape_website(url)
```

Si el usuario ha ingresado una URL adecuada, llama a la función "scrape_website" para que, de nuevo, extraiga los datos del sitio web.

Pero si hay un fallo en el contenido o un error en el contenido, escribiremos lo siguiente dentro del if:

```py
    if "☣️ Failed" in content or "❌ Error" in content: #1
        st.write(content) #2
    else: #3
        summary = summarize_content(content) #4
        st.subheader("📋 Website Summary")
        st.write(summary)
```

1. Muestra la condición "if" Si el contenido de la entrada tiene un fallo o tiene un error.

2. En caso verdadero (True) mostrará el error en pantalla.

3. Muestra la condición "else" si no hay fallo o error en el contenido.

4. Entonces mostramos el resumen (summary) de la página web con el "subheader" (encabezado) del sitio web y el resumen del contenido (st.write(summary)).

## Listo! 🎉

Nuestra aplicación ya está completa y lista para funcionar, así que este es **todo** el código que necesitamos escribir para crear nuestro **scraper web de IA**. Espero que hayas podido seguir y entender esto, y pronto estaremos ejecutando este archivo.

Anterior --> [**Click aquí**](03a_Dependencias.md)

Siguiente --> Proximamente...