# Cómo funciona el asistente de IA

Ahora que hemos creado nuestro script, aún no lo hemos probado. Pero hablemos de cómo funciona el asistente de IA. Lo que hace es:

- Escuchar la entrada de voz del usuario usando un micrófono. 

Así que, tan pronto como ejecutes esa aplicación, activará tu micrófono y comenzará a escuchar tu voz. También especificará como viste, como escribimos, escuchando punto, punto, punto (...). Así que le dirá al usuario que está escuchando su texto.

- Entiende y procesa la consulta usando el reconocimiento de voz (Speech Recognition). 

Y luego utiliza Ollama LLM para generar respuestas inteligentes.

- Habla la respuesta de vuelta al usuario usando Text-to-Speech (texto a voz).

Así que enviará el mensaje a Ollama basado en lo que has enviado.

También enviará el historial de chat y luego te devolverá la respuesta que será convertida de texto a voz, y te lo dirá en voz alta.

- Finalmente, sigue funcionando hasta que el usuario diga "exit" o "stop".

Resumiendo bien el código del archivo anterior (ai_voice_assistant.py), así es cómo funciona todo este asistente de inteligencia artificial ahora mismo. 

Anterior --> [**Click aquí**](./02b_AsistenteDeVoz.md)

Siguiente --> [**Click aquí**](./02d_EjecutarAsistente.md)