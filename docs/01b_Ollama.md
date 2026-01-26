# Ollama

## ¿Qué es Ollama?

Ollama es una *herramienta de inteligencia artificial (IA) generativa* diseñada para permitir a los usuarios generar contenido nuevo y realizar análisis avanzados de datos mediante modelos de lenguaje.

## ¿Porqué usar Ollama para los Agentes de IA?

1. **Ejecuta los modelos de IA localmente**: No hay costo de API y es completamente privado. Eso significa que todo lo que haces está en tu máquina. No es necesario una conexión a Internet. Una vez que tienes los modelos descargados localmente, todo lo que haces permanece en tu máquina.
2. **Admite modelos abiertos**: Hay modelos como LLaMA 3, Mistral, Gemma, etc. Todos estos están disponibles para usar en Ollama.
3. **Está optimizado para la inferencia de LLM**: Esto proporciona tiempos de respuesta más rápidos que las APIs basadas en la nube, ya que se ejecuta localmente y los LLM están optimizados debido a la inferencia.
4. **Funciona sin conexión**: Como se mencionó antes, no se requiere Internet después de la configuración. Así que una vez que tienes toda la configuración lista, tienes tus modelos descargados. Puedes simplemente ir en un crucero, estar en cualquier parte del mundo donde no haya Internet y aún así trabajar con los modelos.

# Configuración de Ollama

## Instalar Ollama

Sitio web --> [Ollama](https://ollama.com/)

En ese sitio web encontrarás una opción en la página de inicio para descargar Ollama. Haz click en **Download** en la barra de inicio.

Elige *una de las tres opciones* para el sistema operativo de tu máquina:

- MacOS
Requiere de *macOS 14 Sonoma* o una versión más reciente.

Si tienes masOS, haz click en **Download for masOS**.  Una vez descargado, sigue las indicaciones.

- Linux: 
```bash
# Si quieres ejecutarlo en Linux, copia el siguiente comando: 
curl -fsSL https://ollama.com/install.sh | sh

# Ejecutalo en tu terminal o símbolo del sistema en Linux, y ejecutalo de nuevo.
```

- Windows
Requiere de *Windows 10* o una versión más reciente.

Si tienes Windows, puedes descargar para Windows desde la opción y ejecutarlo. El archivo ejecutable que descargas (archivo .exe), y sigues los pasos para instalarlo.

**Consejo**:
Siempre se aconseja asegurarse de reiniciar tu máquina por si acaso hubiera algunos problemas o inconvenientes, o se necesita configurar algo.

Abrimos símbolo de consola:

```
C:/Users/alumno/Desktop/AIAgents
```

Aparecemos en mi escritorio y está "AIAgents", una carpeta creada por mí. 
Pero no importa en qué máquina estemos ejecutando. Puedes ir al símbolo de sistema y ejecutar:
```bash
ollama --version
```
Si te da una versión "ollama version is 0.5.11", eso significa que el programa está instalado correctamente.
Si no te da una versión, eso significa que hay algo mal.
Si persiste el error ""ollama" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable." u otro error, hazmelo saber en comentarios.

