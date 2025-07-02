# Gemini Q&A Tool (Gradio + LangChain)

This project is built with Gradio, LangChain, and Gemini for answering questions from PDFs:

1. **gradio_qa.py** – Paste or type any text and ask questions based on it.
2. **gradio_pdf.py** – Upload a PDF and ask questions about its content.

## Installation

```bash
# Creating a virtual environment
python -m venv venv
# Mac: source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt

```

`requirements.txt` file
```bash
pip install gradio langchain langchain-google-genai python-dotenv PyMuPDF
```

`.env` file: Create this file wthin the project root
```bash
GEMINI_API_KEY=put_your_gemini_api_key_here
```

1. Run the text-based QA tool:
```bash
python gradio_qa.py
```
- Put any content to ask questions from in the first box.
- Ask any question in the next box.
- Output is received in the 2nd column output box.


2. Run the pdf-based QA tool:
```bash
python gradio_pdf.py
```
- Upload a PDF to ask questions from (that has text that can be parsed).
- Ask any question in the next box.
- Output is received in the 2nd column output box.
