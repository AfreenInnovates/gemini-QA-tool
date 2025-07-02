import os
import fitz 
import gradio as gr
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.0,
    google_api_key=api_key
)

prompt = PromptTemplate.from_template(
    "Context:\n\"\"\"\n{context}\n\"\"\"\n\nQuestion: {question}\nAnswer:"
)

chain = prompt | llm

def extract_text(file_path):
    doc = fitz.open(file_path)
    return "\n".join(page.get_text() for page in doc)

def answer_question(pdf_file, question):
    if not pdf_file or not question:
        return "Please upload a PDF and ask a question."

    try:
        context = extract_text(pdf_file.name)
        response = chain.invoke({"context": context, "question": question})
        return response.content.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

gr.Interface(
    fn=answer_question,
    inputs=[
        gr.File(label="Upload PDF"),
        gr.Textbox(label="Ask a Question")
    ],
    outputs="text",
    title="Simple Q&A Tool",
    description="Upload a PDF and questions",
    allow_flagging="never"
).launch()
