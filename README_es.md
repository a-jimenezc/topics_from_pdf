# Pregutna al PDF

[English](README.md) | Español

Este repositorio contiene el código fuente para la aplicación web: Topics from PDF. La aplicación permite a los usuarios cargar un documento PDF y, independientemente de su tamaño, extraer los temas principales de él. La aplicación admite respuestas tanto en inglés como en español. Utiliza el modelo utilizado por [HugingChat](https://huggingface.co/chat/), a través de una [API no oficial de HuggingChat en Python](https://github.com/Soulter/hugging-chat-api); se proporcionan más detalles a continuación.

## Requisitos

* **Versión de Python:** 3.10
* **Bibliotecas:** langchain, pypdf, nltk, gensim, gradio, hugchat.
* **Instalación:** requirements.txt

## Uso

### Aplicación Web
La forma más sencilla de probar la aplicación es seguir el enlace:

[https://topicspdf.dsapp.me/](https://topicspdf.dsapp.me)

Fue implementada con Docker y utilizando el servicio *serverless* de Google, *Cloud Run*.

### Instalación Local
Para ejecutar la aplicación web localmente, instalar Python 3.10 y Git. Luego, ejecutar en la terminal:

```bash
export HF_EMAIL_1=your.registered.email@mail.com
export HF_PW_1=your_HuggingChat_password
```

```bash
git clone https://github.com/a-jimenezc/topics_from_pdf.git
cd  topics_from_pdf
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

**HF_EMAIL_1** y **HF_PW_1** son las credenciales para una cuenta de HuggingChat. Es necesario registrarse para obtener una cuenta.

## Descripción del Proyecto

El objetivo principal de este proyecto es permitir la extracción de los temas e ideas principales de un documento PDF, independientemente de su tamaño y sin incurrir en costos adicionales. Esto se logró con la ayuda de bibliotecas y recursos de código abierto:

### Resumen con LDA
Proporcionar un resumen conciso del documento ayuda al usuario a comprender su contenido, facilitando el inicio de la conversación. Los Grandes Modelos de Lenguaje (LLMs) pueden resumir documentos documentos, pero el costo computacional para documentos extensos hace que usarlos directamente para esta tarea sea prohibitivamente caro. Por lo tanto, se efectuó preprocesamiento. **LDA** (Latent Dirichlet Allocation) es un gran algoritmo para el procesamiento de documentos. Produce una lista de palabras por tema, y permite seleccionar el número de temas y palabras por tema. Luego, las listas de palabras resultantes podrían ingresarse a un LLM, pidiéndole que articule una descripción utilizando lenguaje natural. Este enfoque ayuda a extraer las ideas principales del documento. En este caso, el resumen se presenta en un formato de tabla de contenido.

### HugChat, API de Chat de Hugging no oficial
La biblioteca [hugchat](https://github.com/Soulter/hugging-chat-api) creada por Soulter ofrece una API no oficial para [HuggingChat](https://huggingface.co/chat/). Actualmente, el modelo usado por HuggingChat es **mistralai/Mixtral-8x7B-Instruct-v0.1**, pero esto puede cambiar con el tiempo. Por lo tanto, se aplican **los términos de uso, limitaciones, advertencias y licencias** estipulados por HuggingChat y el modelo que utiliza al usar esa aplicación web. Por favor, visita la documentación oficial para obtener más información.

### Gradio
La aplicación fue construida con Gradio. Ofrece soporte tanto para el backend como para el frontend de aplicaciones de aprendizaje automático. Además, tienen un excelente soporte para modelos de lenguaje, incluido un objeto de chat muy útil.

### LangChain, la biblioteca de orquestación
LangChain hizo posible este proyecto. Ofrece un conjunto completo de herramientas para trabajar con LLMs, incluidas plantillas para *prompts*, bases de datos de vectores y más.

## Licencia
GNU General Public License v3.0

## Descargo de Responsabilidad
Esta aplicación se basa en bibliotecas y recursos de terceros. En consecuencia, su utilización está sujeta a términos de uso, condiciones y licencias específicas que se aplican a estas bibliotecas y recursos externos.

## Autor
[Antonio Jimenez Caballero](https://www.linkedin.com/in/antonio-jimnzc/)
