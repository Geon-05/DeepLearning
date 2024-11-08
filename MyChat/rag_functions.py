import os
import json
import streamlit as st

from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate

import google.generativeai as genai

# 파일 읽기
with open(r'D:\OneDrive\human\port-folio\personal_project\DeepLearning\day00_preparation\data\APIkey.json', 'r') as file:
    data = json.load(file)  # JSON 파일을 파이썬 딕셔너리로 로드

# 환경 변수에서 API 키 가져오기
api_key = data['Gemini']

os.environ["OPENAI_API_KEY"] = api_key

def load_docs(query):
    loader = WikipediaLoader(query=query, load_max_docs=1)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(documents)
    
    return splits

def create_vectorstore(splits):
    embeddings = genai.get_embeddings
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    return vectorstore

def create_rag_chain(vectorstore):
    # Gemini 모델 사용
    model = "gemini-1.5-pro"  # 원하는 Gemini 모델 선택

    # 프롬프트 조정
    prompt_template = """
    지식베이스를 참고하여 질문에 대한 답변을 생성해주세요. 답변은 최대한 간결하고 명확하게 요약하며, 필요한 경우 핵심적인 증거를 제시해주세요.
    **지식베이스:** {context}
    **질문:** {question}
    **답변:**
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Gemini API를 사용하여 체인 생성
    chain = genai.create_chain(
        llm=model,
        prompt=PROMPT,
        vectorstore=vectorstore
    )

    return chain