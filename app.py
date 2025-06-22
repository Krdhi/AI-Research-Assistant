# AI Research Assistant (Python 3.13 compatible for PyCharm)

# Required packages: Run as separate block if using Colab
# pip install gradio pymupdf openai requests beautifulsoup4

# Required packages: Run this command on the terminal if using Pycharm/VScode
# pip install -r requirements.txt

import gradio as gr
import fitz  # PyMuPDF
import openai
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from io import BytesIO

# Extract text from PDF
def extract_text_from_pdf(file_obj):
    file_data = file_obj.read()
    doc = fitz.open(stream=BytesIO(file_data), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Extract text from URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    return "\n".join(p.get_text() for p in paragraphs)

# Analyze with GPT-4
def analyze_text(api_key, input_type, pdf_file, url):
    client = OpenAI(api_key=api_key)
    try:
        if input_type == "PDF" and pdf_file is not None:
            text = extract_text_from_pdf(pdf_file)
        elif input_type == "URL" and url:
            text = extract_text_from_url(url)
        else:
            return "Please provide valid input."

        prompt = f"""
        Analyze the following content and return:
        - Bullet-point summary of key ideas
        - Any contradictions found
        - Tags for major topics or themes

        Content:
        {text[:6000]}
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert research assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
def create_ui():
    with gr.Blocks() as demo:
        api_key = gr.Textbox(label="OpenAI API Key", type="password")
        input_type = gr.Radio(["PDF", "URL"], label="Select Input Type")
        pdf_file = gr.File(label="Upload PDF", file_types=[".pdf"])
        url = gr.Textbox(label="Enter URL")
        output = gr.Textbox(label="Output Summary", lines=15)

        def wrapped_analyze(api_key_val, input_type_val, pdf_val, url_val):
            return analyze_text(api_key_val, input_type_val, pdf_val, url_val)

        run_btn = gr.Button("Run Analysis")
        run_btn.click(fn=wrapped_analyze, inputs=[api_key, input_type, pdf_file, url], outputs=output)

    demo.launch(share=True)

if __name__ == "__main__":
    create_ui()
