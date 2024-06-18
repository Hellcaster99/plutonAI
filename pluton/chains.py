import os
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain

from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

llm = GoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=os.environ['GOOGLE_API_KEY'])


# ----------- Multi Model -------------------------------

# system_prompt_summ = (
#     "You are an assistant for summarizing task."
#     "Use the following pieces of retrieved context to summarize "
#     "in not more than n words. If you don't know the answer, say that you "
#     "don't know. "
#     "\n\n"
#     "{context}"
# )

# system_prompt_qna = (
#     "You are an assistant for question-answering tasks. "
#     "Use the following pieces of retrieved context and history to answer "
#     "the question. If you don't know the answer, say that you "
#     "don't know. "
#     "\n\n"
#     "{context}"
#     "{history}"
# )

# prompt_summ = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt_summ),
#         ("human", "{input} {n}")
#     ]
# )

# prompt_qna = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt_qna),
#         ("human", "{input}")
#     ]
# )

# ----------- Single Model -------------------------------

system_prompt = (
    "You are an assistant for summarizing and question-answering tasks. "
    "Use the following pieces of retrieved context and history and perform the "
    "given input task. If you don't know the answer, say that you "
    "don't know. "
    "\n\n"
    "{context}"
    "{history}"
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

# ------------------ RAG ---------------------------------

# Multi
# summarizer_chain = create_stuff_documents_chain(llm=llm, prompt=prompt_summ)

# qna_chain = create_stuff_documents_chain(llm=llm, prompt=prompt_qna)

# Single
# chain = create_stuff_documents_chain(llm, prompt)


# -------------------- Without RAG -------------------------------------

# Multi
# summarizer_chain = prompt_summ | llm | StrOutputParser()

# qna_chain = prompt_qna | llm | StrOutputParser()

# Single
chain = prompt | llm | StrOutputParser()