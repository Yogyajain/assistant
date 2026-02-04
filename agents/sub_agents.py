from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableMap, RunnableLambda
from langchain_core.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
# from agents.helper import retrieval
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"]
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    # hallucination control
    temperature=0,
    # top_p=0.1,
    # top_k=1,
)



# Fix the RunnableMap implementation
def run_chain(retrieval):
    prompt=""" You are a retrieval-based QA system.

You must answer ONLY using the information provided in the given context/document.
Do NOT use your own knowledge, memory, assumptions, or external information.

Rules:
1. If the answer is clearly present in the context, answer concisely and accurately.
2. If the answer is partially present, answer only with the available facts.
3. If the answer cannot be found or inferred directly from the context, respond exactly with:
   "I don't know based on the provided data."
4. Do not guess.
5. Do not fabricate information.
6. Do not add extra explanations beyond the context.
Never:
- Assume
- Infer missing facts
- Use prior knowledge
- Hallucinate
- Generate examples not in the context

Only extract and rephrase facts from the context.

Format your final response as follows:
Answer Format:
- Maximum 2 to 3 sentences OR 40 words
- Plain text only
- No reasoning steps
- No extra commentary
- Direct answer only
Context: 
{context}


Question:
{question}
"""
    prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(prompt),
    HumanMessagePromptTemplate.from_template("{question}") 
    ])
    chain = retrieval | prompt_template | llm | StrOutputParser()
    return chain

