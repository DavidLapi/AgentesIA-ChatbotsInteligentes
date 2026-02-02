# Construir el Asistente de Voz de IA

Nuestro paso siguiente es **construir el asistente de voz**. 

Empezaremos por crear el **script de Python** que *escucha*, *procesa* y *responde*.

Así que vamos a crear un nuevo archivo en la carpeta de datos (Day 2), y a este archivo lo llamaremos "ai_voice_assistant.py".

Una vez creado vamos a importar las bibliotecas que instalamos anteriormente:

```py
import speech_recognition as sr # <-- Importa el módulo de reconocimiento de voz para convertir el habla en texto
import pyttsx3 # <-- Importa la biblioteca pyttsx3 para la conversión de texto a voz
from langchain_community.chat_message_histories import ChatMessageHistory # <-- Para almacenar el historial de mensajes de chat
from langchain_core.prompts import PromptTemplate # <-- Define el formato de los prompts de IA
from langchain_ollama import OllamaLLM # <-- Utilidad para el modelo de IA
```

El siguiente paso es cargar el modelo de IA:

```py
# Load AI Model
llm = OllamaLLM(model="mistral") # Change to "llama3" or another Ollama model
```

De nuevo, puedes reemplazar "mistral" con otros modelos como "llama3", "gamma" o cualquier otro modelo que hayas instalado.

Ahora inicializaremos nuestro historial de chat:

```py
# Initialize Memory (LangChain v1.0+)
chat_history = ChatMessageHistory()
```

De nuevo, esto almacena conversaciones pasadas entre el usuario y la IA dentro de él. Es útil para respuestas conscientes del contexto que necesitaríamos o que necesitamos en cualquier aplicación de chat hoy en día.

A continuación voy a proceder a inicializar el motor de texto a voz.

```py
# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
```

Esto inicializa el motor de texto a voz. Luego voy a decir:

```py
engine.setProperty("rate", 160) # Adjust speaking speed
```

Esto es para ajustar la velocidad de habla. El valor predeterminado para la velocidad suele ser alrededor de 200, así que ajustamos el valor a 160 para que el habla sea un poco más lento para mayor claridad.

A continuación vamos a inicializar el reconocimiento de voz:

```py
# Speech Recognition
recognizer = sr.Recognizer()
```

Recordemos que "sr" es el reconocimiento de voz (speech_recognition) que hemos agregado al importar. Esto creará una instacia de reconocedor de voz para convertir el habla en texto.

A continuación escribamos nuestra **función** para hablar:

```py
# Function to Speak
def speak(text):
```

Dentro de la función escribimos:

```py
    engine.say(text)
```

Esto es un texto que envía al motor de voz. Debajo de esa línea escribimos:

```py
    engine.runAndWait()
```

Esto procesa y pronuncia el texto. Así que, hasta que el texto sea hablado, va a esperar.

Procedemos a escribir otra **función para escuchar**. Esto es conversión de voz a texto:

```py
# Function to listen
def listen():
    with sr.Microphone() as source:
```

El reconocimiento de voz utiliza el micrófono de punto como fuente, por lo que utiliza el micrófono para capturar la entrada de audio. Así que dentro de sr.Microphone() voy a imprimir "Escuchando..." para que sepamos que el micrófono está activo y encendido ahora mismo:

```py
        print("\n🎤 Listening...")
```

A continuación voy a decir:

```py
        recognizer.adjust_for_ambient_noise(source)
```

Esto reduce el ruido de fondo. Por eso busca de alguna manera **bordes para ruidos ambientales**.

A continuación escribimos:

```py
        audio = recognizer.listen(source)
```

Esto graba el discurso de nuestros usuarios.

Así que lo que vamos a hacer es intentar consultar para obtener una consulta para reconocerlo o reconocer Google Audio:

```py
    try:
        query = recognizer.recognize_google(audio)
```

Esto convierte el habla en texto. Utiliza la API de reconocimiento de voz de Google para convertir el habla en texto. Nuevamente, no nos hemos registrado para ello, pero está disponible para nosotros.

A continuación, imprimimos:

```py
        print(f"💡 You Said: {query}")
```

Cualquier cosa que sea esa consulta que obtengamos, la imprimiremos y luego finalmente devolvemos la consulta:

```py
        return query.lower()
```

A continuación vamos a proceder a buscar excepciones, así que empezamos por buscar *Error de valor desconocido*:

```py
    except sr.UnknownValueError:
```

Si no se reconoce el habla, le pide al usuario que repita. Así que imprimiremos "Lo siento, no pude entender. Intenta de nuevo y sal de eso":

```py 
        print("🤖 Sorry, I couldn`t understand. Try again!")
        return ""
```

Otra excepción es el *error de solicitud*:

```py
    except sr.RequestError:
```

Si el servicio de Google está caido o inaccesible, notifica al usuario.

```py
        print("☣️ Speech Recognition Service Unavailable")
        return ""
```

Ahora vamos a proceder a decir **Crear nuestro formato de aviso de chat de IA**. Vamos a escribir lo siguiente:

```py
# AI Chat Prompt
prompt = PromptTemplate(
    imput_variables=["chat_history", "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:",
)
```

Lo que hace esto es definir cómo la IA debe generar respuestas. El historial de chat (chat_history) almacena la conversación pasada. La pregunta (question) es la última entrada del usuario.

Así que, con estas variables vamos a crear la plantilla (template) que tiene la conversación anterior. El "chat_history" es lo que tenemos y la "question" del usuario está aquí, y la respuesta de la IA se mostrará al final de la frase.

Entonces, la IA ve el mensaje anterior y la nueva pregunta del usuario antes de generar una respuesta.

A continuación vamos a crear una **función para procesar las respuestas de la IA**:

```py
# Function to Process AI Responses
def run_chain(question):
```

Dentro de la función, recuperaremos el historial de chat pasado manualmente:

```py
    # Retrieve past chat history manually
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])
```

Con esto lo quehace es recuperar los mensajes pasados del historial de chat y formatearlos aquí.

A continuación, ejecutaremos la generación de respuestas de la IA:

```py
    # Run AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text, question=question))
```

Esto genera respuestas de IA formateando el prompt, enviándolo al modelo Ollama LLM mistral y obteniendo la respuesta de la IA.

Una vez tenga esto, vamos a almacenar la nueva entrada del usuario y la respuesta de la IA en la memoria:

```py
    # Store new user input ans AI response in memory
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)
```

Y finalmente, devolvemos la respuesta de la IA para ser hablada o mostrada:

```py
    return response
```

Una vez terminada la función, vayamos a crear nuestro **buble principal** donde vamos a escribir:

```py
# Main Loop
speak("Hello! I am your AI Assistant. How can I help you today?")
```

Este es sólo un mensaje de saludo para que el usuario comience a hablar. Así que vamos a escribir nuestro bucle:

```py
while True:
    query = listen()
```

La variable "query" escucha continuamente la entrada del usuario.

A continuación vamos a decir si salir en consulta o detener en consulta:

```py
    if "exit" in query or "stop" in query:
        speak("Goodbye! Have a nice day.")
        break
```

Si el usuario dice "stop" o "exit", va a decir el programa "Adios! Que tengas un buen día.", y sal de este bucle (break).

Después escribiremos:

```py
    if query:
        response = run_chain(query)
        print("\n🤖 AI Response: {response}")
        speak(response)
```

Si hay consulta, ejecutaremos la función "run_chain" para procesar las respuestas de la IA y pasar la pregunta que el usuario ha pasado.

A continuación, imprimiremos la respuesta de la IA que sea la respuesta que obtenemos y pronuncia la respuesta. speak(response) pronunciará o leerá la respuesta que devuelve.

Y hasta aquí, ya hemos terminado toda nuestra aplicación, como podemos ver en el archivo. En la siguiente sección, vamos a continuar y hablar sobre ello de lo que hemos hecho aquí.

Hemos creado el script de Python que escucha, procesa y responde. 🎉

Anterior --> [**Click aquí**](./02a_Dependencias.md)

Siguiente --> [**Click aquí**](./02c_ArrancarAsistente.md)