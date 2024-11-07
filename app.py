import  streamlit as st
import os
import langchain_groq as chatgroq
from langchain_groq import chatgroq
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
import time

python
import langchain_groq
from langchain_objectbox.vectorestores import ObjectBox  # or the specific class you need
from dotenv import load_dotenv
load_dotenv()
# loading yje groq and hugging face
os.environ["HuggingFace_API_KEY"] = os.getenv("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")
os.environ["GROQ_API_KEY"] = os.getenv("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")
llm= chatgroq(groq_api_key = groq_api_key,model="LIama3_8b_8192")
prompt = ChatPromptTemplate.from_template(''')