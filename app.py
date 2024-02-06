"""Gradio application for extracting topics from PDF documents"""
import os
from dotenv import load_dotenv
import gradio as gr
from src.llm_hugging_chat import LlmHuggingChat
from src.topics_from_pdf import topics_from_pdf
from pages.about import intro_html, author_html

# Variables
load_dotenv()  # take environment variables from .env.
email_1 = os.environ.get("HF_EMAIL_1")
psw_1 = os.environ.get("HF_PW_1")
css = """
footer {visibility: hidden}
.feedback textarea {font-size: 40px !important} 
"""

# Functions
def input_lang(language):
    """
    The user is force to introduce the key if openAI model selected.
    """
    return {
        lang_var : language
        }

def summary(file, lang):
    """
    Extracts the PDF topics
    """
    llm = LlmHuggingChat(
        n=2000,
        hugging_face_account=email_1,
        hugging_face_psw=psw_1
        )
    num_topics = 5
    words_per_topic = 30 # optimizar
    file = file.name
    topics = topics_from_pdf(llm, file, num_topics, words_per_topic, lang)
    return {
        output_summary : topics,
    }

with gr.Blocks(css=css, title="Topics from PDF") as demo:

    # State variables
    lang_var = gr.State()

    # Layout
    gr.Markdown("\n")
    gr.HTML('<h1 style="text-align: center;">Topics from PDF</h1>')
    gr.Markdown("\n")

    with gr.Tab("Home"):
        with gr.Row(equal_height=True):
            with gr.Column(scale=25, min_width=0):
                lang_dropdown = gr.Dropdown(
                    choices=[
                        "English",
                        "Español",
                        ],
                    label="Select response language",
                    )
            with gr.Column(scale=75, min_width=0):
                uploaded_file = gr.UploadButton("Upload PDF 📁", file_types=["document"])

        output_summary = gr.Textbox(label="Main topics from the document")

        # Interactivity
        lang_dropdown.input(
            input_lang,
            [lang_dropdown],
            [lang_var]
            )
        uploaded_file.upload(
            summary,
            [uploaded_file, lang_var],
            [output_summary],
            queue=False
            )

    # About Tab
    with gr.Tab("About"):
        gr.HTML(intro_html)
        gr.HTML(author_html)

    gr.Markdown("Version 0.1")

demo.queue(max_size=10, api_open=False)
demo.launch(server_name="0.0.0.0", server_port=8080, share=False)
