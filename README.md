# Topics from PDF

English | [Español](README_es.md)

This repository contains the source code for the web application: Topics from PDF. The application enables users to upload a PDF document and, regardless of its size, extract the main topics from it. The application supports responses in English as well as in Spanish. It utilizes the model serving [HugingChat](https://huggingface.co/chat/) as its language model, through an [Unofficial HuggingChat Python API](https://github.com/Soulter/hugging-chat-api); further details are provided below.

## Requirements

* **Python version:** 3.10
* **Libraries:** langchain, pypdf, nltk, gensim, gradio, hugchat.
* **Installation:** requirements.txt

## Usage

### Web App
The simplest way to try the app is to follow the link:

[https://topicspdf.dsapp.me](https://topicspdf.dsapp.me)

It was deployed with Docker and using the serverless service from Google, *Cloud Run*.

### Local installation
To run the web app on a local machine running Linux, install python 3.10 and git. Then, run on the terminal:

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

**HF_EMAIL_1** and **HF_PW_1** are the credentials for a HuggingChat account. It is required to register an account.

## Project Description

The main goal of this project is to enable the extraction of the main topics and ideas from a PDF document, regardless of its size and without incurring any additional cost. This was achieved with the help of open source libaries and resources:

### Summarization with LDA
LLMs can summarize documents, but the computational cost for large documents makes using them for this task prohibitively expensive. So, some preprossessing was needed. **LDA** (Latent Dirichlet Allocation) is a great algorithm for document processing. It produces a list of words per topic; it also allows the selection of the number of topics and words per topic. Then, the output word lists could be feeded into an LLM and ask, prompting it to articulate a description using natural language. This approach aids in extracting the core ideas from the document. In this case, the "summary" is given in a table-of-content format.

### HugChat, Unofficial Hugging Chat API
The library [hugchat](https://github.com/Soulter/hugging-chat-api) by Soulter offers an unofficial API for [HuggingChat](https://huggingface.co/chat/). Currently, the model powering HuggingChat is **mistralai/Mixtral-8x7B-Instruct-v0.1**, but this can change over time. So, **the terms of use, limitations, caveats, and licencing** stipulated by HuggingChat and the model it is using apply when using this web application. Please, visit the oficial documentation for more information.

### Gradio
The application was built with gradio. It offers back-end and front-end support for machine learning applications. Also, they have an exelent support for language models.

### LangChain, the orchestration library
LangChain made this project possible. It offers a rich set of tools for working with LLMs, including template for prompts, vector databases, and more.

## Licence
GNU General Public License v3.0

## Disclaimer
This application relies on third-party libraries and resources. Consequently, its utilization is subject to specific terms of use, conditions, and licenses that pertain to these external libraries and resources.

## Author
[Antonio Jimenez Caballero](https://www.linkedin.com/in/antonio-jimnzc/)
