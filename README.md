# Gemini Q&A Tool (Gradio + LangChain)

This project is built with Gradio, LangChain, and Gemini for answering questions from PDFs:

1. **gradio_qa.py** – Paste or type any text and ask questions based on it.
2. **gradio_pdf.py** – Upload a PDF and ask questions about its content.

## Clone the Repo

Type in terminal:
```bash
git clone https://github.com/AfreenInnovates/gemini-QA-tool.git
cd gemini-QA-tool
```

## Installation

Type in terminal:
```bash
python -m venv venv
```
- Mac: source venv/bin/activate
- On Windows: venv\Scripts\activate

Create `requirements.txt` file in the same directory as of `gemini-QA-tool` and must contain the following:
```bash
gradio 
langchain 
langchain-google-genai 
python-dotenv 
PyMuPDF
```

To install dependencies, type in terminal:
```bash
pip install -r requirements.txt
```
or if above does not work, type
```pip install gradio langchain langchain-google-genai python-dotenv PyMuPDF``` in the terminal

Next, create an `.env` file wthin the project directory and must contain the following:
```bash
GEMINI_API_KEY=put_your_gemini_api_key_here
```
Must create a Gemini API key from here: https://aistudio.google.com/u/0/apikey

<hr>

1. Run the pdf-based QA tool:
```bash
python gradio_pdf.py
```
- Upload a PDF to ask questions from (that has text that can be parsed).
- Ask any question in the next box.
- Output is received in the 2nd column output box.

<hr>

2. Run the text-based QA tool:
```bash
python gradio_qa.py
```
- Put any content to ask questions from in the first box.
- Ask any question in the next box.
- Output is received in the 2nd column output box.
