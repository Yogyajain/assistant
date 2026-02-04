from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()
loader = TextLoader("test_db.txt", encoding="utf-8")
documents = loader.load()

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vecstore_a = DocArrayInMemorySearch.from_documents(
    documents,
    embedding=embedding
)
retriever_a = vecstore_a.as_retriever()

retrieval_a = RunnableParallel(
    {
        "context_a": retriever_a, 
        "question": RunnablePassthrough()
    }
)



def get_retrieval(documents_text):  
    vecstore_b= DocArrayInMemorySearch.from_texts(
        documents_text,
        embedding=embedding
    )
    retriever_b= vecstore_b.as_retriever()
    retrieval_b= RunnableParallel(
        {
            "context": retriever_b, 
            "question": RunnablePassthrough()
        }
    )
    return retrieval_b
