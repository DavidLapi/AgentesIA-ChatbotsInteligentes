# Construir el Lector de Documentos de IA

Entonces, con todo listo, avancemos y construyamos el lector de documentos de IA.

Crearemos una *IA* que:

- Suba y lea *PDFs*.

- Almacene el texto extraído en *FAISS*.

- Permita a los usuarios *hacer preguntas* basadas en el conocimiento almacenado.

Así que avancemos a nuestro proyecto donde creamos el día 4:

*C:\Users\alumno\Desktop\AIAgents\Day4>*

Voy a crear un nuevo archivo aquí, le llamaremos "ai_document_reader.py".

Ese será nuestro archivo de Python, así que empezaremos a escrivir código.

## Importación de bibliotecas instaladas

Aquí vamos a importar las bibliotecas necesarias para hacer funcionar la aplicación:

```py
import streamlit as st #1
import faiss #2
import numpy as np #3
import pypdf #4
from langchain_ollama import OllamaLLM #5
from langchain_huggingface import HuggingFaceEmbeddings #6
from langchain_community.vectorstores import FAISS #7
from langchain_text_splitters import CharacterTextSplitter #8
from langchain_core.documents import Document #9
```

1. **import streamlit as st**: Se utiliza para construir una interfaz de usuario basada en la web para subir PDFs e interactuar con el sistema de preguntas y respuestas impulsado por IA en este caso particular.

2. **import faiss**: Biblioteca para la búsqueda eficiente de similitudes utilizada aquí para almacenar y recuperar incrustaciones vectoriales. La razón por la que se llama "FAISS" entre iniciales es "Facebook AI Similarity Search".

3. **import numpy as np**: Se utiliza para manejar cálculos numéricos, especialmente para convertir incrustaciones de texto en un formato compatible con FAISS.

4. **import pypdf**: Biblioteca para extraer texto de archivos PDF.

5. **from langchain_ollama import OllamaLLM**: Se utiliza para cargar e interactuar con el modelo de Ollama como "mistral" o "llama3".

6. **from langchain_huggingface import HuggingFaceEmbeddings**: Esto maneja la generación de incrustaciones de texto usando los transformadores de oraciones de Huggingface.

7. **from langchain_community.vectorstores import FAISS**: Esto proporciona la integración de FAISS en Langchain para una recuperación de documentos basada en vectores de manera eficiente.

8. **from langchain_text_splitters import CharacterTextSplitter**: Esto divide el texto en fragmentos más pequeños para facilitar un mejor indexado y recuperación.

9. **from langchain_core.documents import Document**: Esto define el esquema del documento para el procesamiento de texto.

## Modelo de IA

A continuación vamos a cargar nuestro modelo de IA:

```py
# Load AI Model
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model
```

Como se dijeron en anteriores días, se puede cambiar a cualquiera de los modelos disponibles en el sitio web de Ollama (deepseek, llama3...).

## Embeddings de Hugging Face

A continuación, vamos a continuar con las incrustaciones (embeddings) de texto:

```py
# Load Hugging Face Embeddings 
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

Como hemos visto antes en el día 3, se utiliza para convertir texto en incrustaciones numéricas para la búsqueda de similitud. Y eso es lo que necesitamos en una base de datos vectorial.

Estos embeddings ayudan a almacenar y recuperar fragmentos de texto relevantes usando FAISS. Así que, a continuación:

## Base de datos vectorial FAISS

Vamos a continuar e inicializar la base de datos de vectores FAISS:

```py
# Initialize FAISS Vector Database
index = faiss.IndexFlatL2(384) # Vector dimension for MiniLM
vector_store = {}
```

Este "faiss.indexFlatL2" inicializa un índice FAISS para almacenar vectores. "384" es el tamaño de incrustación (embedding) de "MiniLM-L6-v2", asegurando compatibilidad. La distancia "L2", que es la distancia euclidiana, se utiliza para la búsqueda de similitud.

Como un almacén de vectores (vector_store), que es un diccionario para almacenar documentos, metadatos y fragmentos de texto.

## Función extract_text_from_pdf

Ahora vamos a continuar y escribir una función para *extraer texto de un PDF*:

```py
# Function to extract text from PDFs
def extract_text_from_pdf(uploaded_file): #1
    pdf_reader = pypdf.PdfReader(uploaded_file) #2
    text = "" #3
    for page in pdf_reader.pages: #4
        text += page.extract_text() + "\n" #5
    return text #6
```

1. Llamamos a la función "extract_text_from_pdf" y recibirá un archivo subido (uploaded_file) como entrada.

2. "pdf_reader" lee un archivo PDF subido.

3. Declaramos "text" como un campo vacío.

4. Esto dice: Para cada página en "pdf_reader.pages" esto iterará a través de todas las páginas y extraerá texto.

5. Así que aquí voy a obtener el texto, añadirlo diciendo "page.extract_text()" y añadir salto de línea (\n). También concatena el texto en una sola cadena.

6. Devolvemos el texto extraído.

## Función store_in_faiss

Ahora vamos a escribir una función para *almacenar texto en FAISS*:

```py
# Function to store text in FAISS
def store_in_faiss(text, filename): #1
    global index, vector_store #2
    st.write(f"📩 Storing document '{filename}' in FAISS...") #3

    # Split text into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100) #4
    texts = splitter.split_text(text) #5

    # Convert text into embeddings
    vectors = embeddings.embed_documents(texts) #6
    vectors = np.array(vectors, dtype=np.float32) #7 

    # Store in FAISS
    index.add(vectors) #8
    vector_store[len(vector_store)] = (filename, texts) #9

    return "✅ Document stored successfully!" #10

```

1. Llamamos a la función "store_in_faiss" y toma como entrada el texto (text) y el nombre del archivo (filename).

2. Vamos a crear un uso global, índice global (index) y almacén de vectores (vector_store) para almacenar el documento.

3. Mensaje de Streamlit diciendo: Almacenando documento {nombre_archivo} en FAISS..."

4. Dividimos el texto en fragmentos. Pondremos el tamaño de fragmento del splitter a 500 carácteres, y superposición de fragmento a 100 carácteres. La superposición asegura que no se pierda información importante entre los fragmentos.

5. Esto divide el texto en fragmentos más pequeños de 500 carácteres con una superposición de 100 carácteres.

6. Ahí empezamos a convertir texto en incrustaciones. Esta línea hace convertir los fragmentos de texto en incrustaciones usando el modelo de Hugging Face.

7. Después convierte las incrustaciones en un array de numpy en formato float32 (dtype=np.float32).ectores 

8. Empezaremos a almacenar en FAISS. Así que diremos "index" que añada vectores, que lo guardará como un almacén de vectores.

9. Mediremos la longitud de los datos incrustados con el nombre del archivo y los textos.

10. Devolveremos una respuesta de que el documento se almacenó con éxito.

## Función retrieve_and_answer

Vamos a escribir la función para *recuperar fragmentos y responder preguntas*:

```py
# Function to retrieve relevant chunks and answer questions
def retrieve_and_answer(query): #1
    global index, vector_store #2

    # Convert query into embeddings
    query_vector = np.array(embeddings.embed_query(query), dtype=np.float32).reshape(1, -1) #3

    # Search FAISS
    D, I = index.search(query_vector, k=2) # Retrieve top 2 similar chunks #4

    context = "" #5
    for idx in I[0]: #6
        if idx in vector_store: #7
            context += " ".join(vector_store[idx][1]) + "\n\n" #8

    if not context: #9
        return "🤖 No relevant data found in stores documents." #10

    # Ask AI to generate an answer
    return llm.invoke(f"Based on the following document context, answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:") #11
```

1. Llamaremos a la función "retrieve_and_answer" y toma como entrada el índice global de consultas (query). Esto tomará la consulta (query) de un usuario y recuperará fragmentos de texto relevantes de los documentos almacenados.

2. Usaremos el uso global "index" y "vector_store".

3. Procederemos a convertir una consulta en incrustación, empezando por el vector de consulta (query_vector). Convierte la consulta del usuario en una representación vectorial y la reformatea par asegurar la compatibilidad con los archivos.

4. Una vez que se ejecuta el vector de consulta, lo siguiente es proceder a buscar en los archivos. Esta línea busca en los archivos los dos fragmentos de texto más relevantes, por eso "k=2" muestran los dos vecinos más cercanos principales.

5. Pondremos contexto igual a texto vacío.

6. Esta línea es para recuperar los fragmentos coincidentes para el índice.

7. Condición si "idx" está en "vector_store".

8. En cso verdadero, esta línea extrae fragmentos de documentos relevantes basados en los índices recuperados, y luego los concatena en una cadena de contexto.

9. Vamos a manejar el caso cuando no se encuentra ningún dato relevante.

10. Si no hay contexto, nos devuelve un mensaje que no se encontraron datos relevantes en los documentos almacenados.

11. Aquí generamos la respuesta de la IA. Le pediremos que genere una respuesta a la IA. Así que devuelve la invocación del modelo de IA que envía el contexto del documento recuperado y la consulta del usuario al modelo de IA o Ollama LLM, y el modelo genera una respuesta basada en el texto recuperado.

## Interfaz UI (Web UI)

Vamos a continuar y comenzar con nuestra interfaz web de Streamlit:

```py
# Streamlit Web UI
st.title("📋 AI Document Reader & Q&A Bot") #1
st.write("Upload a PDF and ask questions based on its content!") #2

# File uploader for PDF
uploaded_file = st.file_uploader("📂 Upload a PDF Document", type=["pdf"]) #3
if uploaded_file: #4
    text = extract_text_from_pdf(uploaded_file) #5
    store_message = store_in_faiss(text, uploaded_file.name) #6
    st.write(store_message) #7

# User input for Q&A
query = st.text_input("❓ Ask a question based on the uploaded document:") #8
if query: #9
    answer = retrieve_and_answer(query) #10
    st.subheader("🤖 AI Answer:") #11
    st.write(answer) #12
```

1. Empezaremos con el título HTML que dice "Lector de documentos IA y Bot de preguntas y respuestas".

2. A continuación escibimos mensaje que dice "Sube un PDF y haz preguntas basadas en su contexto".

Esto configura el título básico de la interfaz y la descripción de la aplicación.

3. Vamos a continuar creando el cargador de archivos para PDF. En esta línea diremos que subimos un documento PDF y el tipo es PDF. Esto asegura que cuando el usuario busque solo le proporcionarña archivos PDF.

4. Condición Si se sube el archivo PDF.

5. En caso afirmativo, llamamos a la función para que extraiga texto del PDF.

6. Luego, mostraría un mensaje de almacenamiento llamando a la función que almacena en FAISS.

7. Después de la función obtendrá el mensaje de almacenamiento.

8. A continuación crearemos la entrada de usuario para hacer preguntas. Decimos Consulta igual a la entrada de texto para hacer una pregunta basada en el documento subido.

9. Condición Si se ha hecho una pregunta de usuario.

10. En caso afirmativo, responde con la función que usamos para recuperar contenido y responder.

11. Escribimos subencabezado de la respuesta IA.

12. Escribimos respuesta. Proporciona un cuadro de entrada de texto para que los usuarios hagan preguntas y llaman a "recuperar y responder consulta" para obtener una respuesta y mostrarla.

## Resumen 

Así que esa es toda nuestra aplicación. Este tipo de código carga los modelos de IA necesarios (OllamaLLM y HuggingFace). 

Divide el texto en fragmentos más pequeños y almacena los embeddings en archivos. 

Luego recupera los fragmentos relevantes basado en las consultas de los usuarios.

Pasa el texto recuperado al modelo de IA para generar una respuesta y luego proporciona una interfaz de usuario basada en Streamlit para una interacción fácil.

Así que vamos adelante 🚀

Antes de ejecutarlo, quiero saber más sobre esta aplicación, sobre cómo usarla, así que espero que hayas podido seguir y lograr implementarlo.

Nuestro siguiente paso será entender qué hace este lector.

Anterior página: Dependencias --> [**Click aquí**](./04a_Dependencias.md)

Siguiente página: Cómo funciona el Lector de Documentos de IA --> Proximamente...