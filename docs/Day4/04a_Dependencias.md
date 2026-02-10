# Instalar dependencias

Nuestro primer paso es *instalar las dependencias requeridas*. Así que antes de empezar, instala los paquetes de Python necesarios.

Los paquetes de Python que instalaremos incluyen:

- **pypdf**: Extrae y lee texto de PDFs.

- **faiss-cpu**: Almacena el contenido de documentos para una recuperación rápida.

- **langchain_ollama**: Ejecuta modelos de IA para preguntas y respuestas.

- **langchain_huggingface**: Utiliza encrustaciones (embeddings) para la búsqueda de texto.

- **streamlit**: Se utiliza para la interfaz web.

Vamos a proceder a instalarlos.

Crearemos la carpeta "Day4" en nuestra ruta de proyectos:

*C:\Users\alumno\Desktop\AIAgents>*

Accedemos a la carpeta "Day4" una vez creada:

```bash
cd ./Day4
```

Ahora instalaremos las dependencias nombradas anteriormente con el siguiente comando:

```bash
pip install pypdf faiss-cpu langchain_ollama langchain_huggingface streamlit
```

Una vez que estén todos instalados, estaremos listos para crear o construir el lector de documentos de IA.

Anterior página: Introducción --> [**Click aquí**](./04_Intro.md)

Siguiente página: Construir el Lector de Documentos de IA --> [**Click aquí**](./04b_LectorDocumentos.md)