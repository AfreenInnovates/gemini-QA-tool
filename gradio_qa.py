import os
from dotenv import load_dotenv
import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0, google_api_key=api_key)

prompt = PromptTemplate.from_template(
    "Context:\n\"\"\"\n{context}\n\"\"\"\n\nQuestion: {question}\nAnswer concisely:"
)
chain = LLMChain(llm=llm, prompt=prompt)

def respond(context, question):
    return chain.run(context=context, question=question).strip()

ui = gr.Interface(
    fn=respond,
    inputs=[
      gr.Textbox(lines=10, label="Document Content"),
      gr.Textbox(lines=2, label="Your Question")
    ],
    outputs="text",
    title="Gemini Q&A Tool",
    allow_flagging="never"
)
ui.launch()
