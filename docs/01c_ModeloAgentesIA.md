# Modelo para Agentes de IA

Ahora que está configurado Ollama, nuestro siguiente paso es descargar un modelo para agentes de IA.

Necesitaremos un **modelo de IA** para ejecutar nuestros agentes de IA. Así que, por ahora, descargaremos *Mistral*.

Sitio web --> [Ollama](https://ollama.com/)

Volvemos a la página oficial de Ollama. Accedemos a Modelos (Models) en la parte superior izquierda, y desde ahí ver todos los diferentes modelos disponibles (glm-4.7-flash, lfm2.5-thinking, translategemma...).

---

Al principio saldrá una lista de modelos que, por defecto, están ordenados por "Popular". Puedes cambiarlo a "Newest" para ver el modelo más reciente, y podemos ver el primero de la lista que estará actualizado entre 3 y 7 días.
En los filtros podemos ver modelos de **incrustación (Embedding)**, modelos de **visión (Vision)** y modelos de **herramientas (Tools)**. Así que todos los modelos están disponibles para tí.

Ahora, iremos a la barra de búsqueda y buscar "mistral", ya que queremos instalar Mistral. Elegiremos el siguiente modelo:

![Mistral Modelo](./img/mistral.png)

Ve a Mistral, selecciona Mistral aquí y luego copiamos la siguiente palabra --> mistral

---

Regresamos al símbolo del sistema en la ruta de donde estábamos:

```bash
C:/Users/alumno/Desktop/AIAgents$
# Ejecutamos el siguiente comando
ollama pull mistral

# Esperamos unos minutos a que se descargue el modelo
# Consejo: Asegúrate de tener un buen almacenamiento, ya que contiene 4.4 GB.
# Si lo instalas una vez, no tomará mucho tiempo ejecutarlo de nuevo. 
# Saldría un resultado así:

pulling manifest
pulling f5074b1221da: 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████▏ 4.4 GB
pulling 43070e2d4e53: 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████▏  11 KB
pulling 1ff5b64b61b9: 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████▏  799 B
pulling ed11eda7790d: 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████▏   30 B
pulling 1064e17101bd: 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████▏  487 B
verifying sha256 digest
writing manifest
success
```

También tienes disponibles más modelos populares como son "llama3", "deepseek", "gemma", entre otros. Los puedes buscar en la barra de busqueda y copiar más nombres de modelos de IA.

```bash
ollama pull deepseek-r1
ollama pull gemma
```

Si se vuelve a instalar de nuevo "mistral" con el mismo comando, saldría instantáneo porque ya se encuentra disponible para construir nuestro agente de IA.

Así que asegúrate de tenerlo disponible. descárgalo antes de pasar al siguente proyecto.

Además, otra cosa que debes recordar es que estaremos escribiendo algo de código en Python y hay una sección disponible sobre aprender un poco de Python basado en lo que usaremos en toda esta serie de tutoriales.

Así que si eres nuevo en Python te recomendaría que vayas a dicha sección y lo aprendas.

Si no has instalado Python, te recomendaría ir a [Python](https://www.python.org/) y seguir los pasos para descargar Python para Mac, Linux o Windows del que estés usando.