import os
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import openai # type: ignore
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import json

# 파일 읽기
with open(r'D:\OneDrive\human\port-folio\personal_project\DeepLearning\day00_preparation\data\APIkey.json', 'r') as file:
    data = json.load(file)  # JSON 파일을 파이썬 딕셔너리로 로드

# 환경 변수에서 API 키 가져오기
api_key = data['OpenAI']

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
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    return vectorstore

def create_rag_chain(vectorstore):
    llm = openai(model_name="gpt-3.5-turbo", temperature=0)
    
    prompt_template = """아래의 문맥을 사용하여 질문에 답하십시오.
    만약 답을 모른다면, 모른다고 말하고 답을 지어내지 마십시오.
    최대한 세 문장으로 답하고 가능한 한 간결하게 유지하십시오.
    {context}
    질문: {question}
    유용한 답변:"""
    
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs=chain_type_kwargs,
        return_source_documents=True
    )
    
    return qa_chain