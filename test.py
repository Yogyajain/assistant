from agents.pipeline import chain
from agents.preprocessing import preprocess_pdf
from agents.helper import get_retrieval
from agents.sub_agents import run_chain
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader
# from langchain.docstore.document import Document


load_dotenv()

loader = TextLoader("test_db.txt", encoding="utf-8")
documents = loader.load()
res=chain("How am i eligible for the scholarship?")
print(res)
# request="What is objective for the Lower Income Group Scheme?"
# request="What are the schorlarships for disabled students provided by the government of India?"

# retrieval = get_retrieval(documents)
# chain=run_chain(retrieval)
# res=chain.invoke(request)
# print(res)