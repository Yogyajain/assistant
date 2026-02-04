import pdfplumber
from collections import Counter
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pdf_PATH = os.path.join(BASE_DIR, "assets", "Lower Income Group Scheme.pdf")

pdf_path='assets/Lower Income Group Scheme.pdf'

def extract_pages_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = []
        for page in pdf.pages:
            pages.append(page.extract_text())
        return pages

# pages = extract_pages_text(pdf_PATH)
def extract_pages(pages):
    lines = []
    for page in pages:
        if page:
            lines.extend(page.split("\n"))

    line_counts = Counter(lines)
    common_lines = {line for line, count in line_counts.items() if count > 3}
    return common_lines

def clean_page(text, common_lines):
    return "\n".join(
        line for line in text.split("\n")
        if line not in common_lines
    )

def preprocess_pdf(pdf_path):
    pages = extract_pages_text(pdf_path)
    common_lines = extract_pages(pages) 
    cleaned_pages = [clean_page(page, common_lines) for page in pages]
    return cleaned_pages
