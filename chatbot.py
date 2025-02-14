import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from vectorstore import load_vectorstore

load_dotenv()
vectordb = load_vectorstore()
retriever = vectordb.as_retriever()

llm = HuggingFaceHub(repo_id="meta-llama/Meta-Llama-3-8B-Instruct")

template_1 = """Given the following context and a question, generate an answer based on this context only.
In the answer, try to provide as much text as possible from the "response" section in the source documents.
If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

Question: {question}
Context: {context}

Response:"""

prompt = ChatPromptTemplate.from_template(template_1)
output_parser = StrOutputParser()

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | output_parser
)

def get_response(query):
    return rag_chain.invoke(query)
