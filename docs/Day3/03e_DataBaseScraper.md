# Almacenar Datos Extraídos en una Base de datos Vectorial

Lo que vamos a hacer aquí es **mejorar** nuestro raspador web con estas mejoras:

- Almacenamos el contenido web extraído en una *base de datos vectorial* que es **FAISS**.

- Permitimos a los usuarios *buscar en el conocimiento almacenado*.

- Recuperaremos *contenido relevante* usando IA.

Así que empecemos:

1. Primero instalaremos las dependencias necesarias.

2. Modificaremos los raspadores web de IA para almacenar datos en archivos donde:

- Primero extraeremos el sitio web.

- Luego incrustaremos el contenido.

- Después lo almacenaremos en los archivos o en la base de datos vectorial (FAISS).

- Al final, habilitaremos la búsqueda potenciada por IA en este contenido almacenado.

---

## Archivo nuevo

Primero vamos a ir a la terminal en nuestra ruta:

*C:\Users\alumno\Desktop\AIAgents\Day3>*

En lugar de actualizar nuestra aplicación (ai_web_scraper.py) vamos a mantenerla tal y como está. Crearemos un archivo nuevo y lo guardaremos como nombre "ai_web_scrapper_faiss.py". Así ya podemos empezar a escribir código.

## Dependencias necesarias

Lo primero que necesitamos hacer es asegurarnos de haber instalado todas nuestras dependencias. Para esto, tenemos que volver a la *terminal* y asegurarme de que todas nuestras dependencias estén instaladas. 

Esto incluye también instalar lo que ya hemos instalado anteriormente, así que haremos un recuento de los paquetes instalados y los que vamos a instalar a continuación:

```bash
pip install requests beautifulsoup4 langchain_ollama faiss-cpu chromadb streamlit
```

Ejecutamos el comando y, después de instalar dependencias, limpiamos la terminal (*cls* o *clear*)

## Recuento de dependencias ya instalados 

(Por si no viste --> [03a_Dependencias](./03a_Dependencias.md)):

1. **requests** --> Obtiene datos de páginas web.

2. **beautifulsoup4** --> Extrae y limpia texto de HTML.

3. **langchain_ollama** --> Usa Ollama para el *resumen impulsado con IA* (AI-powered summarization).

4. **streamlit** --> Construye una interfaz web para el *raspador web* (web scrapper).

## Dependencias a instalar para FAISS (Base de datos vectorial):

1. **faiss-cpu**: Sirve para la *búsqueda eficiente de similitud*, es decir que busca los vectores más similares a una consulta; y *clustering de vectores densos*. Indexa grandes cantidades en embeddings de forma eficiente.

2. **chromadb**: Es una alternativa de almacenaciemto de vectores local, completa y más moderna. Sirve para guardar tanto los vectores como los documentos originales y metadatos. 

---

# Empieza el código

Ahora vamos a dirigirnos a nuestro archivo creado *ai_web_scrapper_faiss.py* y comenzaremos con nuestras importaciones:

```py
import requests # Solicitudes HTTP
from bs4 import BeautifulSoup # Obtención de páginas web
import streamlit as st # Interfaz web
import faiss # Busquedas de similitud
import numpy as np 
from langchain_huggingface import HuggingFaceEmbedding # Updated Import
from langchain_community.vectorstores import FAISS # Base de datos vectorial
from langchain.text_splitter import CharacterTextSplitter # Dividor texto
from langchain.schema import Document # Documentos
```

## Datos importantes

- **from langchain_huggingface import HuggingFaceEmbedding**: 

Esta es una importación actualizada. Esto solía ser un poco diferente de la versión anterior.Así que si tenías la anterior, se obtenía directamente de Langchain. Ejecutaríamos el siguiente comando: 

```bash
pip install langchain_huggingface
```

Actualiza el archivo y verás cómo ya funciona.

- **from langchain.text_splitter import CharacterTextSplitter**: 

Es el dividor de texto de caracteres de LangChain. Divide textos largos en fragmentos más pequeños.

Este módulo proviene de la versión anterior de LangChain 0.2.x. Si no te importa el archivo, prueba a importar con este otro:

```py
from langchain_text_splitters import CharacterTextSplitter
```

Si eso no funciona, prueba a instalar el siguiente paquete desde la terminal:

```bash
pip install langchain-text-splitters
```

- **from langchain.schema import Document**: 

Representa un documento o fragmento de texto estructurado para el procesamiento en LangChain. Este también proviene de la versión anterior de LangChain 0.2.x. Si hay fallo en la importación, prueba a importar con este otro:

```py
from langchain_core.documents import Document
```

Si eso no funciona, asegurate de instalar el siguiente paquete desde la terminal:

```bash
pip install langchain-core
```

---

## Modelo de IA

Ahora vamos a cargar el modelo de IA:

```py
# Load AI Model
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model
```

## Hugging Face Embeddings

A continuación, cargaremos las incrustaciones d la página de Hugging:

```py
# Load Hugging Face Embeddings (Update)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

Esta es una versión actualizada de LangChain en comparación con la versión anterior de la V.0.2.x. Esto carga un modelo de transformador de oraciones (all-MiniLM-L6-v2).

Esto se utiliza para convertir texto en incrustaciones numéricas para la búsqueda de similitud. Y eso es lo que necesitamos en una base de datos vectorial.

## FAISS Vector Database

A continuación, vamos a proceder a inicializar un almacén de vectores de FAISS:

```py
# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384) # Vector dimension for MiniLM
vector_store = {}
```

El *"index"* crea un índice de archivos para la búsqueda de similitud. La *"IndexFlatL2"*, que es la distancia euclidiana, se utiliza para medir la similitud. El número *"384"* es el tamaño del vector que coincide con el modelo de incrustación MiniLM.

La dimensión del vector para el almacén de vectores miniLM está vacía. Por eso, hemos creado un almacén de vectores (*"vector_store"*) que es un diccionario para guardar URLs y verificaciones.

## Función para extraer datos de un sitio web

Proximamente...