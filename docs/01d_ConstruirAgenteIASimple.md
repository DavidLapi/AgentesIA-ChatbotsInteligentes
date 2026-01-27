# Construir un Agente de IA Simple

Ahora que tenemos todo nuestro entorno configurado, vamos a construir **un agente de IA simple**.

Aquí vamos a construir un **chatbot** impulsado por IA usando **LangChain + Ollama**.

1. El primer paso será instalar los paquetes necesarios.
2. Luego procederemos a crear un archivo Python que se llamará *basic_ai_agent.py*.

## Empecemos

Accedemos a nuestro VS Code y nos dirigimos a nuestra ruta: C:/Users/alumno/Desktop/AIAgents$

Crearemos un directorio llamada "Day1". Dentro de ese directorio crearemos un nuevo archivo. Lo llamaremos *basic_ai_agent.py*.

Ahora, nuestro primer paso mencionado anteriormente es instalar los paquetes necesarios. Así que accederemos a la terminal de VS Code:

```bash
PS C:\Users\alumno\Desktop\AIAgents>
```

Para comprobar de que está instalado Python, comprobaremos los siguientes datos:

```bash
PS C:\Users\alumno\Desktop\AIAgents> python --version
Python 3.13.4
# Si nos sale la versión de Python, es que se ha instalado correctamente.
# Vamos a comprobar en qué ruta estamos
PS C:\Users\alumno\Desktop\AIAgents> pwd

Path
----
C:\Users\alumno\Desktop\AIAgents

# Accedemos a nuestro directorio Day1 y comprobamos si está el archivo creado.
PS C:\Users\alumno\Desktop\AIAgents> cd Day1
PS C:\Users\alumno\Desktop\AIAgents\Day1> ls

Directorio: C:\Users\alumno\Desktop\AIAgents\Day1

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        27/01/2026     11:15              0 basic_ai_agent.py

# Limpiamos la pantalla de la terminal con cls
PS C:\Users\alumno\Desktop\AIAgents\Day1> cls
```

## Instalar paquetes

```bash
# Ejecutamos el comando: pip install langchain langchain-community langchain-ollama
PS C:\Users\alumno\Desktop\AIAgents\Day1> pip install langchain langchain-community langchain-ollama
```

## ¿Qué significan estos comandos?

langchain, langchain-community, langchain-ollama --> Estas son las bibliotecas necesarias que puedes usar.

## El comando "pip"

El comando pip es algo que viene con Python. Si no está allí, probablemente tendrás que proceder a instalarlo. Para comprobar si está instalado, ejecuta el siguiente comando:
```bash
pip --version
# Resultado:
pip 25.1.1 from C:\Users\alumno\AppData\Local\Programs\Python\Python313\Lib\site-packages\pip (python 3.13)
```

Puedes abrir la terminal y simplemente decir, **pip, instalar langchain**; y LangChain será descargado e instalado.

## LangChain

Si nunca has oído hablar de LangChain, la funcionalidad principal te ayuda para construir aplicaciones basadas en **LLM (Large Language Model o Modelo de Lenguaje Grande)**. Proporciona componentes como cadenas para comibinar diferentes funcionalidades de LLM. 

También admite la integración con varios proveedores de LLM como **OpenAI y Huggingface**, y por eso estamos instalando LangChain.

## LangChain Community

**LangChain Community** es una adicional desarrollada por la comunidad de LangChain con nuevas características y funcionalidades. 

Se sigue actualizando, así que es bueno mantenerlo. Quiere ecir, instalarlo cada vez solo para que si hay nuevas características o algo nuevo que estés usando esté disponible para tí.

Y a menudo incluye características experimentales o soporte para casos de uso específicos, por lo que es muy útil.

## LangChain Ollama

Esta biblioteca permite a los usuarios aprovechar Ollama para ejecutar LLM de código abierto localmente dentro de sus aplicaciones de linterna

Permite **privacidad y control** sobre los datos ejecutando modelos en nuestra máquina local,así que eso es lo que estaremos haciendo.

Vamos a proceder a ejecutar el comando **pip install langchain langchain-community langchain-ollama**. Saldrá un montón de dependencias a descargar e instalar, y nos llevará unos minutos a proceder el comando. Si sale algún error, hazmelo saber para solucionarlo.

## Agente de IA básico

Nuestro siguiente paso es escribir el código en nuestro archivo (basic_ai_agent.py) para nuestro agente de IA básico.

Empezaremos por importar Ollama LLM, así que en la primera línea de código escribiremos lo siguiente:

```py
from langchain_ollama import OllamaLLM
```

Lo que hace esta primera línea es que está importando la clase **"OllamaLLM"** del paquete **"langchain_ollama"** que instalamos previamente.

**OllamaLLM** es una implementación de un modelo de lenguaje que utiliza Ollama, un marco para ejecutar e interactuar con modelos de IA que ya hemos instalado y está funcionando en nuestra máquina.

Ahora, esto nos permite interactuar con modelos de IA como Mistral que hemos instalado. También puedes usar la matriz u otros a través de LangChain para que esté disponible para nosotros.

En la siguiente línea escribiremos lo siguiente:

```py
# Load AI Model from Ollama
llm = OllamaLLM(model="mistral")
```

La variable "llm" inicializa el modelo de IA. El modelo *OllamaLLM(model="mistral")* crea una instancia de la clase LLM y la asigna a la variable LLM. Ahora Mistral especifica el modelo que se está utlizando. Puedes reemplazarlo por "deepseek-r1" o "gemma" o cualquier otro modelo que desees.

Ahora, el objeto "llm" se usará más tarde para generar respuestas basadas en la entrada del usuario, así que tenlo en cuenta.

Escribiremos la siguiente línea:

```py
print("\nBienvenido a tu Agente de IA! Preguntame algo...")
```

Este es un mensaje que le vamos a mostrar al usuario en la CLI. Así que eso se ejecutará.

Una vez escrito el mensaje, escribiremos lo siguiente:

```py
while True:
    question = input("Make your question (or write 'exit' to stop the machine): ")
    if question.lower() == "exit":
        print("Good bye, begginner!")
        break
    response = llm.invoke(question)
    print("\n Response for IA: ", response)
```

1. **while True:**

Ejecutaremos un bucle "while". Esto hace que, mientras sea verdadero (True), se ejecutará constantemente y hará preguntas al usuario.

2. **question = input("Make your question (or write 'exit' to stop the machine): ")**

Dentro del bucle "while", creamos una variable de pregunta (question) y añadimos un "input" para tomar la entrada al usuario. Es decir, que después de mostrar el mensaje, esperará a que el usuario especifique algo. El usuario tiene dos opciones, de escribir una pregunta o escribe 'exit' para detener el bucle "while".

3. **if question.lower() == "exit":**

Aquí se verifica una función ifelse por si ve la palabra "exit". Si por un casual la máquina ve "Exit" con alguna mayúscula de por medio, la variable lo convierte en minúscula automáticamente con la función *lower()*.

4. **print("Good bye, begginner!")**

Muestra el mensaje de despedida al escribir la palabra "exit".

5. **break**

Después del mensaje de despedida, se termina el bucle con la condición "break". Esto cierra la aplicación.

6. **response = llm.invoke(question)**

Si el usuario escribió una pregunta, se declara una variable "response" que se encarga de hacer que la variable "llm" pueda invocar (invoke) una respuesta del modelo de IA al usuario. Así que "question" se pasará dentro de la funcion "invoke". Esta línea realmente pasa la pregunta al modelo de IA y genera y obtiene una respuesta del modelo. Así que la respuesta se almacena de nuevo en la variable "response".

7. **print("\n Response for IA: ", response)**

Una vez declarado response, hay que imprimir la respuesta de la IA. Y con esto sería todo.

## Prueba

Ya tenemos nuestro agente de IA funcionando. Ahora llegó la hora de ejecutar el archivo para comprobar si funciona. Abrimos la terminal y nos dirigimos a nuestra ruta con el archivo almacenado. Una vez dentro, ejecutaremos el siguiente comando:

```bash
C:\Users\alumno\Desktop\AIAgents\Day1> py .\basic_ai_agent.py
# Nos saldría un resultado así:

Welcome to your Agent IA! Ask me something...
Make your question (or write 'exit' to stop the machine): 

# Le haremos una pregunta en inglés para empezar, porque el modelo instalado no es multiidioma.
# Le preguntaremos algo como: Qué es IA?
# Nos saldría una respuesta como esta:
# ---
# Response for IA:   IA, or Intelligent Assistants, refer to computer systems and software designed to perform tasks for human users. These tasks can range from answering questions, making recommendations, scheduling appointments, sending messages, or even controlling other applications. Examples of Intelligent Assistants include virtual assistants like Siri, Alexa, Google Assistant, and Cortana. They are powered by artificial intelligence (AI), natural language processing (NLP), and machine learning (ML) technologies to understand user requests and respond in a conversational manner. The goal is to make interactions with technology more seamless, intuitive, and human-like.
# ---

```

# Y listo 🥳 

Ya tenemos nuestro primer chatbot básico para poder aprender.
