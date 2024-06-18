import sys
import os

from langchain.chains import create_retrieval_chain

# from pluton.chains import summarizer_chain, qna_chain
from pluton.chains import chain

# ------------ RAG ---------------------------------------

# def plutonSummarize(retriever, n: int):
#     rag_chain = create_retrieval_chain(retriever, summarizer_chain)
#     return rag_chain.stream({'n': n, 'input': 'What are the key points in the article ?'})

# def askPluton(retriever, query, history):
#     rag_chain = create_retrieval_chain(retriever, qna_chain)
#     return rag_chain.stream({'input': query, 'history': history})

# Single
# def Pluton(retriever, query):
#     rag_chain = create_retrieval_chain(retriever, chain)
#     return rag_chain.stream({'input':query})


# ------------ Without RAG -------------------------------

# Multi
# def plutonSummarize(context, n: int):
#     return summarizer_chain.stream({'context': context,'n': n, 'input': 'What are the key points in the article ?'})

# def askPluton(context, query, history):
#     return qna_chain.stream({'context':context, 'input': query, 'history': history})

# Single 
def Pluton(context, query, history):
    return chain.stream({'context':context, 'input':query, 'history':history})
