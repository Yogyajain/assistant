from agents.preprocessing import preprocess_pdf
from agents.helper import get_retrieval
from agents.sub_agents import run_chain
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# pdf_PATH = os.path.join(BASE_DIR, "assets", "Lower Income Group Scheme.pdf")
# pdf_PATH = os.path.join(BASE_DIR, "assets", "Lower Income Group Scheme.pdf")
paths=['assets/Post Matric Scholarship Students With Disabilities.pdf','assets/Lower Income Group Scheme.pdf']
pdf_path='assets/Post Matric Scholarship Students With Disabilities.pdf'
def chain(request: str) -> str:
    texts=[]
    for path in paths:
        cleaned_pages = preprocess_pdf(path)
        texts.append(cleaned_pages)
    retrieval = get_retrieval(cleaned_pages)
    chain=run_chain(retrieval)
    res=chain.invoke(request)
    return res